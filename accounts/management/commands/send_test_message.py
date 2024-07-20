from django.core.management.base import BaseCommand
from accounts.tasks import send_test_message


class Command(BaseCommand):
    help = 'Send a test message to all students'

    def handle(self, *args, **kwargs):
        send_test_message.delay()
        self.stdout.write(self.style.SUCCESS('Test messages sent!'))
