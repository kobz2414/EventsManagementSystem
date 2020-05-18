from django import forms
from .models import event

class addAndEditForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['event_name', 'event_location', 'event_date', 'event_remarks', 'event_pricing']