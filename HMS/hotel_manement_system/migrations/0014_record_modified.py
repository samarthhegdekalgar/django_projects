# Generated by Django 2.2.6 on 2019-10-19 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_manement_system', '0013_auto_20191019_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='modified',
            field=models.BooleanField(default=False, help_text='select if you want to modify your checkout date', verbose_name='Modify my check out date'),
        ),
    ]
