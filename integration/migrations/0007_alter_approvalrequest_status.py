# Generated by Django 4.2.6 on 2023-10-15 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0006_alter_approvalrequest_iin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalrequest',
            name='status',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
