# Generated by Django 3.1.4 on 2020-12-13 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='mobilenum',
            new_name='mobileno',
        ),
    ]
