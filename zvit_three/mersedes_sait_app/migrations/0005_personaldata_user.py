# Generated by Django 5.1.1 on 2024-10-24 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersedes_sait_app', '0004_alter_product_car_model_alter_product_car_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('payment_method', models.CharField(choices=[('hotivca', 'Hotivca'), ('paypal', 'PayPal'), ('mono', 'Monobank'), ('pumb', 'Pumb Bank'), ('privat', 'Privat Bank'), ('visa', 'Visa'), ('master', 'MasterCard')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
