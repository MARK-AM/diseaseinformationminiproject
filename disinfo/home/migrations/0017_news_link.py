# Generated by Django 3.1.4 on 2021-01-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_remove_news_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.TextField(default=''),
        ),
    ]
