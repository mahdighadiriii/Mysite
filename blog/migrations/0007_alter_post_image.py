# Generated by Django 3.2.23 on 2023-12-06 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='defualt.jpg', upload_to='blog/'),
        ),
    ]
