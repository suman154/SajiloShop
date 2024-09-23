from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Category, Customer, Product, Order
from datetime import datetime

# Test cases for models

class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def test_profile_creation(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user.username, 'testuser')
        self.assertEqual(profile.phone, '')  # Default value
        self.assertEqual(profile.city, '')  # Default value

class CategoryModelTest(TestCase):

    def test_category_creation(self):
        category = Category.objects.create(name="Electronics")
        self.assertEqual(str(category), "Electronics")


class CustomerModelTest(TestCase):

    def test_customer_creation(self):
        customer = Customer.objects.create(first_name="John", last_name="Doe", phone="1234567890", email="john@example.com", password="password")
        self.assertEqual(str(customer), "John Doe")


class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

    def test_product_creation(self):
        product = Product.objects.create(
            name="Laptop",
            price=500.00,
            category=self.category,
            description="A gaming laptop",
            image="uploads/product/laptop.jpg",
            is_sale=True,
            sale_price=450.00
        )
        self.assertEqual(str(product), "Laptop")
        self.assertEqual(product.is_sale, True)
        self.assertEqual(product.sale_price, 450.00)


class OrderModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Electronics")
        self.product = Product.objects.create(
            name="Laptop",
            price=500.00,
            category=self.category,
            description="A gaming laptop",
            image="uploads/product/laptop.jpg"
        )
        self.customer = Customer.objects.create(first_name="John", last_name="Doe", phone="1234567890", email="john@example.com", password="password")

    def test_order_creation(self):
        order = Order.objects.create(
            product=self.product,
            customer=self.customer,
            quantity=2,
            address="123 Main St",
            phone="1234567890",
            date=datetime.today(),
            status=True
        )
        self.assertEqual(order.product.name, "Laptop")
        self.assertEqual(order.customer.first_name, "John")
        self.assertEqual(order.quantity, 2)
        self.assertEqual(order.status, True)
        self.assertEqual(str(order.product), "Laptop")
