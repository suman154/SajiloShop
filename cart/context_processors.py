from .cart import Cart

# Create context processor so our cart work on the all pages od website 
def cart(request):
    # Return the default data from our cart 
    return {'cart': Cart(request)}