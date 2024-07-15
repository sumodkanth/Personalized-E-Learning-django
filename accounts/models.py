from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from datetime import timedelta


class CustUser(AbstractUser):
    phone = models.IntegerField(null=True)
    options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    COURSE_CHOICES = [
        ('Python', 'Python'),
        ('HTML', 'HTML'),
        ('PHP', 'PHP'),  # SELECTING COURSE
    ]
    gender = models.CharField(max_length=100, choices=options, null=True, default='Male')
    age = models.IntegerField(null=True)
    Course = models.CharField(max_length=10, choices=COURSE_CHOICES, null=True, blank=True)
    is_student = models.BooleanField(null=True, blank=True, default=False)
    is_faculty = models.BooleanField(null=True, blank=True, default=False)
    is_hr = models.BooleanField(null=True, blank=True, default=False)
    is_active_basic = models.BooleanField(default=False, null=True, blank=True)
    is_active_inter = models.BooleanField(default=False, null=True, blank=True)
    is_active_adv = models.BooleanField(default=False, null=True, blank=True)
    is_active_coding = models.BooleanField(default=False, null=True, blank=True)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CourseDB(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)  # Duration in weeks
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    fee = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.course_name


class CourseRegistration(models.Model):
    course_id = models.ForeignKey(CourseDB, related_name='registrations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.start_date and not self.end_date:
            duration_weeks = int(self.course.duration.split()[0])
            self.end_date = self.start_date + timedelta(weeks=duration_weeks)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.course_id} {self.name}'


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_language = models.CharField(max_length=50)
    git_link = models.URLField()
    project_description = models.TextField()
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.project_name


class Payment(models.Model):
    card_type = models.CharField(max_length=50)
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=7)
    cvv = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    course = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.cardholder_name} {self.course}"


class Placement(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    date_posted = models.DateField(auto_now_add=True)
    image_icon = models.ImageField(upload_to='placement_icons/', blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.job_title


class JobApplication(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    job = models.ForeignKey(Placement, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    resume = models.FileField(upload_to='resumes/')
    date_applied = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.job}"
