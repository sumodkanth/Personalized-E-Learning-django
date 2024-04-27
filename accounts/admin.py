from django.contrib import admin
from .models import CustUser,pdfnotes,Feedback,UploadedFile
from Faculty.models import Video,Comment,Like
# Register your models here.

admin.site.register(CustUser)
admin.site.register(pdfnotes)
admin.site.register(Feedback)
admin.site.register(UploadedFile)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Like)