from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary),
    path('customers/', views.list_customers),
    path('customer/', views.view_customer),
    path('add_customer/', views.add_customer),
    path('add_customer/submit/', views.save_customer)
]