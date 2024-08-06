from django.core.management.base import BaseCommand
from random import choice, randint
from performance_app.models import Student

class Command(BaseCommand):
    help = 'Generate 500 students with Nigerian names'

    def handle(self, *args, **kwargs):
        names = [
            'Abdullahi', 'Abimbola', 'Abiola', 'Abubakar', 'Adebayo', 'Adeoye', 'Adesina',
            'Adeyemi', 'Akinyemi', 'Amaechi', 'Babangida', 'Balogun', 'Bankole', 'Bassey',
            'Bello', 'Bolaji', 'Chukwu', 'Danjuma', 'Eze', 'Gbadamosi', 'Hassan', 'Ibeh',
            'Igwe', 'Kalu', 'Lawal', 'Mohammed', 'Njoku', 'Nwadike', 'Obi', 'Okeke', 'Okoro',
            'Okpara', 'Oni', 'Taiwo', 'Tyjani', 'Unigwe', 'Zabu'
        ]

        for _ in range(500):
            first_name = choice(names)
            last_name = choice(names)
            full_name = f"{first_name} {last_name}"
            
            Student.objects.create(
                name=full_name,
                studyHours=randint(2, 10),
                punctuality=randint(25, 100)
            )

        self.stdout.write(self.style.SUCCESS('Successfully generated 500 students with Nigerian names'))
