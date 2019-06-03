from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Brand(models.Model):
	brand_name= models.CharField(max_length=100)
	description= models.TextField()
	#owner = models.ForeignKey('auth.User', related_name='brand', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('brand_name',)
	def save(self, *args, **kwargs):
		super(Brand, self).save(*args, **kwargs)

class Person(models.Model):
	person_type=models.CharField(max_length=100)
	first_name=models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	description= models.TextField()
	company=models.CharField(max_length=100)
	phone=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	fax=models.TextField(max_length=100)
	email=models.CharField(max_length=100)
	website=models.CharField(max_length=100)
	#group_id=models.IntegerField()
	group_id = models.ForeignKey('Group', related_name='person_id', on_delete=models.CASCADE)
	code=models.CharField(max_length=100)
	date_of_birth=models.DateField()
	gender=models.CharField(max_length=100)
	#owner = models.ForeignKey('auth.User', related_name='person', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('person_type',)
	def save(self, *args, **kwargs):
		super(Person, self).save(*args, **kwargs)

class Address(models.Model):
	road=models.CharField(max_length=100)
	street=models.CharField(max_length=100)
	suburb=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	post_code=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	country=models.CharField(max_length=100)
	#person_id=models.IntegerField()
	person_id = models.ForeignKey('Person', related_name='address_id', on_delete=models.CASCADE)
	#owner = models.ForeignKey('auth.User', related_name='address', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('road',)
	def save(self, *args, **kwargs):
		super(Address, self).save(*args, **kwargs)

class Group(models.Model):
	group_name=models.CharField(max_length=100)
	create_date=models.DateTimeField(auto_now_add=True)
	no_customer=models.IntegerField()
	country=models.CharField(max_length=100)
	#owner = models.ForeignKey('auth.User', related_name='group', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('group_name',)
	def save(self, *args, **kwargs):
		super(Group, self).save(*args, **kwargs)

class Product(models.Model):
	product_name=models.CharField(max_length=100)
	#type_id=models.IntegerField()
	type_id = models.ForeignKey('Type', related_name='product_id', on_delete=models.CASCADE)
	product_image=models.ImageField(max_length=254)
	description=models.TextField(max_length=100)
	quality=models.CharField(max_length=100)
	#brand_id=models.IntegerField()
	brand_id = models.ForeignKey('Brand', related_name='product_id', on_delete=models.CASCADE)
	#tag_id=models.IntegerField()
	tag_id = models.ForeignKey('Tags', related_name='product_id', on_delete=models.CASCADE)
	#person_id=models.IntegerField()
	person_id = models.ForeignKey('Person', related_name='product_id', on_delete=models.CASCADE)
	product_price=models.IntegerField()
	supplier_price=models.IntegerField()
	create_date=models.DateField()
	#owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('product_name',)
	def save(self, *args, **kwargs):
		super(Product, self).save(*args, **kwargs)

class Tags(models.Model):
	tags_name=models.CharField(max_length=100)
	#owner = models.ForeignKey('auth.User', related_name='tags', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering=('tags_name',)
	def save(self, *args, **kwargs):
		super(Tags, self).save(*args, **kwargs)

class Type(models.Model):
	type_name=models.CharField(max_length=100)
	#owner = models.ForeignKey('auth.User', related_name='type', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta():
		ordering=('type_name',)
	def save(self, *args, **kwargs):
		super(Type, self).save(*args, **kwargs)

# Sale Table
class Sales(models.Model):
	#person_id = models.IntegerField()
	person_id = models.ForeignKey('Person', related_name='sales_id', on_delete=models.CASCADE)
	transaction_date = models.DateTimeField(auto_now_add=True)
	amount_paid = models.IntegerField()
	paid = models.IntegerField()
	#owner = models.ForeignKey('auth.User', related_name='sales', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('person_id',)
	def save(self, *args, **kwargs):
		super(Sales, self).save(*args, **kwargs)

class SaleDetails(models.Model):
	#sales_id = models.IntegerField()
	sales_id = models.ForeignKey('Sales', related_name='saledetails_id', on_delete=models.CASCADE)
	#product_id = models.IntegerField()
	product_id = models.ForeignKey('Product', related_name='saledetails_id', on_delete=models.CASCADE)
	quantity = models.IntegerField()
	product_price = models.IntegerField()
	sub_total = models.IntegerField()
	#owner = models.ForeignKey('auth.User', related_name='saledetails', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('product_id',)
	def save(self, *args, **kwargs):
		super(SaleDetails, self).save(*args, **kwargs)

class Register(models.Model):
	status = models.CharField(max_length=100)
	opening_balance = models.IntegerField()
	note = models.CharField(max_length=200)
	opening_time = models.DateTimeField(auto_now_add=True)
	closing_time = models.DateTimeField(auto_now_add=True)
	expected = models.IntegerField()
	counted = models.IntegerField()
	difference = models.IntegerField()
	#sales_id = models.IntegerField()
	sales_id = models.ForeignKey('Sales', related_name='register_id', on_delete=models.CASCADE)
	cash_payment_received = models.IntegerField()
	store_credit = models.IntegerField()
	total = models.IntegerField()
	closing_note = models.CharField(max_length=200)
	#owner = models.ForeignKey('auth.User', related_name='register', on_delete=models.CASCADE)
	#highlighted = models.TextField()
	class Meta:
		ordering = ('status',)
	def save(self, *args, **kwargs):
		super(Register, self).save(*args, **kwargs)


