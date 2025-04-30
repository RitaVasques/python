from service_snacks import ServiceSnacks
from snack import Snack

class SnacksMachine:
    def __init__(self):
        #to be able to use the service methods
        self.service_snacks = ServiceSnacks()
        #to generate ticket
        self.products_bought = []

    def snacks_machine(self):
        exit = False
        print('*** Snacks Machine ***')
        self.service_snacks.show_snacks()
        while not exit:
            try:
                option = self.show_menu()
                exit = self.execute_option(option)
            except Exception as e:
                print(f'Error: {e}')
    
    def show_menu(self):
        print(f'''Menu: 
              1. Buy snack
              2. Show ticket
              3. Add new snack
              4. Show snacks
              5. Exit''')
        return int(input('Chose an option: '))
    
    def execute_option(self, option):
        if option == 1:
            self.buy_snack()
        elif option == 2:
            self.show_ticket()
        elif option == 3:
            self.add_snack()
        elif option == 4:
            self.service_snacks.show_snacks()
        elif option == 5:
            print('Bye Bye!')
            return True
        else:
            print('Invalid Option')
        return False
    
    def buy_snack(self):
        id_snack = int(input('What snack do you want (id)? '))
        snacks = self.service_snacks.getSnacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.products_bought.append(snack)
            print(f'You bought: {snack}')
        else:
            print('Id not found')

    def show_ticket(self):
        if not self.products_bought:
            print('No products bought')
            return
        total = sum(snack.price for snack in self.products_bought)
        print('--- Sale Ticket---')
        for product in self.products_bought:
            print(f'\t- {product.name} - ${product.price:.2f}')
        print(f'\tTotal -> ${total:.2f}')
    
    def add_snack(self):
        name = input('Snack name: ')
        price = float(input('Price of product: '))
        new_snack = Snack(name, price)
        self.service_snacks.add_snack(new_snack)
        print('Snack added')

# Programa principal
if __name__ == '__main__':
    snacks_machine = SnacksMachine()
    snacks_machine.snacks_machine()