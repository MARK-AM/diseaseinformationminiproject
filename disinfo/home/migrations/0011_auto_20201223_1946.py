# Generated by Django 3.1.4 on 2020-12-23 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_info_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='detail',
            new_name='causes',
        ),
        migrations.AddField(
            model_name='info',
            name='ov',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='prev',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='risk',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='symptoms',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
