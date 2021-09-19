# Generated by Django 3.2 on 2021-04-30 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigfishapp', '0006_remove_admindb_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='categorydb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(blank=True, max_length=30, null=True)),
                ('Category_description', models.CharField(blank=True, max_length=100, null=True)),
                ('FileUpload', models.ImageField(null=True, upload_to='categoryimage/')),
            ],
        ),
    ]