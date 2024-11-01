# Generated by Django 5.1.1 on 2024-10-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mersedes_sait_app', '0002_alter_product_description_alter_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='car_model',
            field=models.CharField(default='Невідома модель', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='car_type',
            field=models.CharField(default='Невідомий тип', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='Невідомий тип', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
