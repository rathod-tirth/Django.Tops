# Generated by Django 5.0.1 on 2024-01-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_delete_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=20)),
                ('notice_title', models.CharField(max_length=50)),
                ('notice_text', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
