# Generated by Django 4.1.7 on 2023-03-22 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='desc',
            new_name='desc1',
        ),
    ]
