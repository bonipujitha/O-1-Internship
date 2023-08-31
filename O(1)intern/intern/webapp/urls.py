from django.urls import path, include
from . import views

urlpatterns = [

    path('task/', views.task, name='task'),

]