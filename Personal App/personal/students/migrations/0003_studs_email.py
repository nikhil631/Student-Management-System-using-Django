# Generated by Django 4.1.3 on 2022-12-04 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_rename_students_studs'),
    ]

    operations = [
        migrations.AddField(
            model_name='studs',
            name='email',
            field=models.EmailField(max_length=300, null=True),
        ),
    ]