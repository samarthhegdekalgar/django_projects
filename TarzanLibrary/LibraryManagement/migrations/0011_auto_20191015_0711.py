# Generated by Django 2.2.6 on 2019-10-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagement', '0010_auto_20191015_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book_returned',
            field=models.BooleanField(default=False),
        ),
    ]
