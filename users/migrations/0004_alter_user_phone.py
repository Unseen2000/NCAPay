# Generated by Django 3.2.8 on 2021-10-19 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211017_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11, null=True, unique=True),
        ),
    ]