# Generated by Django 2.2.6 on 2019-10-19 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_manement_system', '0012_auto_20191019_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(help_text='Enter room number', max_length=3, verbose_name='Room No'),
        ),
    ]
