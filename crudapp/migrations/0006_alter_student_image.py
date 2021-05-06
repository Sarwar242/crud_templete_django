# Generated by Django 3.2 on 2021-05-02 10:43

import crudapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0005_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=crudapp.models.UploadToPathAndRename('images/profile_image')),
        ),
    ]