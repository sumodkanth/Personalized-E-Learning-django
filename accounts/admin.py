from django.contrib import admin
from .models import CustUser, Feedback, UploadedFile, CourseDB, CourseRegistration, Placement,JobApplication
from Faculty.models import Video, Comment, Like

# Register your models here.

admin.site.register(CustUser)
admin.site.register(Feedback)
admin.site.register(UploadedFile)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(CourseDB)
admin.site.register(CourseRegistration)
admin.site.register(Placement)
admin.site.register(JobApplication)
