# Generated by Django 3.1.4 on 2021-01-02 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtally', '0006_tally_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tally',
            name='date',
            field=models.DateField(),
        ),
    ]
