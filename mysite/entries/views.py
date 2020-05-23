from django.shortcuts import render
from .models import Video

# Create your views here.

def show_videos(request):
    video_list = Video.objects.all()

    context = {

        'video_list' : video_list

    }

    return render(request, 'entries/show_videos.html', context)