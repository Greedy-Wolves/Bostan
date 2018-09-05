from django.db import models

# Create your models here.


class Course(models.Model):
    id = models.DecimalField(max_digits=7, decimal_places=0, primary_key=True)
    department = models.DecimalField(max_digits=2, decimal_places=0)
    name = models.CharField(max_length=50)
    unit_count = models.SmallIntegerField()


class ClassTime(models.Model):
    day_of_week = models.SmallIntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()


class OfferedCourse(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    semester = models.DecimalField(max_digits=3, decimal_places=0)
    group = models.DecimalField(max_digits=2, decimal_places=0)
    instructor = models.CharField(max_length=50)
    times = models.ManyToManyField(ClassTime)
    location = models.CharField(max_length=50, null=True)
    gender_spec = models.NullBooleanField()
    description = models.CharField(max_length=100, null=True)

    @property
    def full_id(self):
        return "{!s}-{!s:0>2}".format(self.course.id, self.group)
