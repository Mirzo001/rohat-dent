from django.contrib import admin
from django.urls import path
from .views import DeleteInvoiceView, InvoiceListView, createInvoice, invoice_search, view_PDF

app_name = 'invoice'
urlpatterns = [
    path('invoice/', InvoiceListView.as_view(), name="invoice-list"),
    path('create/', createInvoice, name="invoice-create"),
    path('invoice-detail/<id>', view_PDF, name='invoice-detail'),
    path('invoice/s', invoice_search, name='invoice_search'),
    path('delete/invoice/<int:pk>/', DeleteInvoiceView.as_view(), name='invoice-delete'),
    # path('invoice-download/<id>', generate_PDF, name='invoice-download')
]
