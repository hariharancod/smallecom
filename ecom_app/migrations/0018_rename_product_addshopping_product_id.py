# Generated by Django 5.0.3 on 2024-08-01 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0017_rename_product_id_addshopping_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addshopping',
            old_name='Product',
            new_name='Product_id',
        ),
    ]
