class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    def __repr__(self):
        return '{name} is available from {start_time} to {end_time}'.format(name=self.name, start_time=str(self.start_time), end_time=str(self.end_time))
    def calculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += (self.items).get(item)
        return total

items_brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch = Menu('Brunch', items_brunch, 1100, 1600)

items_early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu('Early Bird', items_early_bird, 1500, 1800)

items_dinner = {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
dinner = Menu('Dinner', items_dinner, 1700, 2300)

items_kids = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
kids = Menu('Kids', items_kids, 1100, 2100)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    def __repr__(self):
        return '{address}'.format(address=self.address)
    def available_menus(self, time):
        available_menu = []
        for menu in self.menus:
            if time >= menu.start_time and time <= menu.end_time:
                available_menu.append(menu)
        return available_menu

menus_available = [brunch, early_bird, dinner, kids]
flagship_store = Franchise('1232 West End Road', menus_available)
new_installment = Franchise('12 East Mulberry Street', menus_available)

print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    def __repr__(self):
        return '{name}, you can find it at {franchises}.'.format(name=self.name, franchises=self.franchises)

business1 = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

items_arepa = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu('Arepas', items_arepa, 1000, 2000)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

business2 = Business('Take a\' Arepa', [arepas_place])

print(business1)
print(business2)