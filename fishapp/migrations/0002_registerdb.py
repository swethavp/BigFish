# Generated by Django 3.2 on 2021-05-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registerdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Email', models.CharField(blank=True, max_length=30, null=True)),
                ('Address', models.CharField(blank=True, max_length=50, null=True)),
                ('PhoneNo', models.IntegerField(blank=True, null=True)),
                ('Username', models.IntegerField(blank=True, max_length=20, null=True)),
                ('Password', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
