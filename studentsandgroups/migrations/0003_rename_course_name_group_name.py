# Generated by Django 5.0.6 on 2024-05-26 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentsandgroups', '0002_alter_group_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='course_name',
            new_name='name',
        ),
    ]
