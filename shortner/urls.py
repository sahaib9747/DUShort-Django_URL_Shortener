from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shortner', views.short, name='short'),
    path('<str:link>', views.go, name='go'),
]