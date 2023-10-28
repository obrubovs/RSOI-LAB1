from django.urls import path
from . import views

urlpatterns = [
    path('', views.records, name='persons'),
    # path('create', views.create, name='create'),
    path('<int:pk>', views.record_by_id, name='record'),
]
