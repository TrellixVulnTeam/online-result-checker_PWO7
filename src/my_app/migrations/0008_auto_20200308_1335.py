# Generated by Django 2.1.5 on 2020-03-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AlterField(
            model_name='account',
            name='study_level',
            field=models.IntegerField(choices=[(100, 'ND 1'), (200, 'ND 2')], default=100),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
