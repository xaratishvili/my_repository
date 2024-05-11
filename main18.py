class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan}"


class House:
    def __init__(self, ID, price, owner=None, status="For Sale"):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = status

    def sell(self, buyer, loan_amount=None):
        if loan_amount is None:
            buyer.deposit -= self.price
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Sold"
            print(f"The house with ID {self.ID} has been sold to {buyer.name}.")
        else:
            buyer.deposit -= self.price
            buyer.loan += loan_amount
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "Sold with Loan"
            self.owner.loan += loan_amount
            print(f"The house with ID {self.ID} has been sold to {buyer.name} with a loan of {loan_amount}.")
            print(f"{buyer.name}'s loan amount is now {buyer.loan}.")


owner = Person("Owner")
buyer = Person("Buyer")
house = House("888", 200000, owner)

print("Initial Information:")
print(owner)
print(buyer)
print(house.owner)

house.sell(buyer)
house.sell(buyer, 50000)

print("\nUpdated Information:")
print(owner)
print(buyer)
print(house.owner)
