# Generated by Django 5.0.6 on 2025-06-24 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_customer_customer_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Customer_Email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
