import datetime
import json

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.models import User

# from models import School, Kitchen, Manager
from food.models import *


@require_POST
@csrf_exempt
def register_kitchen(request):
    name = request.POST.get('name', '')
    kitchen_type = request.POST.get('type', 'centralised')

    kitchen = Kitchen.objects.create(name=name, kitchen_type=kitchen_type)

    return HttpResponse(json.dumps({'message': 'Kitchen done',
                                    'kitchen_id': kitchen.id,
                        })
    )

@require_POST
@csrf_exempt
def register_school(request):
    name = request.POST.get('name', '')
    kitchen_id = request.POST.get('kitchen_id', 1)

    school = School.objects.create(name=name, kitchen_id=kitchen_id)
    return HttpResponse(json.dumps({'message': 'School Registration Successful',
                                    'school_id': school.id,
                        }))


@require_POST
@csrf_exempt
def register_teacher(request):
    username = request.POST.get('username', '')
    firstname = request.POST.get('firstname', '')
    lastname = request.POST.get('lastname', '')
    school_id = request.POST.get('school', 1)
    role = request.POST.get('role', 1)

    school = School.objects.get(id=school_id)

    user = User.objects.create(username=username, first_name=firstname, last_name=lastname)
    teacher = Teacher.objects.create(user_id=user.id, school_id=school.id,
                                     role=role)

    return HttpResponse(json.dumps({'message': 'Teacher Registration Successful'}))


@require_POST
@csrf_exempt
def register_manager(request):
    username = request.POST.get('username', '')
    firstname = request.POST.get('firstname', '')
    lastname = request.POST.get('lastname', '')
    kitchen_id = request.POST.get('kitchen', 1)
    role = request.POST.get('role', 1)

    kitchen = Kitchen.objects.get(id=kitchen_id)

    user = User.objects.create(username=username, first_name=firstname, last_name=lastname)
    manager = Manager.objects.create(user_id=user.id, kitchen_id=kitchen.id,
                                     role=role)

    return HttpResponse(json.dumps({'message': 'Manager Registration Successful'}))


@require_POST
@csrf_exempt
def update_attendance(request):
    teacher_id = request.POST.get('teacher_id', 1)
    attendance_count = request.POST.get('attendance_count', 0)
    teacher = Teacher.objects.get(teacher_id=teacher_id)

    try:
        school_attendance = Attendance.objects.get(school_id=teacher.school_id,
                                                   date=datetime.date.today)
    except Attendance.DoesNotExist:
        school_attendance = Attendance.objects.create(school_id=teacher.school_id)

    if teacher.role:
        school_attendance.secondary += attendance_count
    else:
        school_attendance.primary += attendance_count

    school_attendance.save()

