from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.records, name='persons'),
    # path('create', views.create, name='create'),
    re_path('^/([0-9]+)$', views.record_by_id, name='record'),
]
