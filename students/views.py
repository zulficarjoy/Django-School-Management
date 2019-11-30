from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from admin_tools.models import Department, Semester, SemesterCombination
from .models import Student
from .forms import StudentForm


@login_required
def add_student_view(request):
    """
    :param request:
    :return: admission form to
    logged in user.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            pk = form.instance.pk
            return redirect('students:student_details', pk=pk)
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'students/addstudent.html', context)


@login_required
def students_view(request):
    """
    :param request:
    :return: renders student list with all department
    and semesters list.
    """
    all_students = Student.objects.select_related(
        'department', 'semester', 'ac_session').all()
    departments = Department.objects.select_related(
        'head').all()
    semesters = SemesterCombination.objects.select_related(
        'department', 'semester', 'batch').all()
    context = {'students': all_students,
               'departments': departments,
               'semesters': semesters}
    return render(request, 'students/students_list.html', context)


@login_required
def students_by_department_view(request, pk):
    dept_name = Department.objects.get(pk=pk)
    students = Student.objects.select_related(
        'department', 'semester', 'ac_session').filter(department=dept_name)
    semesters = SemesterCombination.objects.select_related(
        'department', 'semester', 'batch').filter(
            department=dept_name)
    context = {'students': students,
               'semesters': semesters}
    return render(request, 'students/students_by_department.html', context)


# TODO: Improve students filtering by
# semester_number instead of semester obj.
@login_required
def students_by_semester(request, dept_pk, semester_n):
    dept = Department.objects.get(pk=dept_pk)
    sem = Semester.objects.get(number=semester_n)
    students = Student.objects.select_related(
        'department', 'semester', 'ac_session').filter(
            department=dept, semester=sem)
    # for sidepanel
    semesters = SemesterCombination.objects.select_related(
        'department', 'semester', 'batch').filter(
            department=dept)
    context = {'students': students,
               'dept': dept,
               'sem': sem,
               'semesters': semesters}
    return render(request, 'students/students_by_semester_of_dept.html', context)


class student_update_view(LoginRequiredMixin, UpdateView):
    """
    renders a student update form to update students details.
    """
    model = Student
    fields = '__all__'
    template_name = 'students/update_student.html'

    def get_success_url(self):
        student_id = self.kwargs['pk']
        return reverse_lazy('students:student_details', kwargs={'pk': student_id})


class student_detail_view(LoginRequiredMixin, DetailView):
    model = Student
    template_name = 'students/student_details.html'


@login_required
def student_delete_view(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('students:all_student')
