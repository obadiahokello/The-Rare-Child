# Generated by Django 4.2.4 on 2024-03-07 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rarechild', '0022_cartorder_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorderitems',
            name='qty',
        ),
    ]
