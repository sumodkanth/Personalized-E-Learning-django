from django import forms
from accounts.models import Placement


class PlacementForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = ['company_name', 'job_title', 'job_description', 'image_icon', 'location', 'qualification', 'skills']
