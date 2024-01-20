from django.urls import path 

from . import views

urlpatterns = [
        path("", views.DataCollector.as_view(), name='index')
        ]


