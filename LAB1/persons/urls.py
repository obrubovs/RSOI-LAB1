from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^api/v1/persons$', views.records, name='persons'),
    # path('create', views.create, name='create'),
    re_path(r'^api/v1/persons/([0-9]+)$', views.record_by_id, name='record'),
]
