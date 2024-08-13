from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

# Create cuttomer profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default='', blank=True)
    last_name = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    email = models.EmailField(default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    state = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    zip = models.CharField(max_length=10, default='', blank=True)
    image = models.ImageField(upload_to='uploads/profile/', default='uploads/profile/default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'



# Create a user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile =Profile.objects.create(user=instance)
        user_profile.save()


# Automate the profile creation
post_save.connect(create_profile, sender=User)





class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
    class meta:
        verbose_name_plural = 'categories'


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)



    def __str__(self):
        return f'{self.first_name} {self.last_name}'



class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=-8, decimal_places=2, max_digits=6)
    category =models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True)
    image = models.ImageField(upload_to='uploads/product/')

    # Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)


    def __str__(self):
        return self.name



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=-1)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=20)
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product