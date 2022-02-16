from django.urls import path
from . import views

urlpatterns = [
    path('', views.csv_to_database),
    path('main_window', views.main_window, name='main_window'),
]