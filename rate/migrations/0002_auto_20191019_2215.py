# Generated by Django 2.2.6 on 2019-10-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
