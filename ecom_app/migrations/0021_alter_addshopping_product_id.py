# Generated by Django 5.0.3 on 2024-08-01 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0020_rename_product_id_addshopping_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addshopping',
            name='product_id',
            field=models.JSONField(),
        ),
    ]
