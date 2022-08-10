from pydoc import doc
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from doctors.models import Appointment, Patient
from django.urls import reverse_lazy
from django.shortcuts import redirect
from patients.forms import PatientCreateForm
from accounts.models import CustomUser
from django.http import JsonResponse
from django.shortcuts import render




class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patients/patients.html'
    
    def get_context_data(self,**kwargs):
        # doctor = CustomUser.objects.all()
        # print(doctor)
        # patient = Patient.objects.all()
        patients = Patient.objects.filter(doctor=self.request.user).order_by('name')
    
        # query = self.request.GET.get('q','')
        # if query:
        #     patients = self.model.objects.filter(name__icontains=query)
    
        context = super(PatientListView,self).get_context_data(**kwargs)
        context={
            # 'patient':patient,
            'patients': patients,
            # 'doctor':doctor,
            # 'query':query,
        } 
        return context
    
class CreatePatientView(LoginRequiredMixin, CreateView, UserPassesTestMixin):
    model = Patient
    template_name = 'patients/patients_new.html'
    fields = ['name','phone','address','date_recorded','diagnoz']
    
    def test_func(self):
        return self.request.user
    
    def post(self, request):
        form = PatientCreateForm(data=request.POST)
        form.save()
        return redirect(reverse_lazy('patients'))
    
    success_url = reverse_lazy('patients')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)
    
    # def test_func(self):
    #     return self.request.user.is_superuser
    # success_url = reverse_lazy('patients')
    
class EditPatientView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ('name','phone','address','diagnoz')
    template_name = 'patients/patients_edit.html'

    def test_func(self):
        return self.request.user   
     
    
    success_url = reverse_lazy('patients')

class PatientDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patients/patients_delete.html'
    success_url = reverse_lazy('patients')

    def test_func(self):
        obj = self.get_object() 
        return obj.doctor == self.request.user
    
class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patients/patients_detail.html'
    pk_url_kwarg = "pk"

def autosuggest(request):
    print(request.GET)
    query_original = request.GET.get('term')
    queryset = Patient.objects.filter(name__icontains=query_original)
    print(queryset)
    mylist = []
    mylist += [x.name for x in queryset] 
    return JsonResponse(mylist, safe=False)  

def patient_search(request):
    print(request.user)
    search = request.GET.get("search")
    # patient = Patient.objects.all()
    patients = Patient.objects.filter(doctor=request.user)

    if search:
        patients = Patient.objects.filter(doctor=request.user).filter(name__icontains=search).order_by('name')
        # patients = Patient.objects.filter(name__icontains=search)


    context = {"patients": patients, "search": search}
    return render(request, "patients/patient_search.html", context)

from django.core import serializers
from django.http.response import JsonResponse

def patient_list_view(request):
    """ get json data """
    patients = serializers.serialize(
        'json', 
        Patient.objects.all(), 
        fields=('name',)
    )
    return JsonResponse({'patients': patients}, status=200)



# def CreateBillView(request):
#     form = BillCreateForm(request.GET or None)
    
#     patients=Patient.objects.filter(doctor=request.user)
#     if request.method == 'GET':
            
#             form = BillCreateForm(request.GET or None)
#     # q = request.GET.get('q')
#     # query = Q(name__contains=q) | Q(surname__contains=q) 
#     # patients=Patient.objects.filter(query)   
#     # query = request.GET.get('q','')
#     # if query:
#     #     patients = Patient.objects.filter(name__icontains=query)
#     if request.method == 'POST':
        
#         # amount = request.POST['amount']
#         # quantity = request.POST['quantity']
        
#         # total = float(amount*quantity)
#         # print(total)
#         form = BillCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = BillCreateForm()
        
#     return render(request, 'bill/invoice-create.html', {'form': form,'patients':patients,})


# from django.views import View
# from django.core.paginator import Paginator

# class BillListView(LoginRequiredMixin, View):
#     def get(self, request):
        
        
#         bills = PatientBill.objects.order_by('payment_date')
        
#         paginator = Paginator(bills, 20)
#         page_number = request.GET.get('page')
#         page_obj = paginator.get_page(page_number)

#         context = {
#             "bills":bills,
#             'page_obj': page_obj,
#             # 'lineitem':lineitem
#         }
        
#         return render(self.request, 'bill/invoice-list.html', context)