# Generated by Django 3.2 on 2021-08-09 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_message',
            name='room',
        ),
    ]
