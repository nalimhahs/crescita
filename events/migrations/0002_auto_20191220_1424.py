# Generated by Django 2.2.7 on 2019-12-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.TextField(max_length=4000),
        ),
    ]
