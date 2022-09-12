from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    
    path('inside/', views.inside, name='inside')
]
