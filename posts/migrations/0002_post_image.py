# Generated by Django 4.0.4 on 2022-06-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='dummy.jpg', upload_to='images'),
            preserve_default=False,
        ),
    ]
