from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('invoices', InvoiceListView.as_view(), name="invoices"),
    path('invoices/<int:id>', InvoiceView.as_view(), name="invoice"),
    path('invoices/new', csrf_exempt(NewInvoiceView.as_view()), name="new_invoice"),
    path('invoices/<int:invoiceId>/items', csrf_exempt(NewItemView.as_view()), name="new_item"),
    path('user/login', csrf_exempt(LoginView.as_view()), name="login"),
    path('user/signup', csrf_exempt(SignUpView.as_view()), name="signup"),
]