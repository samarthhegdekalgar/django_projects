from django.db import models
from datetime import date, timedelta


class Hotel(models.Model):
    name = models.CharField(verbose_name="Name", help_text='Enter Hotel name', max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    type = models.CharField(verbose_name='Category', help_text='Enter type of room', max_length=100)
    price = models.IntegerField(verbose_name='Price', help_text='Enter the price')

    def __str__(self):
        return self.type


class Room(models.Model):
    number = models.IntegerField(verbose_name='Room No', help_text='Enter room number')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE,
                                 help_text='Select category')

    def __str__(self):
        return str(self.number)


class Guest(models.Model):
    name = models.CharField(verbose_name='Name', help_text='Enter Guest name', max_length=100)
    phone_no = models.IntegerField(verbose_name='Contact Number', help_text='Enter phone number')
    adhar_number = models.IntegerField(verbose_name='Adhar number', help_text='Enter adhar numbr')

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(verbose_name='Manger name', help_text='Enter manager name', max_length=100)
    phone_number = models.IntegerField(verbose_name='Phone number', help_text='Enter phone number')

    def __str__(self):
        return self.name


class Record(models.Model):
    id = models.AutoField(primary_key=True)
    room_no = models.ForeignKey(Room, verbose_name='Room number', help_text='Select room', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, verbose_name='Guest name', help_text='Select guest', on_delete=models.CASCADE)
    people_count = models.IntegerField(default=1, verbose_name='Total guest', help_text='Enter number of people')
    checkin_date = models.DateField(verbose_name='Check In date', help_text='select date', default=date.today())
    checkout_date = models.DateField(verbose_name='Check out date', help_text='select date', default=date.today()+timedelta(days=1))
    completed = models.BooleanField(default=False, verbose_name='Completed Transaction')
    is_canceled = models.BooleanField(default=False, verbose_name='Canceled', help_text='select to cancel booking')

    def calculate_price(self):
        days = (self.checkout_date - self.checkin_date).days
        price = self.room_no.category.price

        return days * price
