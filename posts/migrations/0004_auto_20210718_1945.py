# Generated by Django 3.2.4 on 2021-07-18 16:45

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.FileField(blank=True, default='', upload_to=posts.models.comment_directory_path),
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, default='', upload_to=posts.models.post_directory_path),
        ),
    ]