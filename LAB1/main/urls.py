from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),  # method 'index' call from views file when user is on the main page
    path('about', views.about, name='about')
]
