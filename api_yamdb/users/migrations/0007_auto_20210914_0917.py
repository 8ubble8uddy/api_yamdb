# Generated by Django 2.2.16 on 2021-09-14 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210914_0911'),
    ]

    operations = [
        migrations.RenameField(
            model_name='confirmation',
            old_name='user_id',
            new_name='user',
        ),
    ]
