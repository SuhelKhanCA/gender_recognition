from django.urls import path
from .views import upload_voice, feedback

urlpatterns = [
    path('', upload_voice, name='upload_voice'),
    path('feedback/<int:sample_id>/', feedback, name='feedback'),
]
