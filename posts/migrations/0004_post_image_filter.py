# Generated by Django 3.2.19 on 2023-07-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20230704_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_filter',
            field=models.CharField(choices=[('novice', 'Novice'), ('intermediate', 'Intermediate'), ('professional', 'Professional')], default='normal', max_length=32),
        ),
    ]