from django.shortcuts import render, get_object_or_404
from attempts.models import Attempt
from .models import Course
from django.http import HttpResponse, JsonResponse

def main_view(request):
    return render(request, 'tomo_statistics/statistika_test.html')

def test_view(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)             
    return render(request, 'tomo_statistics/statistika_course.html', course.statistika())

def graph(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    response = JsonResponse(course.json_za_graf())
    return render(request, 'tomo_statistics/graf.html', course.json_za_graf())
    #return response

def graph_json(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    response = JsonResponse(course.json_za_graf(), safe = False)
    return response
