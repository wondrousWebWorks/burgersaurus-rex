# Generated by Django 3.0.7 on 2020-07-07 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
    ]
