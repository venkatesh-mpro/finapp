from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('summary/', views.summary),
    path('customers/', views.list_customer),
    path('add_customer/', views.add_customer),
    path('add_customer/submit/', views.save_customer)
]