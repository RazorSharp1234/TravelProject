# Generated by Django 4.1.7 on 2023-03-22 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_rename_desc_place_desc1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='desc1',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='place',
            name='heading',
        ),
    ]
