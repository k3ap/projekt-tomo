from django.shortcuts import render, get_object_or_404, render_to_response
from attempts.models import Attempt
from .models import Course
from django.http import HttpResponse, JsonResponse
import json

def main_view(request):
    return render(request, 'tomo_statistics/statistika_test.html')

def test_view(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)             
    return render(request, 'tomo_statistics/statistika_course.html', course.statistika())

def graph(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    json_data = json.dumps(course.statistika()['solved_atleast'])
    return render(request, 'tomo_statistics/graf.html', {'json_data' : json_data})

def graph_json(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    response = JsonResponse(course.json_za_graf(), safe = False)
    return response
