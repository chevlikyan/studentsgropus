# Generated by Django 5.0.6 on 2024-05-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsandgroups', '0003_rename_course_name_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='student'),
        ),
    ]