# Generated by Django 5.1.1 on 2024-10-25 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersedes_sait_app', '0015_alter_product_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='car_model',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
