# Generated by Django 3.2 on 2021-05-31 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fishapp', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='Image',
            field=models.ImageField(null=True, upload_to='productimage/'),
        ),
    ]
