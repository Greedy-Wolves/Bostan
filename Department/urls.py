from django.urls import path

from . import views

urlpatterns = [
    path('', views.Departments.as_view()),
]
