from typing import Any

from django.db.models import Sum
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView, UpdateView, View
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from exam.models import *
from exam2.models import *
from exam3.models import *
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import FeedbackForm, ProjectUploadForm


# Create your views here.


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    def post(self, request, *args, **kwargs):
        log_form = LoginForm(data=request.POST)
        if log_form.is_valid():
            un = log_form.cleaned_data.get('username')
            ps = log_form.cleaned_data.get('password')
            user = authenticate(request, username=un, password=ps)
            if user:
                if user.is_student == True:
                    login(request, user)
                    return redirect('h')
                if user.is_faculty == True:
                    login(request, user)
                    return redirect('comments')
            else:
                return render(request, 'login.html', {"form": log_form, 'error': "Invalid credentials"})
        return render(request, 'login.html', {"form": log_form})


# class HomeView(TemplateView):
#     template_name = 'home.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = TestResult.objects.filter(user=self.request.user)
#         return context


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['data'] = TestResult.objects.filter(user=user)
        # Fetch the project languages associated with the user's uploaded files
        uploaded_files = user.uploadedfile_set.all()  # Assuming UploadedFile is related to the user model
        project_languages = set(uploaded_files.values_list('project_language', flat=True))
        context['project_languages'] = project_languages
        return context


class RegView(CreateView):
    template_name = 'reg.html'
    model = CustUser
    form_class = RegForm
    success_url = reverse_lazy('log')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['val'] = self.kwargs.get('val')
        return context

    def form_valid(self, form):
        val = self.kwargs.get('val')

        if val == 'student':
            form.instance.is_student = True
        if val == 'faculty':
            form.instance.is_faculty = True
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class Profile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   id=kwargs.get('pk')
        context['data'] = CustUser.objects.get(id=self.request.user.id)
        return context


class ProfileUpdateView(UpdateView):
    template_name = "profileupdate.html"
    model = CustUser
    form_class = StudentFormProfile
    success_url = reverse_lazy('pro')


class ChangePasswordView(FormView):
    template_name = "changeps.html"
    form_class = ChangePasswordForm

    def post(self, request, *args, **kwargs):
        form_data = ChangePasswordForm(data=request.POST)
        if form_data.is_valid():
            current = form_data.cleaned_data.get("current_password")
            new = form_data.cleaned_data.get("new_password")
            confirm = form_data.cleaned_data.get("confirm_password")
            user = authenticate(request, username=request.user.username, password=current)
            if user:
                if new == confirm:
                    user.set_password(new)
                    user.save()
                    logout(request)
                    return redirect("log")
                else:
                    return redirect("cp")
            else:
                return redirect("cp")
        else:
            return render(request, "changepassword.html", {"form": form_data})


class LogOut(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        return redirect("log")


class ScoreTable(TemplateView):
    template_name = 'score_table.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   id=kwargs.get('pk')
        context['data'] = CustUser.objects.get(id=self.request.user.id)
        context['score'] = TestResult.objects.filter(user=self.request.user)
        return context


class ProgressCard(TemplateView):
    template_name = 'progress.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #   id=kwargs.get('pk')
        context['data'] = CustUser.objects.get(id=self.request.user.id)
        context['score'] = TestResult.objects.filter(user=self.request.user)

        return context


@login_required
def send_certificate_email(request):
    user = request.user

    # Render HTML content
    html_content = render_to_string('score_table.html', {'data': user, 'score': user.scores})

    # Attach the certificate to the email
    email = EmailMessage(
        'Your Certificate',
        'Congratulations! You have successfully generated your certificate.',
        'sumodkanthcs@gmail.com',  # Replace with your email address
        [user.email],  # Send to the authenticated user's email address\
        html_message=html_content,
        fail_silently=False,
    )

    # Attach the certificate to the email

    # Send the email
    email.send()
    return HttpResponse('Email sent successfully.')


def htmlcertificate(request):
    return render(request, 'htmlcertificate.html')


def pythoncertificate(request):
    return render(request, 'pythoncertificate.html')


def phpcertificate(request):
    return render(request, 'phpcertificate.html')


# html section
@login_required
def generate_certificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/htmlcertificate.png'  # Replace with the path to your font file

    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={user.username}_certificate.png'

    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 60
    font_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (780, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # Retrieve the latest project associated with the user
    latest_project = UploadedFile.objects.filter(student=user, project_language='html').latest('id')

    # Convert project name to uppercase
    uppercase_project_name = latest_project.project_name.upper()

    # Overlay the latest project name onto the certificate
    project_name_position = (780, 970)  # Adjust the position as needed
    draw.text(project_name_position, uppercase_project_name, fill="black", font=font)

    # You can add more overlay text or images as needed
    #     # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    # Send the image as response
    response.write(img_byte_array.getvalue())
    return response


@login_required
def send_certificate_email(request):
    # Your existing code for sending the certificate via email
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/htmlcertificate.png'  # Replace with the path to your font file

    # Open the existing certificate image using Pillow
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 60
    font_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (780, 680)  # Adjust the position as needed
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # Retrieve the latest project associated with the user
    latest_project = UploadedFile.objects.filter(student=user, project_language='html').latest('id')

    # Convert project name to uppercase
    uppercase_project_name = latest_project.project_name.upper()

    # Overlay the latest project name onto the certificate
    project_name_position = (780, 970)  # Adjust the position as needed
    draw.text(project_name_position, uppercase_project_name, fill="black", font=font)

    # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Attach the certificate to the email
    email = EmailMessage(
        'Your Certificate',
        'Congratulations! You have successfully generated your certificate.',
        'sumodkanthcs@gmail.com',  # Replace with your email address
        [user.email],  # Send to the authenticated user's email address
    )
    # Attach the certificate to the email
    email.attach('certificate.png', img_byte_array.getvalue(), 'image/png')
    # Add a success message

    # Send the email
    email.send()

    # Return a response indicating the certificate has been sent
    return HttpResponse('Certificate sent to your email.')


# for python section
@login_required
def generate_pythoncertificate(request):
    # Your existing code for generating the certificate
    user = request.user
    # Calculate total scores for Basic, Intermediate, and Advanced sections
    basic_score = TestResult.objects.filter(user=user, section__startswith='Basic').aggregate(total_score=Sum('score'))[
                      'total_score'] or 0
    intermediate_score = \
        TestResult.objects.filter(user=user, section__startswith='Intermediate').aggregate(total_score=Sum('score'))[
            'total_score'] or 0
    advanced_score = \
        TestResult.objects.filter(user=user, section__startswith='Advanced').aggregate(total_score=Sum('score'))[
            'total_score'] or 0

    # Calculate total score and percentage
    total_score = basic_score + intermediate_score + advanced_score
    # total_questions = TestResult.objects.filter(user=user).count()  # Assuming each test has equal weight
    total_percentage = int((total_score / 30) * 100)
    print(total_score)

    # Load the existing certificate PNG template
    template_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/pythoncertificate.png'  # Replace with the path to your font file
    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={user.username}_certificate.png'

    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 60
    font_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # # Position to display the percentage
    # percentage_position = (780, 750)
    # percentage_text = f' {total_percentage:}%'
    # draw.text(percentage_position, percentage_text, fill="black", font=font)

    # Overlay the user's name onto the certificate
    name_position = (780, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)
    # Retrieve the latest project associated with the user
    latest_project = UploadedFile.objects.filter(student=user, project_language='python').latest('id')

    # Convert project name to uppercase
    uppercase_project_name = latest_project.project_name.upper()

    # Overlay the latest project name onto the certificate
    project_name_position = (780, 970)  # Adjust the position as needed
    draw.text(project_name_position, uppercase_project_name, fill="black", font=font)

    # You can add more overlay text or images as needed
    #     # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    # Save the modified image to the response
    img.save(response, format='PNG')
    return response


@login_required
def send_pythoncertificate_email(request):
    # Your existing code for sending the certificate via email
    user = request.user
    # Calculate total scores for Basic, Intermediate, and Advanced sections
    basic_score = TestResult.objects.filter(user=user, section__startswith='Basic').aggregate(total_score=Sum('score'))[
                      'total_score'] or 0
    intermediate_score = \
        TestResult.objects.filter(user=user, section__startswith='Intermediate').aggregate(total_score=Sum('score'))[
            'total_score'] or 0
    advanced_score = \
        TestResult.objects.filter(user=user, section__startswith='Advanced').aggregate(total_score=Sum('score'))[
            'total_score'] or 0

    # Calculate total score and percentage
    total_score = basic_score + intermediate_score + advanced_score
    # total_questions = TestResult.objects.filter(user=user).count()  # Assuming each test has equal weight
    total_percentage = int((total_score / 30) * 100)
    print(total_score)

    # Load the existing certificate PNG template
    template_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/pythoncertificate.png'  # Replace with the path to your font file

    # Open the existing certificate image using Pillow
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 60
    font_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (780, 680)  # Adjust the position as needed
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)

    # Retrieve the latest project associated with the user
    latest_project = UploadedFile.objects.filter(student=user, project_language='python').latest('id')

    # Convert project name to uppercase
    uppercase_project_name = latest_project.project_name.upper()

    # Overlay the latest project name onto the certificate
    project_name_position = (780, 970)  # Adjust the position as needed
    draw.text(project_name_position, uppercase_project_name, fill="black", font=font)
    # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Attach the certificate to the email
    email = EmailMessage(
        'Your Certificate',
        'Congratulations! You have successfully generated your certificate.',
        'sumodkanthcs@gmail.com',  # Replace with your email address
        [user.email],  # Send to the authenticated user's email address
    )
    # Attach the certificate to the email
    email.attach('certificate.png', img_byte_array.getvalue(), 'image/png')
    # Add a success message

    # Send the email
    email.send()

    # Return a response indicating the certificate has been sent
    return HttpResponse('Certificate sent to your email.')


# for php section
@login_required
def generate_phpcertificate(request):
    # Your existing code for generating the certificate
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/phpcertificate.png'  # Replace with the path to your font file

    # Create a response object to store the PNG
    response = HttpResponse(content_type='image/png')
    response['Content-Disposition'] = f'filename={user.username}_certificate.png'

    # Open the existing certificate image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 60
    font_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (780, 680)  # Adjust the position as needed(horizontal,vertical)
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)
    # Retrieve the latest project associated with the user
    latest_project = UploadedFile.objects.filter(student=user, project_language='php').latest('id')

    # Convert project name to uppercase
    uppercase_project_name = latest_project.project_name.upper()

    # Overlay the latest project name onto the certificate
    project_name_position = (780, 970)  # Adjust the position as needed
    draw.text(project_name_position, uppercase_project_name, fill="black", font=font)
    #     # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')
    # Save the modified image to the response
    img.save(response, format='PNG')
    return response


@login_required
def send_phpcertificate_email(request):
    # Your existing code for sending the certificate via email
    user = request.user

    # Load the existing certificate PNG template
    template_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/phpcertificate.png'  # Replace with the path to your font file

    # Open the existing certificate image using Pillow
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Specify the font and size for the text overlay
    font_size = 60
    font_path = 'C:/Projects/Learning/Personalized-E-Learning/accounts/static/images/Roboto-Medium.ttf'  # Replace with the path to your font file
    font = ImageFont.truetype(font_path, font_size)

    # Overlay the user's name onto the certificate
    name_position = (780, 680)  # Adjust the position as needed
    uppercase_name = user.get_full_name().upper()
    draw.text(name_position, uppercase_name, fill="black", font=font)
    # Retrieve the latest project associated with the user
    latest_project = UploadedFile.objects.filter(student=user, project_language='php').latest('id')

    # Convert project name to uppercase
    uppercase_project_name = latest_project.project_name.upper()

    # Overlay the latest project name onto the certificate
    project_name_position = (780, 970)  # Adjust the position as needed
    draw.text(project_name_position, uppercase_project_name, fill="black", font=font)

    # Save the modified image to BytesIO
    img_byte_array = BytesIO()
    img.save(img_byte_array, format='PNG')

    # Attach the certificate to the email
    email = EmailMessage(
        'Your Certificate',
        'Congratulations! You have successfully generated your certificate.',
        'sumodkanthcs@gmail.com',  # Replace with your email address
        [user.email],  # Send to the authenticated user's email address
    )
    # Attach the certificate to the email
    email.attach('certificate.png', img_byte_array.getvalue(), 'image/png')
    # Add a success message

    # Send the email
    email.send()

    # Return a response indicating the certificate has been sent
    return HttpResponse('Certificate sent to your email.')


# views.py
def feedback(request):
    feedback_data = Feedback.objects.all()
    return render(request, 'thankyou.html', {'feedback_data': feedback_data})


# views.py


class submit_feedback(CreateView):
    template_name = "feedback.html"
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy("feedback")


# def submit_feedback(request):
#     if request.method == 'POST':
#         form = FeedbackForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,"feedback.html",{"form":form})
#         else:
#             return HttpResponse({'message': 'Please fill in all fields correctly.'}, status=400)
#     else:
#         # If request method is not POST, return a method not allowed response
#         return HttpResponse({'error': 'Method not allowed.'}, status=405)


class Feedbacks(TemplateView):
    template_name = "feedback.html"


def Contact(request):
    return render(request, "contactus.html")


@login_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the uploaded project with the authenticated user
            project = form.save(commit=False)  # Don't save to database yet
            project.student = request.user  # Associate with the authenticated user
            project.save()  # Now save to database
            return redirect('project_list')  # Redirect to file list page after successful upload
    else:
        form = ProjectUploadForm()  # Create a new form instance if not a POST request
    return render(request, 'upload_project.html', {'form': form})  # Render the form template


@login_required
def upload_project3(request):
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the uploaded project with the authenticated user
            project = form.save(commit=False)  # Don't save to database yet
            project.student = request.user  # Associate with the authenticated user
            project.save()  # Now save to database
            return redirect('project_list')  # Redirect to file list page after successful upload
    else:
        form = ProjectUploadForm()  # Create a new form instance if not a POST request
    return render(request, 'upload_project3.html', {'form': form})  # Render the form template


@login_required
def upload_project4(request):
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Associate the uploaded project with the authenticated user
            project = form.save(commit=False)  # Don't save to database yet
            project.student = request.user  # Associate with the authenticated user
            project.save()  # Now save to database
            return redirect('project_list')  # Redirect to file list page after successful upload
    else:
        form = ProjectUploadForm()  # Create a new form instance if not a POST request
    return render(request, 'upload_projectmain.html', {'form': form})  # Render the form template


def project_list(request):
    projects = UploadedFile.objects.all()

    return render(request, 'project_list.html', {'projects': projects})


def download_project(request, project_id):
    project = get_object_or_404(UploadedFile, pk=project_id)
    file_path = project.file.path
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type="application/force-download")
        response['Content-Disposition'] = 'attachment; filename=%s' % project.file.name.split('/')[-1]
        return response
