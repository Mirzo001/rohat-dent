from django import forms
from django.forms import formset_factory
from .models import Invoice, LineItem

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        
        
        fields = ['patient']
# class InvoiceForm(forms.Form):
    
#         # fields = ['customer', 'message']
#     customer = forms.CharField(
#         label='Customer',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Customer/Company Name',
#             'rows':1
#         })
#     )
    # customer_email = forms.CharField(
    #     label='Customer Email',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'customer@company.com',
    #         'rows':1
    #     })
    # )
    # billing_address = forms.CharField(
    #     label='Billing Address',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': '',
    #         'rows':1
    #     })
    # )
    # message = forms.CharField(
    #     label='Message/Note',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'message',
    #         'rows':1
    #     })
    # )
    
class LineItemForm(forms.Form):
    
    service = forms.CharField(
        required=True,
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'required':True,
            'class': 'form-control input',
            'placeholder': 'XIZMAT TURI'
        })
    )
   
    quantity = forms.IntegerField(
        required=True,
        label='Qty',
        widget=forms.TextInput(attrs={
            'required':True,
            'class': 'form-control input quantity',
            'placeholder': 'SONI'
        }) #quantity should not be less than one
    )
    rate = forms.DecimalField(
        required=True,
        label='Rate $',
        widget=forms.TextInput(attrs={
            'required':True,
            'class': 'form-control input rate required',
            'placeholder': 'NARXI'
        })
    )
    
  
        # return any errors if found
        
    
    # amount = forms.DecimalField(
    #     disabled = True,
    #     label='Amount $',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control input',
    #     })
    # )
    
LineItemFormset = formset_factory(LineItemForm, extra=1)