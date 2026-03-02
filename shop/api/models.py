from django.db import models

# Create your models here.
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  stock = models.IntegerField()
  
  def __str__(self):
    return f"{self.name}"

class Vendor(models.Model):
  name = models.CharField(max_length=30, unique=True, blank=False, null=False)
  products = models.ManyToManyField(Product, related_name='vendors')
  bio = models.TextField()

  def __str__(self):
    return f"{self.name}"

class Review(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
  vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='reviews')
  rating = models.IntegerField()
  comment = models.TextField()

  def __str__(self):
    return f"{self.product} - {self.vendor} - {self.rating}"
