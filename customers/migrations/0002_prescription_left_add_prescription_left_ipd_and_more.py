# Generated by Django 4.2 on 2023-09-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='left_add',
            field=models.FloatField(blank=True, choices=[(0.0, '0.00'), (0.25, '0.25'), (0.5, '0.50'), (0.75, '0.75'), (1.0, '1.00'), (1.25, '1.25'), (1.5, '1.50'), (1.75, '1.75'), (2.0, '2.00'), (2.25, '2.25'), (2.5, '2.50'), (2.75, '2.75'), (3.0, '3.00'), (3.25, '3.25'), (3.5, '3.50'), (3.75, '3.75')], null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='left_ipd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='left_prism',
            field=models.FloatField(blank=True, choices=[(0.0, '0.00'), (0.25, '0.25'), (0.5, '0.50'), (0.75, '0.75'), (1.0, '1.00'), (1.25, '1.25'), (1.5, '1.50'), (1.75, '1.75'), (2.0, '2.00'), (2.25, '2.25'), (2.5, '2.50'), (2.75, '2.75'), (3.0, '3.00'), (3.25, '3.25'), (3.5, '3.50'), (3.75, '3.75'), (4.0, '4.00'), (4.25, '4.25'), (4.5, '4.50'), (4.75, '4.75'), (5.0, '5.00'), (5.25, '5.25'), (5.5, '5.50'), (5.75, '5.75'), (6.0, '6.00'), (6.25, '6.25'), (6.5, '6.50'), (6.75, '6.75'), (7.0, '7.00'), (7.25, '7.25'), (7.5, '7.50'), (7.75, '7.75'), (8.0, '8.00'), (8.25, '8.25'), (8.5, '8.50'), (8.75, '8.75'), (9.0, '9.00'), (9.25, '9.25'), (9.5, '9.50'), (9.75, '9.75')], null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='right_add',
            field=models.FloatField(blank=True, choices=[(0.0, '0.00'), (0.25, '0.25'), (0.5, '0.50'), (0.75, '0.75'), (1.0, '1.00'), (1.25, '1.25'), (1.5, '1.50'), (1.75, '1.75'), (2.0, '2.00'), (2.25, '2.25'), (2.5, '2.50'), (2.75, '2.75'), (3.0, '3.00'), (3.25, '3.25'), (3.5, '3.50'), (3.75, '3.75')], null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='right_ipd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prescription',
            name='right_prism',
            field=models.FloatField(blank=True, choices=[(0.0, '0.00'), (0.25, '0.25'), (0.5, '0.50'), (0.75, '0.75'), (1.0, '1.00'), (1.25, '1.25'), (1.5, '1.50'), (1.75, '1.75'), (2.0, '2.00'), (2.25, '2.25'), (2.5, '2.50'), (2.75, '2.75'), (3.0, '3.00'), (3.25, '3.25'), (3.5, '3.50'), (3.75, '3.75'), (4.0, '4.00'), (4.25, '4.25'), (4.5, '4.50'), (4.75, '4.75'), (5.0, '5.00'), (5.25, '5.25'), (5.5, '5.50'), (5.75, '5.75'), (6.0, '6.00'), (6.25, '6.25'), (6.5, '6.50'), (6.75, '6.75'), (7.0, '7.00'), (7.25, '7.25'), (7.5, '7.50'), (7.75, '7.75'), (8.0, '8.00'), (8.25, '8.25'), (8.5, '8.50'), (8.75, '8.75'), (9.0, '9.00'), (9.25, '9.25'), (9.5, '9.50'), (9.75, '9.75')], null=True),
        ),
    ]
