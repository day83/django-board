# Generated by Django 4.0.4 on 2022-06-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_comment_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]
