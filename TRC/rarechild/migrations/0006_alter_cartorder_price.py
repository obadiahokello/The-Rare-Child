# Generated by Django 4.2.4 on 2024-02-29 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rarechild', '0005_alter_product_old_price_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='price',
            field=models.DecimalField(decimal_places=2, default='1.99', max_digits=9),
        ),
    ]
