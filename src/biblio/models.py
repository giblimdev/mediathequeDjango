#biblio/models.py
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Member(models.Model):
    name = models.CharField(max_length=100, unique=True)
    can_borrow = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def current_borrowings(self):
        return self.borrowing_set.filter(return_date__isnull=True).count()

    def can_borrow_media(self):
        return self.current_borrowings() < 3 and not self.has_overdue_borrowing()

    def has_overdue_borrowing(self):
        return self.borrowing_set.filter(return_date__isnull=True, due_date__lt=timezone.now()).exists()

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

class Borrowing(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Emprunt'
    
    def save(self, *args, **kwargs):
        if self.media.category == 'board_game':
            raise ValidationError("Les jeux de société ne peuvent pas être empruntés.")
        
        if self.member.has_overdue_borrowing():
            raise ValidationError("Ce membre ne peut pas emprunter, il a un emprunt en retard.")
        
        if self.member.current_borrowings() >= 3:
            raise ValidationError("Ce membre ne peut pas avoir plus de 3 emprunts à la fois.")

        # Définir la date limite à 1 semaine après l'emprunt
        self.due_date = timezone.now() + timedelta(weeks=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member.name} emprunte {self.media.title}"
            
class Book(Media):
    
    class Meta:
        verbose_name = 'Livre'
        
class Dvd(Media):
    
   class Meta:
        verbose_name_plural = 'Dvd'

class Cd(Media):
   
   class Meta:
          verbose_name_plural = 'Cd'

class BoardGame(Media):
    
    class Meta:
        verbose_name = 'Jeu de plateau'

