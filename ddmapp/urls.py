from django.urls import path
from .import views

app_name='ddmapp'


urlpatterns = [

    path('',views.department,name='department'),


    ]
