# Generated by Django 2.2.7 on 2019-12-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0005_auto_20191220_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
