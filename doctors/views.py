
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from accounts.models import CustomUser
from doctors.forms import AppointmentCreateForm, AppointmentEditForm, StatusEditForm
from doctors.models import STATUS_CHOICES, Appointment, Time
from django.shortcuts import redirect, render
from django.views import View

from django.http import JsonResponse
import datetime

from patients.models import Patient




class AppointmentListView(LoginRequiredMixin,ListView):
    """
    View for the day
    
    """
    model = Appointment
    template_name = 'dashboard/dashboard.html'
        
    def get_context_data(self,**kwargs):
        doctor = CustomUser.objects.all()
        appointment = Appointment.objects.filter(doctor=self.request.user)
        search = self.request.GET.get("search")
        # appointment = Appointment.objects.all()
        time = Time.objects.all()
        # query = self.request.GET.get('q','')
        # if query:
        #     appointment = self.model.objects.filter(patient__name__icontains=query)
        today = datetime.date.today()
        if search:
            
            appointment = appointment.filter(patient__name__icontains=search)
        
        context = super(AppointmentListView,self).get_context_data(**kwargs)
        context={
            'search':search or "",
            'today':today,
            'appointment':appointment,
            'time':time,
            # 'query':query,
            'doctor':doctor,
        }
        return context




class AppointmentDetail(LoginRequiredMixin,DetailView ):
    model = Appointment
    template_name = 'appointment/appointment_detail.html'
    pk_url_kwarg = "pk"

from django.db.models import Q


def CreateAppointmentView(request):
    
    patients=Patient.objects.filter(doctor=request.user)
    # q = request.GET.get('q')
    # query = Q(name__contains=q) | Q(surname__contains=q) 
    # patients=Patient.objects.filter(query)   
    # query = request.GET.get('q','')
    # if query:
    #     patients = Patient.objects.filter(name__icontains=query)
    if request.method == 'POST':
        form = AppointmentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AppointmentCreateForm()
        
    return render(request, 'appointment/new1.html', {'form': form,'patients':patients,})
    



class HomeView(TemplateView):
    template_name = 'home.html'
    


class EditStatusView(LoginRequiredMixin, View):
    def get(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment_form = StatusEditForm(instance=appointment)
        # json = JsonResponse({'data': Appointment.objects.get(id=pk)})
        return render(request, "dashboard/dashboard_search.html", {"appointment": appointment,"appointment_form": appointment_form})

    def post(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment_form = StatusEditForm(instance=appointment, data=request.POST)
    
        # appointment_form.save()
        
        if appointment_form.is_valid():
            appointment_form.save()
            return redirect('dashboard')
            
        print(request.POST)
        return render(request, "dashboard/dashboard_search.html", {"appointment": appointment,"appointment_form": appointment_form})
    
class EditAppointmentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment_form = AppointmentEditForm(instance=appointment)
        # json = JsonResponse({'data': Appointment.objects.get(id=pk)})
        return render(request, "appointment/appointment_edit.html", {"appointment": appointment,"appointment_form": appointment_form,'data': Appointment.objects.all()})

    def post(self, request, pk):
        appointment = Appointment.objects.get(id=pk)
        appointment_form = AppointmentEditForm(instance=appointment, data=request.POST)
    
        # appointment_form.save()
        
        if appointment_form.is_valid():
            appointment_form.save()
            return redirect('dashboard')
            
        print(request.POST)
        return render(request, "appointment/appointment_edit.html", {"appointment": appointment,"appointment_form": appointment_form})


class DeleteAppointmentView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'appointment/appointment_delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        obj = self.get_object() 
        return obj.doctor == self.request.user
        

    
    
class DoctorProfileView(TemplateView):
    model = CustomUser
    template_name = 'doctor_profile.html'
    
    

def autosuggest(request):
    
    query_original = request.GET.get('term')
    queryset = Patient.objects.filter(name__icontains=query_original)
   
    mylist = []
    mylist += [x.name for x in queryset] 
    return JsonResponse(mylist, safe=False)  


def showlist(request):
    patients=Patient.objects.all()
    return render(request, "appointment/appointment_new.html",{"patients":patients})

def dashboard_search(request):
    search = request.GET.get("search")
    appointment = Appointment.objects.all()
    time = Time.objects.all()
    today = datetime.date.today()
    if search:
        appointment = Appointment.objects.filter(doctor=request.user)
        appointment = appointment.filter(patient__name__icontains=search)


    context = {"appointment": appointment, "search": search, "time":time,"today":today}
    return render(request, "dashboard/dashboard_search.html", context)



def form_search(request):
    search = request.GET.get("search")
    patient = Patient.objects.all()
   
    if search:
        patient = Patient.objects.filter(name__icontains=search)
        print(patient)


    context = {"patient": patient, "search": search, }
    return render(request, "appointment/new.html", context)


from django.core.paginator import Paginator


class AppFullListView(LoginRequiredMixin, View):
    """
    Full list of apps View
    
    """
    
    def get(self, request):
        
        
        appointments = Appointment.objects.filter(doctor=request.user).order_by('date')
        
        paginator = Paginator(appointments, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            "appointment":appointments,
            'page_obj': page_obj,
            # 'lineitem':lineitem
        }
        
        return render(self.request, 'appointment/full-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        app_id = request.POST.getlist("app_id")
        app_id = list(map(int, app_id))

        update_status_for_apps = request.POST['status']
        appointment = Appointment.objects.filter(id__in=app_id)
        # import pdb;pdb.set_trace()
        if update_status_for_apps == "Yakunlandi":
            appointment.update(status="Yakunlandi")
        elif update_status_for_apps == "Kutilmoqda":
            appointment.update(status="Kutilmoqda")
        else:
            appointment.update(status="Bekor qilindi")

        return redirect('app-full-list')


def full_applist_search(request):
    search = request.GET.get("search")
    appointments = Appointment.objects.filter(doctor=request.user).order_by('date')
    paginator = Paginator(appointments, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if search:
        page_obj = appointments.filter(patient__name__icontains=search).order_by('date')
        

    context = {"search": search, 'page_obj': page_obj}
    return render(request, 'appointment/full-list-search.html', context)