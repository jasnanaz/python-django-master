# Generated by Django 2.2.9 on 2020-01-13 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]