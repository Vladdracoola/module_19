# Generated by Django 5.1.3 on 2024-12-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0004_alter_buyer_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
