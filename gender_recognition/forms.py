from django import forms
from .models import VoiceSample

class VoiceUploadForm(forms.ModelForm):
    class Meta:
        model = VoiceSample
        fields = ['voice_file']
