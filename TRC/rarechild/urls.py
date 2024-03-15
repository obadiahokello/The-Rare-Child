from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('shop', views.shop, name='shop'),
path('cart/remove/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('blog', views.blog, name='blog'),
    path('blogdetails', views.blogdetails, name='blog-details'),
    path('contact', views.contact, name='contact'),
    path('update-cart-item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('shop/<str:cid>', views.category_product_view, name='shop1'),
    path('product/<str:product_id>', views.product_view, name='product-detail'),
    path('add-to-cart/<str:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product/<str:product_id>/', views.product_view, name='product_view')
]
