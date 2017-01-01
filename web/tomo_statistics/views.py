from django.shortcuts import render, get_object_or_404
from courses.models import Course, ProblemSet

def main_view(request):
    return render(request, 'tomo_statistics/statistika_test.html')

def test_view(request, course_pk):
    course = get_object_or_404(Course, pk = course_pk)
    students = course.student_success()
    return render(request, 'tomo_statistics/statistika_course.html',
                  {'students' : students})
