# Generated by Django 3.2.23 on 2023-12-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20231203_1716'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_date']},
        ),
    ]
