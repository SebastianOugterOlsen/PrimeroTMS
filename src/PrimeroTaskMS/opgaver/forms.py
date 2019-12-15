from django import forms

from .models import Opgaver

class OpgaverForm(forms.ModelForm):
    class Meta:
        model = Opgaver
        fields = [
            'kunde_navn',
            'ansvarlig',
            'opgave_beskrivelse',
            'noter',
            'tid_brugt',
            'status',
            'deadline',
            'prioritet',
        ]