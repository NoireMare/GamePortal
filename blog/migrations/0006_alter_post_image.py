# Generated by Django 4.1.5 on 2023-01-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=0, upload_to='post_images'),
            preserve_default=False,
        ),
    ]
