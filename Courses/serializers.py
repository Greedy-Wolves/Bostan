from rest_framework import serializers
from .models import Course, OfferedCourse, ClassTime


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ClassTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassTime
        fields = '__all__'


class OfferedCourseSerializer(serializers.ModelSerializer):
    full_id = serializers.ReadOnlyField()
    course_name = serializers.ReadOnlyField(source='course.name')
    times = ClassTimeSerializer(many=True)

    class Meta:
        model = OfferedCourse
        fields = ('full_id', 'course_name', 'instructor', 'times')
