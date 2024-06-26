# Generated by Django 4.2 on 2024-06-06 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wholesale', '0005_remove_wholesaleinventory_preferred_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesaleorder',
            name='order_status',
            field=models.CharField(choices=[(1, 'Draft'), (2, 'Confirmed'), (3, 'Delivered'), (4, 'Cancelled'), (3, 'Paid')], default=1, max_length=15),
        ),
        migrations.AlterField(
            model_name='wholesaleorder',
            name='payment_status',
            field=models.CharField(choices=[(1, 'Created'), (2, 'Due'), (3, 'Overdue'), (4, 'Paid'), (3, 'Cancelled')], default=1, max_length=15),
        ),
    ]
