from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_price = models.IntegerField(default=0)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name
