# Generated by Django 4.0.3 on 2022-04-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ethereum', '0011_alter_ethbalance_eth_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethbalance',
            name='eth_balance',
            field=models.DecimalField(blank=True, decimal_places=7, default=1.7e-06, max_digits=9, null=True),
        ),
    ]
