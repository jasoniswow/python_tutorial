# This is an example of a class called "Tab"


class Tab:

    menu = {
            'wine': 5,
            'beer': 3,
            'soft': 2,
            'chicken': 10,
            'beef': 15,
            'veggie': 12,
            'desert': 6
            }

    def __init__(self):
        self.total = 0
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.total += self.menu[item]

    def print_bill(self,tax,tip):
        tax = (tax/100) * self.total
        tip = (tip/100) * self.total
        total =  self.total + tax + tip
        for item in self.items:
            print (f'{item:20} ${self.menu[item]}')
        print (f'{"Total":20} ${total:.2f}')


