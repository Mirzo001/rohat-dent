from django.contrib import admin

from patients.models import Patient



class PatientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    
    list_display = ['name','doctor','diagnoz']
    # autocomplete_fields = ['patient__name']
    list_filter = ['name']    


class PatientBillAdmin(admin.ModelAdmin):
    search_fields = ['name']
    
    # list_display = ['name','doctor','diagnoz']
    
    
    
admin.site.register(Patient, PatientAdmin)
# admin.site.register(PatientBill, PatientBillAdmin)


