from django.shortcuts import render
from biblio.models import Media



def list_media(request):

    media = Media.objects.all()
    context = {
 
        'media': media,
    }
    return render(request, 'member/list-media.html', context)