from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('design', views.design),
    path('technologies', views.technologies),
    path('travel', views.travel),
]
