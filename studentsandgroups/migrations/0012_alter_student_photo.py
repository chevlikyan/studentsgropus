# Generated by Django 5.0.6 on 2024-05-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentsandgroups', '0011_alter_student_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='student'),
        ),
    ]