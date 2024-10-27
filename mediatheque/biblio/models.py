
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta



class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nb_borrow = models.IntegerField(default=0)
    has_overdue = models.BooleanField(default=False)
    can_borrow = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Media(models.Model):
    CATEGORY_CHOICES = [
        ('book', 'Livre'),
        ('Dvd', 'Film'),
        ('Cd', 'Musique'),
        ('board_game', 'Jeu de société'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.category == 'board_game':
            self.is_available = False
        super().save(*args, **kwargs)
           

class Borrowing(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField()
    due_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Emprunt'

    def save(self, *args, **kwargs):
        self.borrow_date = timezone.now()
        self.due_date = self.borrow_date + timedelta(days=7)
        super().save(*args, **kwargs)
        self.media.is_available = False
        self.media.save()
        self.member.nb_borrow += 1
        if self.member.nb_borrow >= 3:
            self.member.can_borrow = False    
        self.member.save()  
        
    def return_media(self,  *args, **kwargs):
        self.return_date = timezone.now()
        super().save(*args, **kwargs)
        self.media.is_available = True
        self.media.save()
        self.member.nb_borrow -=1
        if self.member.nb_borrow <= 3:
            self.member.can_borrow = True    
        
        self.member.save()