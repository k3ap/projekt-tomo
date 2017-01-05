from django.shortcuts import render, get_object_or_404
from attempts.models import Attempt
from .models import Course

def main_view(request):
    return render(request, 'tomo_statistics/statistika_test.html')

def test_view(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)             
    return render(request, 'tomo_statistics/statistika_course.html', course.statistika())
