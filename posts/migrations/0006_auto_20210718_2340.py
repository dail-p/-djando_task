# Generated by Django 3.2.4 on 2021-07-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210718_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
        migrations.AddField(
            model_name='post',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
    ]
