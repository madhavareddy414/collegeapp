# Generated by Django 3.1.4 on 2021-01-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ece', '0002_auto_20210121_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='smob',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='srno',
            field=models.CharField(max_length=30),
        ),
    ]
