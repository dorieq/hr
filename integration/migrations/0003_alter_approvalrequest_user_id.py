# Generated by Django 4.2.6 on 2023-10-15 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0002_applicationtemplate_approvalrequest_exam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalrequest',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
