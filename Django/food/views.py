import datetime
import json

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User

# from models import School, Kitchen, Manager
from models import *



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
    attendance_count = int(request.POST.get('attendance_count', 0))
    teacher = Teacher.objects.get(id=teacher_id)

    try:
        school_attendance = Attendance.objects.get(school_id=teacher.school_id,
                                                   date=timezone.now().date())
    except Attendance.DoesNotExist:
        school_attendance = Attendance.objects.create(school_id=teacher.school_id,
                                                      date=timezone.now().date())

    if teacher.role:
        school_attendance.secondary = school_attendance.secondary + attendance_count
    else:
        school_attendance.primary += school_attendance.primary + attendance_count

    school_attendance.save()
    return HttpResponse(json.dumps({'message': 'Attendance Updation Successful'}))


@require_POST
@csrf_exempt
def add_comment(request):
    teacher_id = request.POST.get('teacher_id', 1)
    comment = request.POST.get('comment', '')
    teacher = Teacher.objects.get(id=teacher_id)
    comment_for_school = Comments.objects.create(school_id=teacher.school_id,
                                                 comment=comment)

    return HttpResponse(json.dumps({
                                'message': 'Comment Added',
                                'comment_id': comment_for_school.id,
                        })
    )


@csrf_exempt
@require_POST
def get_comments(request):
    manager_id = request.POST.get('manager_id', '')
    kitchen_id = Manager.objects.get(id=manager_id).kitchen_id

    schools = School.objects.filter(kitchen_id=kitchen_id)

    comments = []

    for school in schools:
        comment = {}
        comment['school'] = school.name
        comment['messages'] = Comments.objects.filter(school_id=school.id,
                                                      created=timezone.now().date()).values_list('comment',
                                                                                            flat=True)
        print len(comment['messages'])
        comments.append(comment)

    return HttpResponse(json.dumps(comments))


@require_POST
@csrf_exempt
def add_feedback(request):
    teacher_id = request.POST.get('teacher_id', 1)
    feedback = request.POST.get('feedback', '')
    teacher = Teacher.objects.get(id=teacher_id)
    feedback_for_school = Feedback.objects.create(school_id=teacher.school_id,
                                                 feedback=feedback)

    return HttpResponse(json.dumps({
                                'message': 'Comment Added',
                                'feedback_id': feedback_for_school.id,
                        })
    )


@csrf_exempt
@require_POST
def get_feedback(request):
    manager_id = request.POST.get('manager_id', '')
    kitchen_id = Manager.objects.get(id=manager_id).kitchen_id

    schools = School.objects.filter(kitchen_id=kitchen_id)

    comments = []

    for school in schools:
        comment = {}
        comment['school'] = school.name
        comment['messages'] = Feedback.objects.filter(school_id=school.id,
                                                      created=timezone.now().date()).values_list('feedback',
                                                                                            flat=True)
        print len(comment['messages'])
        comments.append(comment)

    return HttpResponse(json.dumps(comments))


@require_POST
@csrf_exempt
def add_units(request):
    teacher_id = request.POST.get('teacher_id', 1)

    teacher = Teacher.objects.get(id=teacher_id)
    school_id = teacher.school_id

    data = request.POST.get('data', '')
    data = json.loads(data)

    for key, value in data.iteritems():
        consumption = SchoolConsumption.objects.create(school_id=school_id,
                                                       item_id=key)
        consumption.unit_consumed = value['consumed']
        consumption.unit_left = value['left']

        consumption.save()

    return HttpResponse(json.dumps({
                                'message': 'Units updated',
                    })
    )


@require_POST
def last_seven_days(request):
    manager_id = request.POST.get('manager_id', 1)
    kitchen_id = Manager.objects.get(id=manager_id).kitchen_id

    schools = School.objects.filter(kitchen_id=kitchen_id)

    for school in schools:
        school_attendance = Attendance.objects.filter(school_id=school.id,
                                                      date__range=[
                                                          str(datetime.date.today() - datetime.timedelta(days=7)),
                                                          str(datetime.date.today())
                                                      ])

        school_consumption = SchoolConsumption.objects.filter(school_id=school.id,
                                                              date__range=[
                                                                  str(datetime.date.today() - datetime.timedelta(
                                                                      days=7
                                                                  )),
                                                                  str(datetime.date.today())
                                                              ])

        expected_attendance = ExpectedAttendance.objects.filter(school_id=school.id,
                                                                date__range=[
                                                                    str(datetime.date.today() - datetime.timedelta(
                                                                        days=7
                                                                    )),
                                                                    str(datetime.date.today())
                                                                ])

        expected_consumption = ExpectedConsumption.objects.filter(school_id=school.id,
                                                                  date__range=[
                                                                      str(datetime.date.today() - datetime.timedelta(
                                                                          days=7
                                                                      )),
                                                                      str(datetime.date.today())
                                                                  ])
        result_data = []

        vals_past = zip(school_attendance, school_consumption)
        vals_expected = zip(expected_attendance, expected_consumption)

        for data in vals_past:
            result_data.append([data[0].primary, data[0].consumption])

        for data in vals_expected:
            result_data.append([data[0].primary, data[0].consumption])

    return HttpResponse(json.dumps({'Rice': result_data}))
