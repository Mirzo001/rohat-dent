from doctors.models import Appointment, Time
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from accounts.models import CustomUser
from django.views.generic import ListView
from django.shortcuts import render

# today = datetime.date.today()  
# dushanba = today + datetime.timedelta(1 - today.weekday() - 1)
# seshanba =  today + datetime.timedelta(2 - today.weekday() - 1)
# chorshanba =  today + datetime.timedelta(3 - today.weekday() - 1)
# payshanba = today + datetime.timedelta(4 - today.weekday() - 1)
# juma = today + datetime.timedelta(5 - today.weekday() - 1)
# shanba = today + datetime.timedelta(6 - today.weekday() - 1)
# yakshanba =  today + datetime.timedelta(7 - today.weekday() - 1)

today = datetime.date.today()  
dushanba = today + datetime.timedelta(0 - today.weekday())
seshanba =  today + datetime.timedelta(1 - today.weekday())
chorshanba =  today + datetime.timedelta(2 - today.weekday())
payshanba = today + datetime.timedelta(3 - today.weekday())
juma = today + datetime.timedelta(4 - today.weekday())
shanba = today + datetime.timedelta(5 - today.weekday())
yakshanba =  today + datetime.timedelta(6 - today.weekday())

dict_week = {
            'dushanba':dushanba,
            'seshanba':seshanba,
            "chorshanba":chorshanba,
            "payshanba":payshanba,
            "juma":juma,
            "shanba":shanba,
            "yakshanba":yakshanba,
        }

class WeekView(LoginRequiredMixin, ListView):
    """
    View for the week
    
    """
    model = Appointment
    template_name = 'dashboard/dashboard_week.html'
    

    
    def get_context_data(self,**kwargs):
        doctor = CustomUser.objects.all()
        appointment = Appointment.objects.filter(doctor=self.request.user)
        time = Time.objects.all()
        
        context = super(WeekView,self).get_context_data(**kwargs)
        context={
            'dictweek':dict_week,
            'today':today,
            'appointment':appointment,
            'time':time,
            'doctor':doctor,
        }
        return context
    
    
def dashboard_week_search(request):
    doctor = CustomUser.objects.all()

    search = request.GET.get("search")
    appointment = Appointment.objects.all().filter(doctor=request.user)
    time = Time.objects.all()
    if search:
        appointment = Appointment.objects.filter(doctor=request.user).filter(patient__name__icontains=search)
        # appointment = appointment.filter(patient__name__icontains=search)


    context = {
        "appointment": appointment,
        'dictweek':dict_week,
        "search": search,
        "time":time,
        "today":today,
        'doctor':doctor,
        }
    return render(request, "dashboard/dashboard_week_search.html", context)

"""
    View for the next week
    
    """
next_dushanba = today + datetime.timedelta(7 - today.weekday())
next_seshanba =  today + datetime.timedelta(8 - today.weekday())
next_chorshanba =  today + datetime.timedelta(9 - today.weekday())
next_payshanba = today + datetime.timedelta(10 - today.weekday())
next_juma = today + datetime.timedelta(11 - today.weekday())
next_shanba = today + datetime.timedelta(12 - today.weekday())
next_yakshanba =  today + datetime.timedelta(13 - today.weekday())

next_dict_week = {
            'dushanba':next_dushanba,
            'seshanba':next_seshanba,
            "chorshanba":next_chorshanba,
            "payshanba":next_payshanba,
            "juma":next_juma,
            "shanba":next_shanba,
            "yakshanba":next_yakshanba,
        }

class NextWeekView(LoginRequiredMixin, ListView):
    """
    View for the next week
    
    """
    model = Appointment
    template_name = 'dashboard/dashboard_next_week.html'
    

    
    def get_context_data(self,**kwargs):
        doctor = CustomUser.objects.all()
        appointment = Appointment.objects.filter(doctor=self.request.user)
        time = Time.objects.all()
        
        context = super(NextWeekView,self).get_context_data(**kwargs)
        context={
            'dictweek':next_dict_week,
            # 'today':today,
            'appointment':appointment,
            'time':time,
            'doctor':doctor,
        }
        return context
    
def dashboard_next_search(request):
    doctor = CustomUser.objects.all()

    search = request.GET.get("search")
    appointment = Appointment.objects.all().filter(doctor=request.user)
    time = Time.objects.all()
    if search:
        appointment = Appointment.objects.filter(doctor=request.user).filter(patient__name__icontains=search)
        # appointment = appointment.filter(patient__name__icontains=search)


    context = {
        "appointment": appointment,
        'dictweek':next_dict_week,
        "search": search,
        "time":time,
        "today":today,
        'doctor':doctor,
        }
    return render(request, "dashboard/dashboard_week_search.html", context)


prev_dushanba = today + datetime.timedelta(today.weekday()-9)
prev_seshanba =  today + datetime.timedelta(today.weekday() - 8)
prev_chorshanba =  today + datetime.timedelta(today.weekday()-7)
prev_payshanba = today + datetime.timedelta(today.weekday()-6)
prev_juma = today + datetime.timedelta(today.weekday()-5)
prev_shanba = today + datetime.timedelta(today.weekday()-4)
prev_yakshanba =  today + datetime.timedelta(today.weekday()-3)

prev_dict_week = {
            'dushanba':prev_dushanba,
            'seshanba':prev_seshanba,
            "chorshanba":prev_chorshanba,
            "payshanba":prev_payshanba,
            "juma":prev_juma,
            "shanba":prev_shanba,
            "yakshanba":prev_yakshanba,
        }
class PrevWeekView(LoginRequiredMixin, ListView):
    """
    View for the week
    
    """
    model = Appointment
    template_name = 'dashboard/dashboard_prev_week.html'
    

    
    def get_context_data(self,**kwargs):
        doctor = CustomUser.objects.all()
        appointment = Appointment.objects.filter(doctor=self.request.user)
        time = Time.objects.all()
        
        context = super(PrevWeekView,self).get_context_data(**kwargs)
        context={
            'dictweek':prev_dict_week,
            # 'today':today,
            'appointment':appointment,
            'time':time,
            'doctor':doctor,
        }
        return context
    
def dashboard_prev_search(request):
    doctor = CustomUser.objects.all()

    search = request.GET.get("search")
    appointment = Appointment.objects.all().filter(doctor=request.user)
    time = Time.objects.all()
    if search:
        appointment = Appointment.objects.filter(doctor=request.user).filter(patient__name__icontains=search)
        # appointment = appointment.filter(patient__name__icontains=search)


    context = {
        "appointment": appointment,
        'dictweek': prev_dict_week,
        "search": search,
        "time": time,
        "today": today,
        'doctor': doctor,
        }
    return render(request, "dashboard/dashboard_prev_search.html", context)