from django.urls import path
from . import views

urlpatterns = [
    path('' , views.crop , name = 'crop'),
    path('crop-results' , views.crop_results , name = 'crop_results'),
]

