from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.forms import forms

from .models import Course, OfferedCourse, ClassTime

# Register your models here.

admin.site.register(Course)


class CourseImportForm(forms.Form):
    course_file = forms.FileField()


@admin.register(OfferedCourse)
class OfferedCourseAdmin(admin.ModelAdmin):
    change_list_template = "entities/heroes_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-course/', self.import_course_list),
        ]
        return my_urls + urls

    def import_course_list(self, request):
        if request.method == "POST":
            import GolestanParser.Course
            course_file = request.FILES["course_file"]
            for dc in GolestanParser.Course.parse_page(course_file):
                try:
                    splited_course_code = dc.code.split('-')

                    course, __ = Course.objects.get_or_create(id=splited_course_code[0],
                                                              department=splited_course_code[0][:2],
                                                              name=dc.name,
                                                              unit_count=int(dc.unit_count)
                                                              )
                    offered_course = OfferedCourse.objects.create(course=course,
                                                                  semester='962',
                                                                  group=int(splited_course_code[1]),
                                                                  instructor=dc.instructor,
                                                                  gender_spec=dc.gender
                                                                  )
                    for day_time in dc.days_times:
                        # todo use get_or_create
                        time = ClassTime.objects.create(day_of_week=day_time[0],
                                                        start_time=day_time[1],
                                                        end_time=day_time[2]
                                                        )
                        offered_course.times.add(time)
                    offered_course.save()
                except Exception as e:
                    print("Error in:", dc.code)
                    raise e

            self.message_user(request, "Your course file has been imported")
            return redirect("..")
        form = CourseImportForm()
        payload = {"form": form}
        return render(
            request, "admin/import_course_form.html", payload
        )
