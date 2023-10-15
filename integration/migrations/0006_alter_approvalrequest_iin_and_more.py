# Generated by Django 4.2.6 on 2023-10-15 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0005_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvalrequest',
            name='iin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.employee'),
        ),
        migrations.AlterField(
            model_name='approvalrequest',
            name='status',
            field=models.CharField(blank=True, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='integration.position'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='iin',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='resume',
            name='iin',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes_as_iin', to='integration.employee'),
        ),
    ]
