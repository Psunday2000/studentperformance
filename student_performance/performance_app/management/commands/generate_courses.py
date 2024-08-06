from django.core.management.base import BaseCommand
from faker import Faker
from performance_app.models import Course
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Generate 10 courses, 2 per instructor'

    def handle(self, *args, **kwargs):
        fake = Faker()

        instructors = User.objects.filter(id__in=[2, 3, 4, 5, 6])
        course_titles = [
            'Introduction to Computer', 'Introduction to Programming', 'Data Structures and Algorithm', 'Introduction to Software Engineering', 'Data Modelling and UMLs',
            'Artificial Intelligence and Machine Learning', 'Expert Systems and Robotics', 'Database Management Systems', 'Data Analysis and Predictive Analysis', 'Introduction to Python'
        ]

        for i, instructor in enumerate(instructors):
            for j in range(2):  # 2 courses per instructor
                Course.objects.create(
                    courseID=fake.unique.random_int(min=1, max=100),
                    title=course_titles[i*2 + j],
                    code=fake.unique.bothify(text='???-###'),
                    instructor=instructor
                )

        self.stdout.write(self.style.SUCCESS('Successfully generated 10 courses, 2 per instructor'))
