from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index_react.as_view(),name='index')
    
]