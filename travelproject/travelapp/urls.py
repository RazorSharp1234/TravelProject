from django.urls import path
from .import views

urlpatterns = [
    path('', views.demo, name='demo'),
    #path('opp/', views.Mathematical_Operations, name='Mathematical_Operations'),
    #path('about/', views.about, name='about'),
    #path('contact/',views.contact, name ='contact')
]
