# Generated by Django 5.1.3 on 2024-12-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0006_alter_buyer_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='age_limited',
            field=models.BooleanField(default=False),
        ),
    ]
