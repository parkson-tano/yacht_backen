# Generated by Django 4.1.7 on 2023-03-18 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_employeedata_port'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedata',
            old_name='delete',
            new_name='is_delete',
        ),
        migrations.RenameField(
            model_name='portdata',
            old_name='delete',
            new_name='is_delete',
        ),
    ]