# biblio/forms.py
from django import forms
from .models import Member, Media, Borrowing

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'can_borrow']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['title', 'author', 'category', 'is_available']

class BorrowingForm(forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ['member', 'media']