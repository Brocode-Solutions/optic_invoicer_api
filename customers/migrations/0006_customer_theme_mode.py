# Generated by Django 4.2 on 2023-10-03 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_email_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='theme_mode',
            field=models.CharField(choices=[('L', 'Light'), ('D', 'Dark'), ('S', 'System')], default='S', max_length=1),
        ),
    ]
