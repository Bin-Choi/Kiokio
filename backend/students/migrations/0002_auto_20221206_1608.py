# Generated by Django 3.2.13 on 2022-12-06 07:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbody',
            name='gender',
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='남성', max_length=10, verbose_name='성별'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='학생ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='0000', max_length=4, validators=[django.core.validators.MinLengthValidator(4)], verbose_name='비밀번호'),
        ),
    ]