from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.records, name='persons'),
    # path('create', views.create, name='create'),
    re_path(r'^([0-9]+)$', views.record_by_id, name='record'),
]
