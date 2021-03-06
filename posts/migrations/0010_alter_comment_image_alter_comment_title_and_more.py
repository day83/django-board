# Generated by Django 4.0.4 on 2022-06-14 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_alter_comment_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(blank=True, default='Anonymous', max_length=50),
        ),
    ]
