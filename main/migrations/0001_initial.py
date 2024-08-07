# Generated by Django 5.1 on 2024-08-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compliant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Full name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email address')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='Phone number')),
                ('compliant', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
