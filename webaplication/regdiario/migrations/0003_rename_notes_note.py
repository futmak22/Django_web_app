# Generated by Django 4.1 on 2022-08-17 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regdiario', '0002_alter_day_number_alter_pacient_age_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notes',
            new_name='Note',
        ),
    ]
