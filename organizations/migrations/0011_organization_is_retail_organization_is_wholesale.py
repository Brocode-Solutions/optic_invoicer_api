# Generated by Django 4.2 on 2024-06-05 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0010_subscription_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='is_retail',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='is_wholesale',
            field=models.BooleanField(default=False),
        ),
    ]
