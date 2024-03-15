from django.http import JsonResponse
from django.shortcuts import render, redirect
from rarechild.models import Category, Vendor, Product, productImages, Order, OrderItem, ProductReview, \
    wishlist, Address, ProductVariation
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

import django.contrib.auth.models
from django.contrib import messages


# Create your views here.

def index(request):
    products = Product.objects.all()[:5]
    hot_products = Product.objects.all()[6:11]
    context = {
        "products": products,
        "hot_products": hot_products
    }
    return render(request, 'index.html', context)


def shop(request):
    categories = Category.objects.all()
    p = Paginator(Product.objects.all().order_by("price"), 6)

    page = request.GET.get('page')

    products = p.get_page(page)

    context = {
        "categories": categories,
        "products": products
    }
    return render(request, 'shop.html', context)


def category_product_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)

    context = {
        'category': category,
        "products": products
    }
    return render(request, 'shop.html', context)


def product_view(request, product_id):
    product = get_object_or_404(Product, pid=product_id)  # Assumes product_id is a UUID string
    p_image = product.p_images.all()
    rel_products = Product.objects.filter(category=product.category).exclude(pid=product_id)[:4]  # Limit to 4
    product_variations = ProductVariation.objects.filter(product__pid=product_id)

    context = {'product': product, 'p_image': p_image, 'rel_products': rel_products,
               'product_variations': product_variations}
    return render(request, 'shop-details.html', context)


# ... other imports

from django.shortcuts import get_object_or_404, redirect


def _get_or_create_active_cart(request):
    if request.user.is_authenticated:
        cart, created = CartOrder.objects.get_or_create(
            user=request.user,
            order_status='active',  # Ensure we get or create an active cart
            defaults={'order_status': 'active'}
        )
    else:
        # ... session-based cart logic ...
        return cart


from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pid=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id]['quantity'] += quantity
        else:
            cart[product_id] = {'quantity': quantity}

        request.session['cart'] = cart

        # Use redirect for success
        return redirect('product_view', product_id=product_id)  # Or redirect to cart view
    else:
        # If not a POST request, handle this case (e.g., redirect to the product page)
        pass
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pid=product_id)

    # Logic for logged-in users
    if request.user.is_authenticated:
        cart = CartOrder.objects.get(user=request.user)
    # Logic for non-logged-in users
    else:
        if not request.session.session_key:
            request.session.create()
        cart = CartOrder.objects.get(session_key=request.session.session_key)

    cart_item = CartorderItems.objects.get(order=cart, product=product)
    cart_item.delete()

    return redirect('cart')


def _get_or_create_cart(request):
    """Helper function to retrieve or create a cart (assumes active carts)"""
    if request.user.is_authenticated:
        cart, created = CartOrder.objects.get_or_create(
            user=request.user, order_status='active'
        )
    else:
        if not request.session.session_key:
            request.session.create()
        cart, created = CartOrder.objects.get_or_create(
            session_key=request.session.session_key, order_status='active'
        )
    return cart, created


def cart(request):
    if request.user.is_authenticated:
        User = request.user
        order, created = Order.objects.get_or_create(user=User, order_status=False)
        cart_items = order.orderitem_set.all()
    else:
        cart_items = []
    context = {'cart_items': cart_items}
    return render(request, 'shopping-cart.html', context)


def update_cart_item(request, item_id):
    if request.method == "POST":
        item = get_object_or_404(CartorderItems, id=item_id)
        new_quantity = int(request.POST.get('quantity'))
        item.quantity = new_quantity
        item.save()
        return JsonResponse({'success': True})  # Return success response
    else:
        return JsonResponse({'success': False})


from urllib.parse import unquote


def checkout(request):
    cart_obj = _get_or_create_active_cart(request)
    cart_items = CartorderItems.objects.filter(order=cart_obj)

    # ... Calculate cart total (if you haven't done this already in the cart view)

    # Create the CartOrder object
    cart_order = CartOrder.objects.create(
        user=request.user if request.user.is_authenticated else None,
        session_key=request.session.session_key if not request.user.is_authenticated else None,
        # ... other CartOrder fields
    )

    # You might need to update the CartorderItems if necessary, e.g.,
    # CartorderItems.objects.filter(order=cart_obj).update(order=cart_order)

    # ... Render your checkout template
    context = {
        'cart_items': cart_items,
        'cart_total': cart_total
    }
    return render(request, 'checkout.html', context)


def blog(request):
    return render(request, 'blog.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def contact(request):
    return render(request, 'contact.html')
