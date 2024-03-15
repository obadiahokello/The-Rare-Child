from django.contrib import admin
from userauths.models import User
from rarechild.models import Category, Vendor, Product, productImages, Order, OrderItem, ProductReview, \
    wishlist, Address, Color, Size, ProductVariation


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


class ProductImagesAdmin(admin.TabularInline):
    model = productImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'price', 'product_status']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']


class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'order_status', 'order_date', 'paid_status' ]


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'quantity', 'add_date', 'product']


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating']


class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']


class AddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'status']


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(productImages)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ProductVariation)
