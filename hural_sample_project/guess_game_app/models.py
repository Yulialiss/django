from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Ronk(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    page_count = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country = models.CharField(max_length=100)
    make_name = models.ForeignKey(Author, on_delete=models.CASCADE)
