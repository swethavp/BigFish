# Generated by Django 3.2 on 2021-04-27 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bigfishapp', '0004_admindb_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admindb',
            old_name='Status',
            new_name='Action',
        ),
    ]
