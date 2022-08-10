from dataclasses import field
from django import forms

from .models import Patient

class PatientEditForm(forms.ModelForm):
    
    class Meta:
        model = Patient
        # fields = ('patient','date', 'time','status')
        fields = '__all__'

class PatientCreateForm(forms.ModelForm):
  
    class Meta:
        model = Patient
        fields = ('name','phone','address','date_recorded','doctor','diagnoz')
        
        
# class BillCreateForm(forms.ModelForm):
#     class Meta:
#         model = PatientBill
        
        
#         fields = '__all__'
#         # fields = ['title', 'content', 'is_published', 'category']
        
#     service = forms.CharField(
#         label='Service/Product',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control input',
#             'placeholder': 'Service Name'
#         })
#     )
   
#     quantity = forms.IntegerField(
#         label='Qty',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control input quantity',
#             'placeholder': 'Quantity'
#         }) #quantity should not be less than one
#     )
#     amount = forms.FloatField(
#         label='Rate $',
#         widget=forms.TextInput(attrs={
#             'class': 'form-control input rate',
#             'placeholder': 'Rate'
#         })
#     )

