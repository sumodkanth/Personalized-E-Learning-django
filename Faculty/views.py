from django.shortcuts import render


# Create your views here.
def facultyindex(request):
    return render(request, 'facultyindex.html')
