from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Student, StudentCourse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    # Get the courses associated with the logged-in instructor
    instructor_courses = Course.objects.filter(instructor=request.user)
    
    for course in instructor_courses:
        print(f'Course ID: {course.courseID}, Course Code: {course.code}, Course Title: {course.title}')
    
    context = {
        'instructor_courses': instructor_courses
    }
    return render(request, 'dashboard.html', context)

@login_required
def students(request, course_id):
    # Use courseID to get the correct course
    course = get_object_or_404(Course, courseID=course_id)
    # Filter StudentCourse objects by the correct course
    student_courses = StudentCourse.objects.filter(course=course)

    # Paginate the results
    paginator = Paginator(student_courses, 20)  # Show 50 students per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'course': course,
        'student_courses': page_obj
    }
    return render(request, 'students.html', context)


@login_required
def predict_performance(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    # Perform prediction logic here
    context = {
        'student': student,
        'prediction': 'Prediction result here'  # Placeholder
    }
    return render(request, 'predict_performance.html', context)