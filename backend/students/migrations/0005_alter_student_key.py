# Generated by Django 3.2.13 on 2022-12-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_alter_student_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='key',
            field=models.BooleanField(verbose_name='패스워드 키'),
        ),
    ]
