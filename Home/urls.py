from django.urls import path, include
from . import views
from .serializerviews import ProductAPIView, CategoryAPIView, OrderItemAPIView, OrderAPIView
from rest_framework import routers

app_name = 'Home'

router = routers.DefaultRouter()
router.register('products', viewset=ProductAPIView)
router.register('categories', viewset=CategoryAPIView)
router.register('order_items', viewset=OrderItemAPIView)
router.register('orders', viewset=OrderAPIView)


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('api/', include(router.urls)),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

]
