from django import forms
from .models import Participation

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = ['will_come']
        widgets = {
            'will_come': forms.RadioSelect(choices=[(True, "Je viens"), (False, "Je ne viens pas")])
        }
