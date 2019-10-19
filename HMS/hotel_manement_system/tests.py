from django.test import TestCase
from .models import Hotel, Category, Room, Guest, Manager, Record


class RecordTestCase(TestCase):
    def setUp(self):
        Hotel.objects.create(name='Palace')
        Category.objects.create(type='Standard', price='1500')
        Room.objects.create(number='101', )