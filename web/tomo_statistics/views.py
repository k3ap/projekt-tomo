from django.shortcuts import render, get_object_or_404
from courses.models import Course, ProblemSet
from attempts.models import Attempt

def main_view(request):
    return render(request, 'tomo_statistics/statistika_test.html')

def test_view(request, course_pk):
    course = get_object_or_404(Course, pk = course_pk)
    students = course.student_success()
    problem_sets = course.problem_sets.all()

    my_students = {student : 0 for student in students}

    number_of_problems = 0
    number_of_problem_parts = 0
    for problem_set in problem_sets:
        problems = problem_set.problems.all()
        number_of_problems += len(problems)
        for problem in problems:
            parts = problem.parts.all()
            number_of_problem_parts += len(parts)
            for part in parts:
                for attempt in part.attempts.all():
                    if attempt.user in my_students:
                        if attempt.valid:
                            my_students[attempt.user] += 1

    my_students = [(student.last_name, student.first_name, value) for student, value in my_students.items()]
            
    return render(request, 'tomo_statistics/statistika_course.html',
                  {'students' : students,
                   'problem_set' : problem_set,
                   'number_of_problems' : number_of_problems,
                   'number_of_problem_parts' : number_of_problem_parts,
                   'my_students' : my_students,
                   })

