class CheckoutSystem:
    def __init__(self):
        self.cart = []

    def update_cart(self, detected_items):
        for item in detected_items:
            if item not in self.cart:
                self.cart.append(item)
                print(f"Added {item} to the cart.")

    def process_payment(self):
        print("Processing payment for the following items:")
        for item in self.cart:
            print(f"- {item}")

        # Placeholder: Payment process (e.g., connecting to a payment gateway)
        print("Payment successful!")

