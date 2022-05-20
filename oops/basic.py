import csv

# class Item:
#     def calculate_total_price(self, a, b):
#         return a*b;

# item1 = Item()
# item1.name = "Laptop"
# item1.price = 15000
# item1.qty = 5
# print(item1.calculate_total_price(item1.price, item1.qty))


# item2 = Item()
# item2.name = "Phone"
# item2.price = 10000
# item2.qty = 2
# print(item2.calculate_total_price(item2.price, item2.qty))



class Item:
    pay_rate = 0.8      # The pay after 20% disocunt
    all = []

    def __init__(self, name: str, price: float, qty = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than zero!!!"
        assert qty >= 0, f"Quantity {qty} is not greater than zero!!!"

        # Assign to self object
        self.name = name
        self.price = price
        self.qty = qty

        # Acitons to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.qty
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return ""
    
    @classmethod                                # DECORATOR
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)          # Read as Dictionary
            item = list(reader)

        for i in item:
            Item(
                name = i.get('name'),
                price = int(i.get('price')),
                qty = int(i.get('qty'))
            )

    def __repr__(self):                         # Represents objects as Strings
        return f"Item({self.name}, {self.price}, {self.qty})"



item1 = Item("Laptop", 15000, 5)
item2 = Item("Phone", 8000, 3)
item3 = Item("Curtain", 500, 2)
item4 = Item("Mouse", 1000, 9)
item5 = Item("Gamepad", 2000, 7)

Item.instantiate_from_csv()

for i in Item.all:
    print(f"{i.name}\t\t{i.price}\t{i.qty}")

print(Item.all)


print(f"Item: {item1.name}\tQuantity: {item1.qty}\tPrice: {item1.price}\nTotal Cost: {item1.calculate_total_price()}\tDiscounted Price: {item1.apply_discount()}{int(item1.calculate_total_price())}")
