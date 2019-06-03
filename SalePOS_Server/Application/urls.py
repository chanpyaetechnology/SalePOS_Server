from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from Application import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Brand', views.BrandViewSet)
router.register(r'Person', views.PersonViewSet)
router.register(r'Product', views.ProductViewSet)
router.register(r'Address', views.AddressViewSet)
router.register(r'Group', views.GroupViewSet)
router.register(r'Tags', views.TagsViewSet)
router.register(r'Type', views.TypeViewSet)
router.register(r'Sales', views.SalesViewSet)
router.register(r'SaleDetails', views.SaleDetailsViewSet)
router.register(r'Register', views.RegisterViewSet)
router.register(r'Users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls))
]

