# Generated by Django 2.1.4 on 2019-01-05 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser4', '0002_auto_20190103_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twogis',
            name='oid',
            field=models.FloatField(unique=True),
        ),
    ]
