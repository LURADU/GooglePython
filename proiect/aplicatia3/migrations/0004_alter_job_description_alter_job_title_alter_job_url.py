# Generated by Django 4.0.4 on 2022-05-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatia3', '0003_job_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
