# Generated by Django 5.0.1 on 2024-01-08 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_chairman_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='../../media/default.png', upload_to='media/upload'),
        ),
    ]
