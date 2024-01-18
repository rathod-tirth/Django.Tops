# Generated by Django 5.0.1 on 2024-01-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_member_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='familyno',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='tenant',
            field=models.CharField(default='owner', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='vehicleno',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
