# biblio/views.py


from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm, MediaForm, BorrowingForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from .models import Borrowing, Member, Media
from django.contrib import messages  

def base(request):    
    return  render(request, 'biblio/base.html', {   
    })
    
def home(request):
    
    members = Member.objects.all()
    medias = Media.objects.all()
    borrowings = Borrowing.objects.filter(return_date__isnull=True)
    context = {
        'members': members,
        'medias': medias,
        'borrowings' : borrowings
    }
    return render(request, 'biblio/home.html', context)

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'biblio/member_form.html', {'form': form})

def member_detail(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'biblio/member_detail.html', {'member': member})


def member_update(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MemberForm(instance=member)
    return render(request, 'biblio/member_form.html', {'form': form})

def member_delete(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == "POST":
        member.delete()
        return redirect('home')
    return render(request, 'biblio/member_confirm_delete.html', {'member': member})




def media_create(request):
    if request.method == "POST":
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
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
            return redirect('home')
    else:
        form = MediaForm(instance=media)
    return render(request, 'biblio/media_form.html', {'form': form})

def media_delete(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    if request.method == "POST":
        media.delete()
        return redirect('home')
    return render(request, 'biblio/media_confirm_delete.html', {'media': media})
        
def borrowing_create(request):
    if request.method == "POST":
        form = BorrowingForm(request.POST)
        if form.is_valid():             
            form.save()
            return redirect('home')
    else:
        form = BorrowingForm()
    return render(request, 'biblio/borrowing_form.html', {'form': form})
           
def borrowing_detail(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    return render(request, 'biblio/borrowing_detail.html', {'borrowing': borrowing})

def borrowing_update(request, borrowing_id):
    borrowing = get_object_or_404(Borrowing, id=borrowing_id)
    if borrowing.return_date:
        messages.info(request, "Ce média a déjà été restitué.")
        return redirect('home')
    if request.method == "POST":
        borrowing.return_media()
        return redirect('home')
    context = {
        'borrowing': borrowing,
        'member': borrowing.member,
        'media': borrowing.media,
    }             
    return render(request, 'biblio/borrowing_return_confirm.html', context)
      
            
            




