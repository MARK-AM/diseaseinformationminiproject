# Generated by Django 3.1.4 on 2020-12-13 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201213_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='mobilenumber',
        ),
    ]
