# binds the urls to the views for the various pages related routes
# route,views name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
