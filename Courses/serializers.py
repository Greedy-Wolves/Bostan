from rest_framework import serializers
from .models import Course, OfferedCourse, ClassTime


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ClassTimeSerializer(serializers.ModelSerializer):
    start = serializers.SerializerMethodField('std_start_time')
    end = serializers.SerializerMethodField('std_end_time')

    def std_start_time(self, obj):
        hour, minute, __ = str(obj.start_time).split(":")
        return int(hour) + int(minute)/60

    def std_end_time(self, obj):
        hour, minute, __ = str(obj.end_time).split(":")
        return int(hour) + int(minute)/60

    class Meta:
        model = ClassTime
        fields = ('day_of_week', 'start', 'end')


class OfferedCourseSerializer(serializers.ModelSerializer):
    full_id = serializers.ReadOnlyField()
    course_name = serializers.ReadOnlyField(source='course.name')
    times = ClassTimeSerializer(many=True)

    class Meta:
        model = OfferedCourse
        fields = ('full_id', 'course_name', 'instructor', 'times')
