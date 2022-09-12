from argparse import Namespace
from django.urls import path
from . import views

app_name = 'drag_drop'

urlpatterns = [
    path('', views.upload_file , name='drag_drop_screen')
]
