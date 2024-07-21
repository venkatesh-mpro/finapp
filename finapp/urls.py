from django.urls import path
from . import views

urlpatterns = [
    path('records/', views.say_hello)
]