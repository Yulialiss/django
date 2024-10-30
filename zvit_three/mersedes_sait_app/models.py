from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.TextField(max_length=100, default='default_value')
    description = models.TextField(null=True, blank=True)
    car_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name

class PersonalData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('hotivca', 'Hotivca'),
            ('paypal', 'PayPal'),
            ('mono', 'Monobank'),
            ('pumb', 'Pumb Bank'),
            ('privat', 'Privat Bank'),
            ('visa', 'Visa'),
            ('master', 'MasterCard')
        ]
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

