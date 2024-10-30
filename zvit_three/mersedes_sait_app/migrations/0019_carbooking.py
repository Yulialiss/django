# Generated by Django 5.1.1 on 2024-10-27 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersedes_sait_app', '0018_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('payment_method', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
