# biblio/views.py


from django.shortcuts import render, redirect
from .models import Member, Media
from .forms import MemberForm, MediaForm

def index(request):
    


    return render(request, 'biblio/base.html', {
        
        
    })
    
def home(request):
    members = Member.objects.all()
    media = Media.objects.all()
    return render(request, 'biblio/home.html', { 
        'members': members,
        'media': media,          
    })

        
def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MemberForm()
    return render(request, 'biblio/member_form.html', {'form': form})

def member_update(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MemberForm(instance=member)
    return render(request, 'biblio/member_form.html', {'form': form})

def member_delete(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.delete()
        return redirect('index')
    return render(request, 'biblio/member_confirm_delete.html', {'member': member})
""""""
def media_create(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MediaForm()
    return render(request, 'biblio/media_form.html', {'form': form})

def media_detail(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    return render(request, 'biblio/media_detail.html', {'media': media})

def media_update(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == "POST":
        form = MediaForm(request.POST, instance=media)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MediaForm(instance=media)
    return render(request, 'biblio/media_form.html', {'form': form})

def media_delete(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == "POST":
        media.delete()
        return redirect('index')
    return render(request, 'biblio/media_confirm_delete.html', {'media': media})
    