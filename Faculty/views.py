from django.shortcuts import render, redirect,get_object_or_404

# from .forms import VideoForm
from .models import Video


# Create your views here.
def facultyindex(request):
    user = request.user
    print(user)
    return render(request, 'facultyindex.html', {'user': user})


def index(request):
    # if request.method == 'POST':
    #     form = VideoForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         video = form.save(commit=False)
    #         video.uploaded_by = request.user
    #         video.save()
    #         return redirect('index')
    # else:
    #     form = VideoForm()
    return render(request, 'videoupload.html')


def add_video(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        video_file = request.FILES.get('video_file')
        course = request.POST.get('course')

        # Create a new Video object and save it to the database
        video = Video(title=title, description=description, video_file=video_file,faculty=user,course=course)
        video.save()

        return redirect(viewvideos)  # Redirect to a success page after saving the video
    else:
        return render(request, 'add_video.html')  # Render the form page for GET requests


def viewvideos(request):
    user = request.user

    # Retrieve all videos for the faculty user from the database, ordered by the most recent
    videos = Video.objects.filter(faculty=user).order_by('-uploaded_at')

    # Pass the videos to the template for rendering
    return render(request, 'viewvideos.html', {'videos': videos})


def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return redirect(viewvideos)