from django.shortcuts import render, get_object_or_404, render_to_response
from attempts.models import Attempt
from .models import Course
from django.http import HttpResponse, JsonResponse
import json

def course_graphs(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    return render(request, 'tomo_statistics/statistika_course.html', {
        'annotated_problem_sets' : course.problem_success(),
        'course' : course,
    })

def user_success(request, course_pk):
    course = get_object_or_404(Course, pk=course_pk)
    json_data = json.dumps(course.statistika()['solved_atleast'])
    return render(request, 'tomo_statistics/user_success.html', {'json_data' : json_data})
