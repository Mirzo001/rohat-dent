from django.urls import path
from doctors.calendar_views import NextWeekView, PrevWeekView, WeekView, dashboard_next_search, dashboard_prev_search, dashboard_week_search
from doctors.forms import StatusEditForm
from .views import AppFullListView, dashboard_search, EditStatusView,AppointmentDetail, AppointmentListView, DeleteAppointmentView, HomeView, CreateAppointmentView, EditAppointmentView, DoctorProfileView,autosuggest, form_search, full_applist_search, showlist

urlpatterns = [
    
    path('dashboard/', AppointmentListView.as_view(), name='dashboard'),
    
    # week path
    path('dashboard/week', WeekView.as_view(), name='dashboard_week'),
    path('dashboard/nextweek', NextWeekView.as_view(), name='dashboard_next_week'),
    path('dashboard/prevweek', PrevWeekView.as_view(), name='dashboard_prev_week'),

    path("autosuggest/", autosuggest, name="autosuggest"),
    
    path('', HomeView.as_view(), name='home'),
    path('new/', CreateAppointmentView, name='appointment_new'),
    path('edit/<int:pk>/', EditAppointmentView.as_view(), name='appointment_edit'),
    path('status_edit/<int:pk>/', EditStatusView.as_view(), name='status_edit'),
    # path('status_edit_full/<int:pk>/', EditStatusFullView.as_view(), name='status_edit_full'),
    path('delete/<int:pk>/', DeleteAppointmentView.as_view(), name='appointment_delete'),
    path('<int:pk>/', AppointmentDetail.as_view(), name='appointment_detail'),
    path('doctor-profile/', DoctorProfileView.as_view(), name='doctor_profile',),
    
    # full list of appointments path
    path('full-list/', AppFullListView.as_view(), name="app-full-list"),
    path('full-list/s', full_applist_search, name='full-list-search'),

    # search path
    path('dashboard/s', dashboard_search, name='dashboard_search'),
    path('dashboard/sw', dashboard_week_search, name='dashboard_week_search'),
    path('dashboard/snw', dashboard_next_search, name='dashboard_next_search'),
    path('dashboard/spw', dashboard_prev_search, name='dashboard_prev_search'),

    # path('new/s', form_search, name='form_search'),
    # path('showlist/',showlist,name='showlist'),
    
    
    # path("doctors/", DoctorsJsonList, name="doctors"),
    # path("list/", list_view, name="list"),
    # path("search/", list_search_view, name="search"),
    # path("register/", RegisterView.as_view(), name="register"),
]