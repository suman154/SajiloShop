from store.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session 

        # Get the current session key if it already exists
        cart = self.session.get('session_key')

        # If the user is new, then no session key. Create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # Cart is available on all pages of website
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            self.session.modified = True



    def total(self):
        # Get product IDs
        product_ids = self.cart.keys()
        # Fetch products from the database
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        # Start counting from 0
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total += product.sale_price * value
                    else:
                        total += product.price * value
        return total


    def __len__(self):
        return len(self.cart)



    def get_prods(self):
        # Get ids from cart
        product_ids = self.cart.keys()
        # Use ids to lookup products in database model
        products = Product.objects.filter(id__in=product_ids)
        # Return those looked up
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities


    def cart_update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        # Get cart
        ourcart = self.cart
        # update dictionary/cart
        ourcart[product_id] = product_qty



        self.session.modified = True

        thing  = self.cart
        return thing
    

    def delete(self, product):
        product_id = str(product)
        # delete from dict/cart 
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True




