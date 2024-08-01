# Generated by Django 3.2.12 on 2024-07-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_packaging', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='packaging_group',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='packaging_group',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Packaging_Group_Item',
        ),
        migrations.DeleteModel(
            name='Packaging_Item',
        ),
    ]
