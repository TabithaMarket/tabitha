# Generated by Django 4.2.13 on 2024-05-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_productpage_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productpage',
            name='SKU',
            field=models.CharField(default='vPzmER0w0aV', max_length=500),
        ),
    ]
