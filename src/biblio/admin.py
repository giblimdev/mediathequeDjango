from django.contrib import admin
from .models import  Media, Book, Cd, Dvd, BoardGame, Member, Borrowing


# Register your models here.

admin.site.register(Media)
admin.site.register(Book)
admin.site.register(Cd)
admin.site.register(Dvd)
admin.site.register(BoardGame)
admin.site.register(Member)
admin.site.register(Borrowing)
