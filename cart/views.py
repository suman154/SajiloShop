from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()  # Call get_prods as a method
    return render(request, 'cart_summary.html', {'cart_products': cart_products})




def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        
        # Get cart quantity
        cart_quantity = cart.__len__()
        
        # Return JSON response with cart quantity
        response = JsonResponse({'qty': cart_quantity})
        return response
    
    # If the request method is not POST or the action is not 'post', return bad request response
    return JsonResponse({'error': 'Invalid request'}, status=400)

def cart_update(request):
    pass

def cart_delete(request):
    pass
