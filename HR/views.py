from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Placement,JobApplication
from .forms import PlacementForm
from django.core.files.storage import FileSystemStorage


# Create your views here.
def HR_index(request):
    return render(request, 'hrindex.html')


def add_placement(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        location = request.POST.get('location')
        qualification = request.POST.get('qualification')
        skills = request.POST.get('skills')
        image_icon = request.FILES.get('image_icon')

        if company_name and job_title and job_description and location and qualification:
            Placement.objects.create(
                company_name=company_name,
                job_title=job_title,
                job_description=job_description,
                location=location,
                qualification=qualification,
                skills=skills,
                image_icon=image_icon
            )
            return redirect('HRindex')  # Assuming 'home' is the name of your homepage URL

    return render(request, 'add_placement.html')


def placement_list(request):
    placements = Placement.objects.all()
    return render(request, 'placement_list.html', {'placements': placements})


def edit_placement(request, placement_id):
    placement = get_object_or_404(Placement, id=placement_id)

    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        job_title = request.POST.get('job_title')
        job_description = request.POST.get('job_description')
        location = request.POST.get('location')
        qualification = request.POST.get('qualification')
        skills = request.POST.get('skills')

        image_icon = request.FILES.get('image_icon')
        if image_icon:
            fs = FileSystemStorage(location='placement_icons/')
            filename = fs.save(image_icon.name, image_icon)
            uploaded_file_url = fs.url(filename)
        else:
            uploaded_file_url = ''

        placement.company_name = company_name
        placement.job_title = job_title
        placement.job_description = job_description
        placement.location = location
        placement.qualification = qualification
        placement.skills = skills
        placement.image_icon = uploaded_file_url if uploaded_file_url else placement.image_icon

        placement.save()
        return redirect('placement_list')

    return render(request, 'edit_placement.html', {'placement': placement})


def delete_placement(request, placement_id):
    placement = get_object_or_404(Placement, id=placement_id)
    if request.method == 'POST':
        placement.delete()
        return redirect('placement_list')
    return redirect('placement_list')


def applications_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'dashboard.html', {'applications': applications})
