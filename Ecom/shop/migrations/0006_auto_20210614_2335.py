# Generated by Django 2.0.12 on 2021-06-14 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210614_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_form',
            name='add_date',
            field=models.DateField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
