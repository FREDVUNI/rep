from django.urls import path
from . import views
urlpatterns = [
    path('enroll/',views.enroll,name='enroll'),
    path('index/',views.index,name='index'),
    path('services/',views.services,name='services'),
    path('events/',views.events,name='events'),
    path('contact/',views.contact,name='contact'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about')
]