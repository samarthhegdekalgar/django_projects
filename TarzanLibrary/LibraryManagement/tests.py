from django.test import TestCase
from .models import Book, Author, Member, Borrow


class BookTestCase(TestCase):
    def setUp(self):
        author_obj = Author.objects.create(author_name='Paul Barry', about_author='He is a Author')
        Book.objects.create(book_name='Python', ISBN='9876543212345', category='Programming',
                            author_name=author_obj, )
        Member.objects.create(member_name='Samarth', member_ID='123456', member_email='uknowshk@gmail.com',
                              member_phone_no='1234567890')

    def test_book_name_correct(self):
        """Name of the book is identified """
        python = Book.objects.get(book_name='Python')
        self.assertEqual(python.get_title(), 'Python')
        self.assertEqual(python.get_availability(), True)

    def test_book_stock_update(self):
        """Stock value of the book in admin page is verified """
        member = Member.objects.get(member_name="Samarth")
        book = Book.objects.get(book_name="Python")
        original_stock = book.in_stock
        Borrow.objects.create(borrowed_member=member, borrowed_book=book, book_returned=False)
        new_book = Book.objects.get(book_name="Python")
        new_stock = new_book.in_stock
        self.assertEqual(original_stock - new_stock, 1)
