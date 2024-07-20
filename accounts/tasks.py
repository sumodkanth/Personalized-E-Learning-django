from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import CustUser
from django.conf import settings

@shared_task
def send_login_reminder():
    # Define the time threshold for login reminders
    threshold_time = timezone.now() - timedelta(days=1)

    # Fetch students who have not logged in since the threshold time
    students = CustUser.objects.filter(is_student=True, last_login__lt=threshold_time)
    print(students)
    for student in students:
        send_mail(
            'Reminder to Log In',
            'Dear {},\n\nThis is a reminder to log in to your e-learning account.\n\nBest regards,\nYour E-learning Team'.format(
                student.username),
            settings.EMAIL_HOST_USER,
            [student.email],
            fail_silently=False,
        )


@shared_task
def send_test_message():
    # Fetch all students for testing
    students = CustUser.objects.filter(is_student=True)
    print(students)
    for student in students:
        send_mail(
            'Test Message',
            'Hello {},\n\nThis is a test message from your e-learning system.'.format(student.username),
            settings.EMAIL_HOST_USER,
            [student.email],
            fail_silently=False,
        )
    return 'Test messages sent!'