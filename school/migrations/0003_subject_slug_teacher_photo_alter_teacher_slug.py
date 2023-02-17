# Generated by Django 4.1.7 on 2023-02-17 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_rename_url_news_slug_rename_url_teacher_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(blank=True, upload_to='teachers_photo/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
