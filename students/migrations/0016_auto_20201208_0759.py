# Generated by Django 2.2.13 on 2020-12-08 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_auto_20201208_0759'),
        ('students', '0015_admissionstudent_rejected'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.AdmissionStudent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='batch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='academics.Batch'),
        ),
        migrations.AddField(
            model_name='student',
            name='temp_serial',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='admissionstudent',
            name='choosen_department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admission_students', to='academics.Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='registration_number',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
