# Generated by Django 2.2.1 on 2019-05-12 20:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190511_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='foto',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='foto'),
        ),
    ]