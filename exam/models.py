from django.db import models

from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustUser, CourseDB


class TestResult(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    options = (
        ('Basic', 'Basic'),
        ('BasicHTML', 'BasicHTML'),
        ('BasicPHP', 'BasicPHP'),
        ('Intermediate', 'Intermediate'),
        ('IntermediateHTML', 'IntermediateHTML'),
        ('IntermediatePHP', 'IntermediatePHP'),
        ('Advanced', 'Advanced'),
        ('AdvancedHTML', 'AdvancedHTML'),
        ('AdvancedPHP', 'AdvancedPHP')
    )
    section = models.CharField(max_length=100, choices=options, default='Basic')
    score = models.IntegerField()
    course_id = models.ForeignKey(CourseDB, on_delete=models.CASCADE, null=True, blank=True)
    date_taken = models.DateTimeField(auto_now_add=True)
    is_active_fields = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Test Result for {self.section} section"


class CorrectAnswers(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    section = models.CharField(max_length=100)
    correct_answers = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Correct Answers for {self.section} section"
