# Generated by Django 4.1.7 on 2023-03-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
