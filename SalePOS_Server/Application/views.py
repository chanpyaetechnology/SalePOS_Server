from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from Application.models import Brand, Person, Product, Address, Group, Tags, Type, Sales, SaleDetails, Register
from Application.serializers import BrandSerializer, PersonSerializer, ProductSerializer, AddressSerializer, GroupSerializer, TagsSerializer, TypeSerializer, SalesSerializer, SaleDetailsSerializer, RegisterSerializer, UserSerializer
from Application.permissions import IsOwnerOrReadOnly

class BrandViewSet(viewsets.ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		brand = self.get_object()
		return Response(brand.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class PersonViewSet(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		person = self.get_object()
		return Response(person.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		product = self.get_object()
		return Response(product.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class AddressViewSet(viewsets.ModelViewSet):
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		address = self.get_object()
		return Response(address.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class GroupViewSet(viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		group = self.get_object()
		return Response(group.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class TagsViewSet(viewsets.ModelViewSet):
	queryset = Tags.objects.all()
	serializer_class = TagsSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		tags = self.get_object()
		return Response(tags.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class TypeViewSet(viewsets.ModelViewSet):
	queryset = Type.objects.all()
	serializer_class = TypeSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		type = self.get_object()
		return Response(type.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

# Sale Views
class SalesViewSet(viewsets.ModelViewSet):
	queryset = Sales.objects.all()
	serializer_class = SalesSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		sales = self.get_object()
		return Response(sales.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class SaleDetailsViewSet(viewsets.ModelViewSet):
	queryset = SaleDetails.objects.all()
	serializer_class = SaleDetailsSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		saledetails = self.get_object()
		return Response(saledetails.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

class RegisterViewSet(viewsets.ModelViewSet):
	queryset = Register.objects.all()
	serializer_class = RegisterSerializer
	# For Authentication
	'''
	permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )
	@detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
	def highlight(self, request, *args, **kwargs): 
		register = self.get_object()
		return Response(register.highlighted)
	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
	'''

# For Authentication
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer