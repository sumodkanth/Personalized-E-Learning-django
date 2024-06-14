from django import forms
# from .models import Video


# class VideoForm(forms.ModelForm):
#     class Meta:
#         model = Video
#         fields = ['title', 'description', 'video_file']
class ReplyForm(forms.Form):
    text = forms.CharField(label='Reply', widget=forms.Textarea)
