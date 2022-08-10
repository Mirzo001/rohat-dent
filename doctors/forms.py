

from django import forms

from patients.models import Patient




from .models import Appointment

class AppointmentEditForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ('patient','date', 'time','status','qaydlar')
        # fields = '__all__'

class StatusEditForm(forms.ModelForm):
    
    class Meta:
        model = Appointment
        fields = ['status']
        # fields = '__all__'
# class AppointmentCreateForm(forms.ModelForm):
    
#     class Meta:
#         model = Appointment
#         fields = ('patient','date', 'time','status','qaydlar')
        
        


# class AppointmentCreateForm(forms.Form):
#     patient = forms.ChoiceField()
#     date = forms.DateField()
#     time = forms.TimeField()
#     status = forms.CharField(max_length=30)
#     qaydlar = forms.Textarea()



class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        results=Patient.objects.all()
        
        # fields = '__all__'
        # fields = ['title', 'content', 'is_published', 'category']
        fields = ['doctor','patient','date', 'time','status','qaydlar']
        
        # widgets = {
        #     'doctor': forms.Select(attrs={'class': 'form-control'}),
        #     'patient': forms.Select(attrs={'class': 'form-control','appointment':results}),
        #     'status': forms.Select(attrs={'class': 'form-control'}),
        #     # 'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'qaydlar': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        #     'date': forms.DateInput(attrs={'class': 'form-control'}),
        #     'time': forms.TimeInput(attrs={'class': 'form-control'}),
        # }
