# Generated by Django 5.0.3 on 2024-08-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0018_rename_product_addshopping_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addshopping',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]