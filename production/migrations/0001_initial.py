# Generated by Django 3.2.12 on 2024-07-29 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_packaging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('default_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('default_width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('default_height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('default_length', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('attributes', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('attributes', models.JSONField(default=dict)),
                ('preduced', models.BooleanField(default=False)),
                ('selled', models.BooleanField(default=False)),
                ('raw_material_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('online_shop', models.JSONField(default=dict)),
                ('preducing_date', models.DateField()),
                ('first_offer_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('package_S2I', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_S2I', to='product_packaging.package_s2i')),
                ('packaging_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='packaging_group', to='product_packaging.packaging_group')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='production.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='production.product_category'),
        ),
    ]