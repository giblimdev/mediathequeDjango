from django.contrib import admin

from django.contrib import admin
from .models import Media, Member, Borrowing

admin.site.register(Media)
admin.site.register(Member)
admin.site.register(Borrowing)
