# Generated by Django 5.0.1 on 2024-01-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_chairman_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='pic',
            field=models.FileField(default='default.png', upload_to='upload'),
        ),
    ]
