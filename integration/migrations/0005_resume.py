# Generated by Django 4.2.6 on 2023-10-15 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integration', '0004_remove_approvalrequest_user_id_approvalrequest_iin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='resumes/')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integration.department')),
                ('iin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes_as_iin', to='integration.employee')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resumes_as_name', to='integration.employee')),
            ],
        ),
    ]
