# Generated by Django 4.1.7 on 2023-03-30 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_department_position_user_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_of_hire',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='level_of_authourity',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
