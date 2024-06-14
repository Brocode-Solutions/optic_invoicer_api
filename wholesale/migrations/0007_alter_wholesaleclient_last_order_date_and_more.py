# Generated by Django 4.2 on 2024-06-06 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0006_alter_wholesaleorder_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesaleclient',
            name='last_order_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wholesaleclient',
            name='last_payment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wholesaleclient',
            name='total_credit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='wholesaleclient',
            name='total_orders',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wholesaleclient',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
