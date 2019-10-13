from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime, date, timedelta


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
    borrowed_member = models.ForeignKey(Member, on_delete=models.CASCADE)
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(default=date.today()+timedelta(days=7))
    expired = None

    def is_due(self):
        return_date = datetime.strptime(self.return_date, '%y %m %d')
        if date.today() > return_date:
            self.expired = 'Yes'
        else:
            self.expired = 'No'
