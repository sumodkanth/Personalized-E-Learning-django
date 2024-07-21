from django.contrib import admin
from .models import CustUser, Feedback, UploadedFile, CourseDB, CourseRegistration, Placement,JobApplication,Payment
from Faculty.models import Video, Comment,WatchHistory

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
admin.site.register(Payment)

