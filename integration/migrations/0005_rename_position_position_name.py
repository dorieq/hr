# Generated by Django 4.2.6 on 2023-10-24 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0004_alter_employee_position'),
    ]

    operations = [
        migrations.RenameField(
            model_name='position',
            old_name='position',
            new_name='name',
        ),
    ]
