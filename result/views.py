from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Result
from students.models import Student
from admin_tools.models import Semester


@login_required
def student_result(request):
    if request.method == 'POST':
        roll = request.POST.get('roll')
        semester_n = request.POST.get('semester')
        student = Student.objects.get(roll=roll)
        semester = Semester.objects.get(number=semester_n)
        try:
            results = Result.objects.filter(student=student,
                                            semester=semester)
            print(
                '*'*200, results, student, semester
            )
        except:
            return HttpResponse("Result not found")
    else:
        return render(request, 'result/result.html')
    return render(request, 'result/result.html', {'results': results})
