from django.core.management.base import BaseCommand
from random import sample, uniform
from performance_app.models import Student, Course, StudentCourse

class Command(BaseCommand):
    help = 'Generate student course data'

    def handle(self, *args, **kwargs):
        students = Student.objects.all()
        courses = Course.objects.all()

        if courses.count() < 5:
            self.stdout.write(self.style.ERROR('Not enough courses in the database. Please ensure there are at least 5 courses.'))
            return

        for student in students:
            selected_courses = sample(list(courses), 5)
            for course in selected_courses:
                StudentCourse.objects.create(
                    student=student,
                    course=course,
                    year_one_semester_one_gpa=round(uniform(0, 4), 2),
                    year_one_semester_two_gpa=round(uniform(0, 4), 2),
                    year_two_semester_one_gpa=round(uniform(0, 4), 2)
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated student course data'))
