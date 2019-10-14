# Generated by Django 2.2.6 on 2019-10-14 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryManagement', '0006_auto_20191014_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='book_returned',
            field=models.BooleanField(auto_created=True, default=False),
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Borrow')),
            ],
        ),
    ]