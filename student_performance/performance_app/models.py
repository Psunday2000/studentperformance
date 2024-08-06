from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    studentID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    studyHours = models.IntegerField()
    punctuality = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=20, default='N/A')  # Adding a default value
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class StudentCourse(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year_one_semester_one_gpa = models.FloatField()
    year_one_semester_two_gpa = models.FloatField()
    year_two_semester_one_gpa = models.FloatField()

    def __str__(self):
        return f'{self.student.name} - {self.course.title}'
