from django.http import HttpResponse
from .models import OfferedCourse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the Courses index.")


class CoursesByDepartment(APIView):
    def get(self, request, department_id, format=None):
        department_courses = OfferedCourse.objects.filter(course_id__department=department_id).select_related('course')
        serialized_dc = OfferedCourseSerializer(department_courses, many=True)
        return Response(serialized_dc.data)
