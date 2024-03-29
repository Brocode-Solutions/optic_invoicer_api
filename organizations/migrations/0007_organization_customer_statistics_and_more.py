# Generated by Django 4.2.4 on 2024-01-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_organization_total_customers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='customer_statistics',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='inventory_statistics',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='invoice_statistics',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='prescription_statistics',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
