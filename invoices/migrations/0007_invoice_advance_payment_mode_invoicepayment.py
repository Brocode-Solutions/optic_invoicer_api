# Generated by Django 4.2 on 2023-11-11 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0005_payment_subscription'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoices', '0006_alter_invoice_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='advance_payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Online', 'Online'), ('Others', 'Others')], default='Cash', max_length=10),
        ),
        migrations.CreateModel(
            name='InvoicePayment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(blank=True, max_length=255, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_type', models.CharField(choices=[('Advance', 'Advance'), ('General', 'General'), ('Return', 'Return'), ('Others', 'Others')], default='General', max_length=10)),
                ('payment_mode', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Online', 'Online'), ('Others', 'Others')], default='Cash', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice_payment_created', to=settings.AUTH_USER_MODEL)),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice_payment', to='invoices.invoice')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoice_payment_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
