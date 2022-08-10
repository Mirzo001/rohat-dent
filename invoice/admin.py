from django.contrib import admin

from .models import Invoice, LineItem

class InvoiceAdmin(admin.ModelAdmin):
    
    search_fields = ['patient__name']
    
    list_display = ['patient']
    autocomplete_fields = ['patient']



class LineAdmin(admin.ModelAdmin):
    
    # search_fields = ['patient__name']
    
    list_display = ['patient']
    autocomplete_fields = ['patient']
    
    # list_filter = ['doctor']
    
admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(LineItem, LineAdmin)
# Register your models here.
