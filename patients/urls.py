
from django.urls import path




from .views import patient_list_view, EditPatientView, PatientDeleteView, PatientDetailView, PatientListView, CreatePatientView, autosuggest, patient_search

appname = "patients"

urlpatterns = [
    path('patients/', PatientListView.as_view(), name='patients'),
    path('patients/new/', CreatePatientView.as_view(), name='patients_new'),
    path("autosuggest/", autosuggest, name="p_autosuggest"),
    path('patients/edit/<int:pk>/', EditPatientView.as_view(), name='patients_edit'),
    path('patients/delete/<int:pk>/', PatientDeleteView.as_view(), name='patients_delete'),

    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patients_detail'),
    
    # patient search path
    # path('createbill/', CreateBillView, name='createbill'),
    # path('bills/', BillListView.as_view(), name="bill-list"),

    path('patients/s', patient_search, name='patient_search'),
    path('ajax/users', patient_list_view, name='json_user_list')
]
