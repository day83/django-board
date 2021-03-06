# Generated by Django 4.0.4 on 2022-06-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_post_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author_email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.CharField(blank=True, default='Anonymous', max_length=50),
        ),
    ]
