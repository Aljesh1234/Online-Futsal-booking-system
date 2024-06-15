# forms.py
from django import forms
from .models import FutsalBooking

class BookingForm(forms.ModelForm):
    class Meta:
        model = FutsalBooking
        fields = ['username', 'email', 'mblnumber', 'futsal_choice', 'date', 'time']
