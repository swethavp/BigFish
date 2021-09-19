# Generated by Django 3.2 on 2021-05-03 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bigfishapp', '0007_categorydb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Product_Weight', models.CharField(blank=True, max_length=30, null=True)),
                ('Product_Price', models.CharField(blank=True, max_length=30, null=True)),
                ('Product_Category', models.CharField(blank=True, max_length=30, null=True)),
                ('Image', models.ImageField(null=True, upload_to='productimage/')),
            ],
        ),
    ]
