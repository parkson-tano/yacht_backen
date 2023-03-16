# Generated by Django 4.1.7 on 2023-03-12 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('employee', '0005_personalinformation_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='user',
        ),
        migrations.AlterField(
            model_name='personalinformation',
            name='port',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.portdata'),
        ),
    ]