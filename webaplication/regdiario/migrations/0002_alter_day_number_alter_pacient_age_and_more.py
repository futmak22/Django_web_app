# Generated by Django 4.1 on 2022-08-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regdiario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pacient',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='phase',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='track',
            name='number',
            field=models.IntegerField(),
        ),
    ]