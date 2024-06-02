from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('subjects', views.subjects, name='subjects'),
    path('informatic', views.informatic, name='informatic'),
    path('physic', views.physic, name='physic'),
    path('math', views.math, name='math')
]
