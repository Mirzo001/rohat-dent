from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect

from accounts.models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
    
class UserChangeView(UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/change.html'


class SignUpView(CreateView):
    # model = CustomUser
    form_class = CustomUserCreationForm

    template_name = 'registration/signup.html'
    # fields = ['username','password']
    
    # def test_func(self):
    #     return self.request.user.is_anonymous
    
    
    # def post(self, request):
    #     form = CustomUserCreationForm(data=request.POST)
    #     form.save()
    #     return redirect(reverse_lazy('dashboard'))
    
   
    success_url = reverse_lazy('dashboard')