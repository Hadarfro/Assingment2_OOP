from Posts import Posts


class SalePost(Posts):

    def __init__(self, user, description, price, location):
        super().__init__(user)
        self.description = description
        self.price = price
        self.location = location
        self.available = True

    def discount(self, percentage, password):
        if self._user.password() == password:
            if 0 <= percentage <= 100:
                discount_amount = self.price * (percentage / 100)
                discounted_price = self.price - discount_amount
                self.price = discounted_price
                print(f"Discount on {self._user.username()} product! the new price is: {self.price}")
            else:
                print("Invalid discount percentage. It should be between 0 and 100.")

    def sold(self, password):
        if self._user.password == password:
            self.available = False
            self.print_info()

    def print_info(self):
        if self.available:
            text = "For sale!"
        else:
            text = "sold!"
        print(f"{self._user.username()} posted a product for sale:")
        print(f"{text} {self.description}, price: {self.price}, pickup from: {self.location}")
        print()
