# Generated by Django 3.2 on 2021-08-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_remove_group_message_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
            ],
        ),
    ]