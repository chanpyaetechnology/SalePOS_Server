from django.contrib.auth.models import User
from rest_framework import serializers
from Application.models import Brand, Person, Product, Address, Group, Tags, Type, Sales, SaleDetails, Register

#class BrandSerializer(serializers.HyperlinkedModelSerializer):
class BrandSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='brand-highlight', format='html')
	product_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model=Brand
		#fields =('url', 'id', 'highlight', 'owner', 'brand_name', 'description', 'product_id')
		fields = ('id', 'brand_name', 'description', 'product_id')

#class PersonSerializer(serializers.HyperlinkedModelSerializer):
class PersonSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='person-highlight', format='html')
	product_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	sales_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	address_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model=Person
		#fields =('url','id', 'highlight', 'owner', 'person_type', 'first_name', 'last_name', 'description', 'company', 'phone', 'mobile', 'fax', 'email', 'website', 'group_id', 'code', 'date_of_birth', 'gender', 'product_id', 'sales_id', 'address_id')
		fields = ('id', 'person_type', 'first_name', 'last_name', 'description', 'company', 'phone', 'mobile', 'fax', 'email', 'website', 'group_id', 'code', 'date_of_birth', 'gender', 'product_id', 'sales_id', 'address_id')

#class ProductSerializer(serializers.HyperlinkedModelSerializer):
class ProductSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')
	saledetails_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model=Product
		#fields =( 'url', 'id', 'highlight', 'owner', 'product_name', 'type_id', 'product_image', 'description', 'quality', 'brand_id', 'tag_id', 'person_id', 'product_price', 'supplier_price', 'create_date', 'saledetails_id')
		fields = ('id', 'product_name', 'type_id', 'product_name', 'description', 'quality', 'brand_id', 'tag_id', 'person_id', 'product_price', 'supplier_price', 'create_date', 'saledetails_id')

#class AddressSerializer(serializers.HyperlinkedModelSerializer):
class AddressSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='address-highlight', format='html')
	class Meta:
		model=Address
		#fields =('url', 'id', 'highlight', 'owner', 'road', 'street', 'suburb', 'city', 'post_code', 'state', 'country', 'person_id')
		fields = ('id', 'road', 'street', 'suburb', 'city', 'post_code', 'state', 'country', 'person_id')

#class GroupSerializer(serializers.HyperlinkedModelSerializer):
class GroupSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='group-highlight', format='html')
	person_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model=Group
		#fields =('url', 'id', 'highlight', 'owner', 'group_name', 'no_customer', 'country', 'person_id')
		fields = ('id', 'group_name', 'no_customer', 'country', 'person_id')

#class TagsSerializer(serializers.HyperlinkedModelSerializer):
class TagsSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='tags-highlight', format='html')
	product_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model=Tags
		#fields =('url', 'id', 'highlight', 'owner', 'tags_name', 'product_id')
		fields = ('id', 'tags_name', 'product_id')

#class TypeSerializer(serializers.HyperlinkedModelSerializer):
class TypeSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='type-highlight', format='html')
	product_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model=Type
		#fields =( 'url', 'id', 'highlight', 'owner', 'type_name', 'product_id')
		fields = ('id', 'type_name', 'product_id')

# Sale Serializer
#class SalesSerializer(serializers.HyperlinkedModelSerializer):
class SalesSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='sales-highlight', format='html')
	register_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	saledetails_id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Sales
		#fields = ('url', 'id', 'highlight', 'owner', 'person_id', 'transaction_date', 'amount_paid', 'paid', 'register_id', 'saledetails_id')
		fields = ('id', 'person_id', 'transaction_date', 'amount_paid', 'paid', 'register_id', 'saledetails_id')

#class SaleDetailsSerializer(serializers.HyperlinkedModelSerializer):
class SaleDetailsSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='saledetails-highlight', format='html')
	class Meta:
		model = SaleDetails
		#fields = ('url', 'id', 'highlight', 'owner', 'sales_id', 'product_id', 'quantity', 'product_price', 'sub_total')
		fields = ('id', 'sales_id', 'product_id', 'quantity', 'product_price', 'sub_total')

#class RegisterSerializer(serializers.HyperlinkedModelSerializer):
class RegisterSerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.username')
	#highlight = serializers.HyperlinkedIdentityField(view_name='register-highlight', format='html')
	class Meta:
		model = Register
		#fields = ('url', 'id', 'highlight', 'owner', 'status', 'opening_balance', 'note', 'expected', 'counted', 'difference', 'sales_id', 'cash_payment_received', 'store_credit', 'total', 'closing_note')
		fields = ('id', 'status', 'opening_balance', 'note', 'expected', 'counted', 'difference', 'sales_id', 'cash_payment_received', 'store_credit', 'total', 'closing_note')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'password')

# For Authentication
'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
	brand = serializers.HyperlinkedRelatedField(many=True, view_name='brand-detail', read_only=True)
	person = serializers.HyperlinkedRelatedField(many=True, view_name='person-detail', read_only=True)
	address = serializers.HyperlinkedRelatedField(many=True, view_name='address-detail', read_only=True)
	group = serializers.HyperlinkedRelatedField(many=True, view_name='group-detail', read_only=True)
	product = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)
	tags = serializers.HyperlinkedRelatedField(many=True, view_name='tags-detail', read_only=True)
	type = serializers.HyperlinkedRelatedField(many=True, view_name='type-detail', read_only=True)
	sales = serializers.HyperlinkedRelatedField(many=True, view_name='sales-detail', read_only=True)
	saledetails = serializers.HyperlinkedRelatedField(many=True, view_name='saledetails-detail', read_only=True)
	register = serializers.HyperlinkedRelatedField(many=True, view_name='register-detail', read_only=True)
	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'brand', 'person', 'address', 'group', 'product', 'tags', 'type', 'sales', 'saledetails','register')
'''
