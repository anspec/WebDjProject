from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='page_home'),
    path('new', views.new, name='page_new'),
]
