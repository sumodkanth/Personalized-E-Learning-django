from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReplyForm
# from .forms import VideoForm
from .models import Video, Comment, Like
from accounts.models import UploadedFile

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
        video = Video(title=title, description=description, video_file=video_file, faculty=user, course=course)
        video.save()

        return redirect(viewvideos)  # Redirect to a success page after saving the video
    else:

        return render(request, 'add_video.html')  # Render the form page for GET requests


def viewvideos(request):
    user = request.user

    # Retrieve all videos for the faculty user from the database, ordered by the most recent
    videos = Video.objects.filter(faculty=user, course=user.Course).order_by('-uploaded_at')

    # Pass the videos to the template for rendering
    return render(request, 'viewvideos.html', {'videos': videos})


def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.delete()
    return redirect(viewvideos)


def comments(request):
    user = request.user
    videos = Video.objects.filter(faculty=user, course=user.Course)
    return render(request, 'comments.html', {'videos': videos})


def video_comments(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    print(video)
    comments = video.comments.all()  # Retrieve all comments for the video

    if request.method == 'POST':
        if request.user.is_authenticated:  # Ensure user is authenticated
            comment_text = request.POST.get('comment_text')
            print(comment_text)
            if comment_text:  # Ensure comment text is not empty
                Comment.objects.create(video=video, user=request.user, text=comment_text)

    return redirect('comments')


def view_projects(request):
    user = request.user
    projects = UploadedFile.objects.filter(project_language=user.Course)
    return render(request, 'viewprojects.html',{'projects': projects})


def review_project(request, project_id):
    project = UploadedFile.objects.get(pk=project_id)

    if request.method == 'POST':
        score = request.POST.get('score')
        project.score = score
        project.save()
        return redirect('view_projects')

    return render(request, 'review_project.html', {'project': project})