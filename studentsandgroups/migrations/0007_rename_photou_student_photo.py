# Generated by Django 5.0.6 on 2024-05-26 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsandgroups', '0006_rename_photo_student_photou'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='photou',
            new_name='photo',
        ),
    ]