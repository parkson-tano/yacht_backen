# Generated by Django 3.2.18 on 2023-03-31 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_nin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_of_hire',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nin',
        ),
    ]
