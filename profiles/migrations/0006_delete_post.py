# Generated by Django 3.2.19 on 2023-07-04 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_post_image_filter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]