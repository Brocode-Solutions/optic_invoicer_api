# Generated by Django 4.2 on 2024-06-05 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_organization_is_retail_organization_is_wholesale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wholesale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WholeSaleClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('country', models.CharField(max_length=100)),
                ('tax_number', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('contact_person', models.CharField(max_length=100)),
                ('contact_person_phone', models.CharField(max_length=100)),
                ('contact_person_email', models.EmailField(max_length=254)),
                ('contact_person_designation', models.CharField(max_length=100)),
                ('total_orders', models.IntegerField()),
                ('total_credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_payment_date', models.DateField()),
                ('last_order_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wholesale_client_created', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wholesale_client', to='organizations.organization')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wholesale_client_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
