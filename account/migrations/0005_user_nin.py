# Generated by Django 3.2.18 on 2023-03-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_date_of_hire_user_level_of_authourity'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nin',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
