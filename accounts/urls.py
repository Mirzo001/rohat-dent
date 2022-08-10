from django.urls import path
from .views import SignUpView, UserChangeView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('change/<int:pk>', UserChangeView.as_view(), name='change'),
]
