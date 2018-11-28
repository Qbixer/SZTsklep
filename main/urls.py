from django.urls import path

from . import views

appname = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('prices/',views.prices,name='priecs'),
    path('contact/', views.contact, name='contact'),
]