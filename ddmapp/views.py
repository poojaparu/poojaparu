from django.shortcuts import render

# Create your views here.
from .models import Department,Course
def department(request):
    courseid=request.GET.get('course',None)
    departmentid = request.GET.get('department', None)
    department=None
    if courseid:
        getcourse=Course.objects.get(id=courseid)
        department=Department.objects.filter(course=getcourse)
    if departmentid:
        getdepartment = Course.objects.get(id=departmentid)

    course=Course.objects.all()
    return render(request,'form.html',locals())

