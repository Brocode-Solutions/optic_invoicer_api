# Generated by Django 4.2 on 2023-11-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0008_invoicepayment_remarks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='tax_percentage',
            field=models.DecimalField(blank=True, decimal_places=2, default=5, max_digits=10, null=True),
        ),
    ]
