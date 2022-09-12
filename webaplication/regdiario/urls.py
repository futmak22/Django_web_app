from django.urls import path
from regdiario import views

app_name = 'reg_diario'

urlpatterns = [
    path('', views.pacients_list, name='pacients_list'),
    path('phase/<int:pacient_id>/', views.phases_list, name='phases_list')
]
