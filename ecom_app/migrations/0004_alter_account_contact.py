# Generated by Django 5.0.3 on 2024-04-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0003_product_alter_account_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='contact',
            field=models.CharField(max_length=254),
        ),
    ]