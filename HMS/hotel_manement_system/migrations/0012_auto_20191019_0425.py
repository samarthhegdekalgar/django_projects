# Generated by Django 2.2.6 on 2019-10-19 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_manement_system', '0011_auto_20191019_0421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='yes_or_no',
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(help_text='Enter manager name', max_length=100, verbose_name='Manager name'),
        ),
        migrations.AlterField(
            model_name='record',
            name='is_canceled',
            field=models.BooleanField(default=False, help_text='select to cancel booking', verbose_name='Cancel'),
        ),
    ]
