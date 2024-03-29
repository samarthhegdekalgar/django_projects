# Generated by Django 2.2.6 on 2019-10-13 16:26

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(help_text='Enter author name', max_length=100)),
                ('about_author', models.TextField(blank=True, help_text='Small introduction about author', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(help_text='Enter book name', max_length=200)),
                ('ISBN', models.CharField(blank=True, help_text='Enter ISBN', max_length=23, validators=[django.core.validators.MinLengthValidator(13)])),
                ('category', models.CharField(blank=True, help_text='Enter category of book', max_length=50)),
                ('availability', models.BooleanField(default=False)),
                ('number_of_copy', models.IntegerField(default=1, help_text='Number of available books')),
                ('book_price', models.IntegerField(default=0, help_text='Book price on market')),
                ('book_description', models.TextField(blank=True, help_text='Complete overview of book', null=True)),
                ('author_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(help_text='Enter Member name', max_length=50)),
                ('member_ID', models.CharField(help_text='Enter member ID number', max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
                ('member_email', models.EmailField(max_length=254)),
                ('member_phone_no', models.CharField(help_text='Enter member Phone number', max_length=13, validators=[django.core.validators.MinLengthValidator(10)])),
                ('member_address', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(default=datetime.date(2019, 10, 20))),
                ('borrowed_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Book')),
                ('borrowed_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Member')),
            ],
        ),
    ]
