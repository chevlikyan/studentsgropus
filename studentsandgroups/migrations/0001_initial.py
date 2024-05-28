# Generated by Django 5.0.6 on 2024-05-26 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('Mathematics', 'Mathematics'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('English', 'English'), ('Russian', 'Russian'), ('French', 'French'), ('Spanish', 'Spanish'), ('Armenian', 'Armenian'), ('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Java', 'Java')], max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('duration', models.CharField(choices=[('1 hour', '1 hour'), ('2 hours', '2 hours'), ('3 hours', '3 hours'), ('4 hours', '4 hours')], max_length=10)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='students')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsandgroups.group')),
            ],
        ),
    ]