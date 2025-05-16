from django.urls import path
from . import views

urlpatterns = [
    path('people/', views.people, name = 'people'),
    path('python_first_app/', views.python_first_app, name = 'python_first_app'),
    path('patients/', views.patients, name = 'patients')
     
]