from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Member, Media, Borrowing

class BiblioTestCase(TestCase):

    def setUp(self):
        # Crée des membres pour les tests
        self.member1 = Member.objects.create(id=1, name="Jean Dupont", nb_borrow=0, has_overdue=False, can_borrow=True)
        self.member2 = Member.objects.create(id=2, name="Marie Martin", nb_borrow=2, has_overdue=False, can_borrow=True)
        self.member3 = Member.objects.create(id=3, name="Pierre Durand", nb_borrow=3, has_overdue=False, can_borrow=False)

        # Crée des médias pour les tests
        self.book = Media.objects.create(id=1,title="Le Petit Prince", author="Saint-Exupéry", category="book", is_available=True)
        self.dvd = Media.objects.create(id=2, title="Matrix", author="Wachowski", category="Dvd", is_available=True)
        self.cd = Media.objects.create(id=3,title="Album Test", author="Artiste Test", category="Cd", is_available=True)
        self.board_game = Media.objects.create(id=4,title="Monopoly", author="Parker Brothers", category="board_game", is_available=False)

        # Crée des emprunts pour les tests
        self.borrowing1 = Borrowing.objects.create(member=self.member1, media=self.book, borrow_date=timezone.now() - timedelta(days=2))
        self.borrowing2 = Borrowing.objects.create(member=self.member2, media=self.dvd, borrow_date=timezone.now() - timedelta(days=5), due_date=timezone.now() + timedelta(days=2))
        self.borrowing3 = Borrowing.objects.create(member=self.member1, media=self.cd, borrow_date=timezone.now() - timedelta(days=8), due_date=timezone.now() - timedelta(days=1))

    def test_member_creation(self):
        member = Member.objects.get(name="Jean Dupont")
        self.assertEqual(member.nb_borrow, 2)
        self.assertTrue(member.can_borrow)
        self.assertFalse(member.has_overdue)
        
    
    def test_board_game_availability(self):
        self.assertFalse(self.board_game.is_available)
        new_board_game = Media.objects.create(title="Risk", author="Hasbro", category="board_game", is_available=False)
        self.assertFalse(new_board_game.is_available)

    def test_borrowing_dates(self):
        now = timezone.now()
        borrowing = Borrowing.objects.create(member=self.member1, media=self.book, borrow_date=now)
        self.assertEqual(borrowing.due_date.date(), (now + timedelta(days=7)).date())

    
    def test_borrowing_process(self):
        now = timezone.now()
        borrowing = Borrowing.objects.create(member=self.member1, media=self.book, borrow_date=now)
        self.assertEqual(borrowing.due_date.date(), (now + timedelta(days=7)).date())
        self.assertIsNone(borrowing.return_date)
 
    