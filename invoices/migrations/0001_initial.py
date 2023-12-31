# Generated by Django 4.2 on 2023-09-27 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('organizations', '0002_organization_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0002_prescription_left_add_prescription_left_ipd_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('invoice_number', models.CharField(max_length=255, unique=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('advance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('Created', 'Created'), ('Advanced', 'Advanced'), ('Paid', 'Paid'), ('Delivered', 'Delivered'), ('Scrapped', 'Scrapped')], default='Created', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices_created', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoices', to='customers.customer')),
                ('frame', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='frames', to='inventory.inventory')),
                ('lens', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lenses', to='inventory.inventory')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.organization')),
                ('prescription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.prescription')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invoices_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
