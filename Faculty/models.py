from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import CourseDB


class Video(models.Model):
    title = models.CharField(max_length=100)
    course = models.CharField(max_length=100, null=True, blank=True)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(default='')
    faculty = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}on {self.video.title}"


class Like(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class WatchHistory(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
    course_id = models.ForeignKey(CourseDB, on_delete=models.CASCADE, null=True, blank=True)
    watched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}{self.course_id}"
