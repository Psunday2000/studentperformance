# data_export/management/commands/export_data.py
import csv
from django.core.management.base import BaseCommand
from performance_app.models import StudentCourse

class Command(BaseCommand):
    help = 'Export student course data to CSV with predicted performance'

    def handle(self, *args, **kwargs):
        # Fetch data from StudentCourse and related Student model
        data = StudentCourse.objects.select_related('student').all().values(
            'student__studyHours', 'student__punctuality',
            'year_one_semester_one_gpa', 'year_one_semester_two_gpa',
            'year_two_semester_one_gpa'
        )

        # Prepare the data for CSV export
        data_list = list(data)
        
        # Define CSV file path
        csv_file_path = 'student_performance_data_with_predictions.csv'

        # Write data to CSV
        with open(csv_file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow([
                'Study Hours', 'Punctuality', 
                'Year 1 Semester 1 GPA', 'Year 1 Semester 2 GPA', 
                'Year 2 Semester 1 GPA', 'Predicted Performance'
            ])
            # Write data
            for row in data_list:
                # Calculate average GPA
                gpas = [
                    row['year_one_semester_one_gpa'],
                    row['year_one_semester_two_gpa'],
                    row['year_two_semester_one_gpa']
                ]
                gpas = [gpa for gpa in gpas if gpa is not None]
                if gpas:
                    average_gpa = sum(gpas) / len(gpas)
                else:
                    average_gpa = 0

                # Determine predicted performance
                predicted_performance = self.predict_performance(
                    row['student__studyHours'],
                    row['student__punctuality'],
                    average_gpa
                )

                writer.writerow([
                    row['student__studyHours'], 
                    row['student__punctuality'],
                    row['year_one_semester_one_gpa'],
                    row['year_one_semester_two_gpa'],
                    row['year_two_semester_one_gpa'],
                    predicted_performance
                ])

        self.stdout.write(self.style.SUCCESS('Data exported successfully to %s' % csv_file_path))

    def predict_performance(self, study_hours, punctuality, average_gpa):
        # Define performance thresholds
        if study_hours >= 5 and punctuality >= 50:
            if average_gpa < 2.0:
                return 'Lower Credit'
            elif average_gpa < 3.0:
                return 'Upper Credit'
            else:
                return 'Distinction'
        else:
            if average_gpa < 2.0:
                return 'Lower Credit'
            elif average_gpa < 3.0:
                return 'Upper Credit'
            else:
                return 'Distinction'
