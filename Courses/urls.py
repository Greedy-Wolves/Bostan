from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<int:department_id>/', views.CoursesByDepartment.as_view()),
]
