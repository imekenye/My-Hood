# Generated by Django 2.2.1 on 2019-06-03 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neighbourhood',
            old_name='admin',
            new_name='user',
        ),
    ]
