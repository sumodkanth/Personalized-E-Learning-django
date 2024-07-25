from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from .models import CustUser
# from django.conf import settings
from E_Learning import settings
from django.core.cache import cache


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
    return 'Daily Alert has send'


@shared_task(bind=True)
def send_test_message():
    threshold_time = timezone.now() - timedelta(days=1)
    # Fetch all students for testing
    students = CustUser.objects.filter(is_student=True, last_login__lt=threshold_time)
    print(students)
    for student in students:
        send_mail(
            'Friendly Reminder: Log in to Your E-learning Account',
                f"""Dear {student.username},

        We hope this message finds you well. We noticed that you haven't logged into your e-learning account recently. Keeping up with your learning is important, and we're here to support you every step of the way.

        Please take a moment to log in to your account and continue your learning journey with us. If you have any questions or need assistance, feel free to reach out to our support team.

        Best regards,
        Your E-learning Team

        ---
        This is an automated message. Please do not reply to this email."""
            .format(
                student.username),
            settings.EMAIL_HOST_USER,
            [student.email],
            fail_silently=False,
        )
    return 'Test messages sent!'


# LOCK_EXPIRE = 60 * 60  # Lock expires in 1 min
#
#
# @shared_task(bind=True)
# def send_test_message(self):
#     lock_id = 'send_test_message_lock'
#     acquire_lock = lambda: cache.add(lock_id, 'true', LOCK_EXPIRE)
#     release_lock = lambda: cache.delete(lock_id)
#
#     if acquire_lock():
#         try:
#             threshold_time = timezone.now() - timedelta(days=1)
#             students = CustUser.objects.filter(is_student=True, last_login__lt=threshold_time)
#             for student in students:
#                 send_mail(
#                     'Friendly Reminder: Log in to Your E-learning Account',
#                     f"""Dear {student.username},
#
# We hope this message finds you well. We noticed that you haven't logged into your e-learning account recently. Keeping up with your learning is important, and we're here to support you every step of the way.
#
# Please take a moment to log in to your account and continue your learning journey with us. If you have any questions or need assistance, feel free to reach out to our support team.
#
# Best regards,
# Your E-learning Team
#
# ---
# This is an automated message. Please do not reply to this email.""",
#                     settings.EMAIL_HOST_USER,
#                     [student.email],
#                     fail_silently=False,
#                 )
#             return 'Test messages sent!'
#         finally:
#             release_lock()
#     else:
#         print('Task already running')
