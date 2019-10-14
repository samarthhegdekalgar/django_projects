from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime, date, timedelta
from django.db.models import signals
from django.dispatch import receiver


class Author(models.Model):
    author_name = models.CharField(max_length=100, help_text='Enter author name')
    about_author = models.TextField(blank=True, null=True, help_text='Small introduction about author')

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=200, help_text='Enter book name')
    ISBN = models.CharField(max_length=23, blank=True, validators=[MinLengthValidator(13)], help_text='Enter ISBN')
    category = models.CharField(max_length=50, blank=True, help_text='Enter category of book')
    availability = models.BooleanField(default=False)
    number_of_copy = models.IntegerField(default=1, help_text='Number of available books')
    in_stock = models.IntegerField(default=1, help_text='Number of copies available for Members')
    book_price = models.IntegerField(default=0, help_text='Book price on market')
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_description = models.TextField(blank=True, null=True, help_text='Complete overview of book')

    def __str__(self):
        return self.book_name


class Member(models.Model):
    member_name = models.CharField(max_length=50, help_text='Enter Member name')
    member_ID = models.CharField(max_length=6, validators=[MinLengthValidator(6)],
                                 help_text='Enter member ID number')
    member_email = models.EmailField()
    member_phone_no = models.CharField(max_length=13, validators=[MinLengthValidator(10)], help_text='Enter member '
                                                                                                     'Phone number')
    member_address = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.member_name


class Borrow(models.Model):
    borrowed_member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Member')
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    book_returned = models.BooleanField(auto_created=True, default=False)
    return_date = models.DateField(default=date.today() + timedelta(days=7))

    def expired(self):
        return_date = self.return_date
        if date.today() > return_date:
            return True
        else:
            return False

    def is_returned(self):
        if self.book_returned:
            return True
        else:
            return False

    is_returned.boolean = True
    is_returned.short_description = 'Returned'
    expired.boolean = True
    expired.short_description = 'Expired'


@receiver(signals.pre_save, sender=Borrow)
def is_returned(sender, instance, **kwargs):
    stock = instance.borrowed_book.in_stock
    if not instance.book_returned:
        if instance.borrowed_book.number_of_copy > stock:
            stock += 1
            book = instance.borrowed_book
            instance.book_returned = True
            book.in_stock = stock
            book.save()


@receiver(signals.post_save, sender=Borrow)
def is_borrowed(sender, instance, created, **kwargs):
    if not instance.book_returned:
        if created:
            stock = instance.borrowed_book.in_stock
            if stock > 0:
                stock -= 1
                book = instance.borrowed_book
                book.in_stock = stock
                book.save()

