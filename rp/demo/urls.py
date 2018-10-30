from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recognise/', views.pill_recognise, name='pill_recognise'),
]
