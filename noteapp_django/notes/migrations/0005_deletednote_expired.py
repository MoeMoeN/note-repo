# Generated by Django 4.1.7 on 2023-04-24 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_deletednote_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='deletednote',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]
