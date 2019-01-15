from . import views
from django.urls import path

urlpatterns = [
    path(r'abc/', views.abc, name='abc'), ]
