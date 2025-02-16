from django.db import models

class VoiceSample(models.Model):
    voice_file = models.FileField(upload_to='voices/')
    predicted_gender = models.CharField(max_length=10, blank=True, null=True)
    user_feedback = models.BooleanField(null=True, blank=True)  # True = Correct, False = Incorrect
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voice Sample {self.id} - {self.predicted_gender}"
