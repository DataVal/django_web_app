from django import forms

from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__' #Vai usar todos os campos do Reservation