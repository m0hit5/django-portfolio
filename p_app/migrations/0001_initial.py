# Generated by Django 3.2 on 2024-07-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('designation', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technologies', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='projects/')),
                ('github_link', models.URLField()),
                ('live_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
