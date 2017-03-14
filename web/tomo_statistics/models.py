from django.db import models
from courses.models import Course
import json


class Course(Course):
    class Meta:
        proxy = True

    def statistika(self):
        students = self.student_success()
        problem_sets = self.problem_sets.all().prefetch_related(
            'problems',
            'problems__parts',
            'problems__parts__attempts',
            'problems__parts__attempts__user',
        )

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

        my_students = [(value, student.last_name, student.first_name) for student, value in my_students.items()]
        my_students.sort()

        solved_atleast = [['Stevilo resenih', 'Število učencev, ki je rešilo toliko nalog']]
        solved = 0
        student_index = 0

        while solved <= number_of_problem_parts:
            while student_index < len(my_students) and my_students[student_index][0] < solved:
                student_index += 1
            solved_atleast.append((str(solved), len(my_students) - student_index))
            solved += 1

        return {
            'students' : students,
           'problem_sets' : problem_sets,
           'number_of_problems' : number_of_problems,
           'number_of_problem_parts' : number_of_problem_parts,
           'my_students' : my_students,
           'solved_atleast' : solved_atleast,
       }

    def problem_success(self):
        problem_sets = self.problem_sets.all().prefetch_related(
            'problems',
            'problems__parts',
            'problems__parts__attempts',
        )

        data = [['Pravilnost', 'Pravilne rešitve', 'Napačne rešitve']]
        pr_number = 0
        for problem_set in problem_sets:
            problems = problem_set.problems.all()
            for problem in problems:
                parts = problem.parts.all()
                correct = 0
                wrong = 0
                for part in parts:
                    #correct = 0
                    #wrong = 0
                    for attempt in part.attempts.all():
                        if attempt.valid:
                            correct += 1
                        else:
                            wrong += 1
                data.append([str(pr_number), correct, wrong])
                pr_number += 1
        return {
            'correct_submissions' : data }

        
        

    

