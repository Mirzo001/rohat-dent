
from django.contrib import admin
from doctors.models import Appointment, Time
# admin.site.register(Appointment)
admin.site.register(Time)



class AppointmentAdmin(admin.ModelAdmin):
    
    search_fields = ['patient__name','time']
    
    list_display = ['date','time', 'patient','doctor']
    autocomplete_fields = ['patient']
    
    list_filter = ['doctor']
    
    

    
admin.site.register(Appointment,AppointmentAdmin)