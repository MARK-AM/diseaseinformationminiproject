# Generated by Django 3.1.4 on 2020-12-13 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201213_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobilenumber',
            field=models.IntegerField(max_length=20),
        ),
    ]