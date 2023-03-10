# Generated by Django 4.1.3 on 2022-12-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_studs_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studs',
            name='email',
            field=models.EmailField(max_length=300, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='studs',
            name='roll',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
