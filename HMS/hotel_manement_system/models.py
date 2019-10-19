from django.db import models
from datetime import date, timedelta


class Hotel(models.Model):
    name = models.CharField(verbose_name="Name", help_text='Enter Hotel name', max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    type = models.CharField(verbose_name='Category', help_text='Enter type of room', max_length=100)
    price = models.CharField(verbose_name='Price', help_text='Enter the price', max_length=10)

    def __str__(self):
        return self.type


class Room(models.Model):
    number = models.CharField(verbose_name='Room No', help_text='Enter room number', max_length=3)
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE,
                                 help_text='Select category')

    def __str__(self):
        return self.number

    def room_type(self):
        return self.category.type


class Guest(models.Model):
    name = models.CharField(verbose_name='Name', help_text='Enter Guest name', max_length=100)
    phone_no = models.CharField(verbose_name='Contact Number', help_text='Enter phone number', max_length=10)
    adhar_number = models.CharField(verbose_name='Adhar number', help_text='Enter adhar number', max_length=12)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(verbose_name='Manager name', help_text='Enter manager name', max_length=100)
    phone_number = models.CharField(verbose_name='Phone number', help_text='Enter phone number', max_length=10)
    Hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, verbose_name='Hotel Name',
                              help_text='Select manager hotel', null=True)

    def __str__(self):
        return self.name


class Record(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Booking ID')
    room_no = models.ForeignKey(Room, verbose_name='Room number', help_text='Select room', on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, verbose_name='Guest name', help_text='Select guest', on_delete=models.CASCADE)
    people_count = models.IntegerField(default=1, verbose_name='Total guest', help_text='Enter number of people')
    checkin_date = models.DateField(verbose_name='Check In date', help_text='select date', default=date.today())
    checkout_date = models.DateField(verbose_name='Check out date', help_text='select date', default=date.today()+timedelta(days=1))
    modified = models.BooleanField(verbose_name='Modify my check out date',
                                   help_text='select if you want to modify your checkout date', default=False)
    completed = models.BooleanField(default=False, verbose_name='Check out')
    is_canceled = models.BooleanField(default=False, verbose_name='Cancel', help_text='select to cancel booking')

    def calculate_price(self):
        days = (self.checkout_date - self.checkin_date).days
        if date.today() < self.checkout_date and self.completed:
            days = (self.checkin_date - date.today()).days
        if days == 0:
            days = 1
        price = int(self.room_no.category.price)
        return days * price

    calculate_price.short_description = 'Total Cost'

    def __str__(self):
        return str(self.id)
