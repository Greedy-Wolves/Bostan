from rest_framework import serializers

from .models import Course, OfferedCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class OfferedCourseSerializer(serializers.ModelSerializer):
    full_id = serializers.ReadOnlyField()
    course_name = serializers.ReadOnlyField(source='course.name')

    class Meta:
        model = OfferedCourse
        fields = ('full_id', 'course_name', 'instructor', 'times')

