from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View

from patients.models import Patient
from .models import LineItem, Invoice
from .forms import LineItemFormset, InvoiceForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


def invoice_search(request):
    search = request.GET.get("search")
    invoices = Invoice.objects.filter(doctor=request.user)
    paginator = Paginator(invoices, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if search:
        page_obj = invoices.filter(patient__name__icontains=search)
        print(invoices)

    context = {"search": search, 'page_obj': page_obj}
    return render(request, 'invoice/invoice-list1.html', context)

class InvoiceListView(LoginRequiredMixin, View):
    def get(self, request):
        
        
        invoices = Invoice.objects.filter(doctor=request.user)
        
        paginator = Paginator(invoices, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "invoices":invoices,
            'page_obj': page_obj,
            # 'lineitem':lineitem
        }
        
        return render(self.request, 'invoice/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice:invoice-list')


def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """
    if request.user.is_authenticated:
        patients=Patient.objects.filter(doctor=request.user)
    
        
        if request.method == 'GET':
            formset = LineItemFormset(request.GET or None)
            form = InvoiceForm(request.GET or None)
        elif request.method == 'POST':
            
            
            # if request.POST.get('service') == None:
            #     return render(request, "invoice/invoice-create.html",{'error':True})
            form = InvoiceForm(request.POST)
            formset = LineItemFormset(request.POST)
            # customer = Patient.objects.get_or_create()
            
            if form.is_valid():
                invoice = Invoice.objects.create(patient=form.cleaned_data.get("patient"),doctor=request.user,
                        date=form.data["date"],
                        # due_date=form.data["due_date"], 
                        # message=form.data["message"],
                        )
                # invoice.save()
                
            if formset.is_valid():
                
                # import pdb;pdb.set_trace()
                # extract name and other data from each form and save
                total = 0
                for form in formset:
                    
                    service = form.cleaned_data.get('service')
                    quantity = form.cleaned_data.get('quantity')
                    rate = form.cleaned_data.get('rate')
                    
                    if service and quantity and rate:
                        amount = float(rate)*float(quantity)
                        total += amount
                        LineItem(patient=invoice,
                                service=service,
                                quantity=quantity,
                                rate=rate,
                                amount=amount,
                                ).save()
                invoice.total_amount = total
                # print(request.POST.get('service'))
                # print(request.POST.get('quantity'))
                # print(request.POST.get('rate'))
                invoice.save()
                # try:
                #     generate_PDF(request, id=invoice.id)
                # except Exception as e:
                #     print(f"********{e}********")
                
                
                return redirect('invoice:invoice-list')
            
        context = {
            "patients":patients,
            "title" : "Invoice Generator",
            "formset": formset,
            "form": form,
            
        }
        return render(request, 'invoice/invoice-create.html', context)


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()

    context = {
        "company": {
            "name": "Rohat Dent",
            "address" :"Istiqlol ko'chasi, 34",
            "phone": "(998) 99 2292240",
            "email": "xmirzo001@gmail.com",
        },
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "patient": invoice.patient,
        "date": invoice.date,
        "lineitem": lineitem,

    }
    return render(request, 'invoice/pdf_template.html', context)

# def generate_PDF(request, id):
#     # Use False instead of output path to save pdf to a variable
#     pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False)
#     response = HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

#     return response


# def change_status(request):
#     return redirect('invoice:invoice-list')

# def view_404(request,  *args, **kwargs):

#     return redirect('invoice:invoice-list')

class DeleteInvoiceView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Invoice
    template_name = 'invoice/invoice_delete.html'
    success_url = reverse_lazy('invoice:invoice-list')

    def test_func(self): 
        return self.request.user
        