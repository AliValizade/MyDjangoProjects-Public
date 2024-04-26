from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list_view, name='notes_list'),
]
