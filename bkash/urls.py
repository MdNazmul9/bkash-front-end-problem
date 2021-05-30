"""
Author: Raju Ahmed Shetu
"""
from django.urls import path
from . import views
app_name='bkash'
urlpatterns = [
    path('payment/create', views.PaymentCreateApiView.as_view(), name='payment_create_api_view'),
    path('payment/execute', views.PaymentExecuteApiView.as_view(), name='payment_execute_api_view'),
]

# 127.0.0.1:8000/bkash/payment/create
# 127.0.0.1:8000/bkash/payment/execute

