# Generated by Django 3.2.18 on 2023-05-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20230501_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyimsform',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='companypolicy',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='companyprocedure',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='departmentalprocedure',
            options={'ordering': ['position']},
        ),
        migrations.AlterModelOptions(
            name='imsform',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='companyimsform',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companypolicy',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companyprocedure',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='departmentalprocedure',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='imsform',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]