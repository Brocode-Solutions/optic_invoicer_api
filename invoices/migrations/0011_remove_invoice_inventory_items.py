# Generated by Django 4.2 on 2023-11-25 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0010_remove_invoice_items_invoiceitem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='inventory_items',
        ),
    ]