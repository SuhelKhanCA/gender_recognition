from django.shortcuts import render, redirect
from .forms import VoiceUploadForm
from .models import VoiceSample
from .utils import predict_gender

def upload_voice(request):
    if request.method == "POST":
        form = VoiceUploadForm(request.POST, request.FILES)
        if form.is_valid():
            voice_sample = form.save()
            voice_sample.predicted_gender = predict_gender(voice_sample.voice_file.path)
            voice_sample.save()
            return redirect('feedback', voice_sample.id)
    else:
        form = VoiceUploadForm()
    return render(request, 'gender_recognition/upload.html', {'form': form})

def feedback(request, sample_id):
    voice_sample = VoiceSample.objects.get(id=sample_id)
    
    if request.method == "POST":
        feedback = request.POST.get("feedback")
        voice_sample.user_feedback = True if feedback == "correct" else False
        voice_sample.save()
        return redirect('upload_voice')

    return render(request, 'gender_recognition/feedback.html', {'sample': voice_sample})
