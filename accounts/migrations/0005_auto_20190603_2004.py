# Generated by Django 2.2.1 on 2019-06-03 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_hoodid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hoodid',
            new_name='hood',
        ),
    ]
