# Generated by Django 5.0.6 on 2025-06-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('New_customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_customer',
            name='Customer_AccountNo',
        ),
        migrations.AlterField(
            model_name='new_customer',
            name='Customer_Email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
