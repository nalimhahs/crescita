# Generated by Django 2.2.7 on 2019-12-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20191220_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
