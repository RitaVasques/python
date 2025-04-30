import os.path
from snack import Snack

class ServiceSnacks:
    file_name = 'snacks.txt'

    def __init__(self):
        #list of snacks
        self.snacks = []
        #check if file already exists
        #if exists, we get the snacks from the file
        if os.path.isfile(self.file_name):
            self.snacks = self.get_snacks()
        #if not, we add snacks and create file
        else:
            self.add_initial_snacks()

    def add_initial_snacks(self):
        inicial_snacks = [Snack('chips', 70), Snack('soda', 50), Snack('sandwich', 120)]
        #add snack to list already created @ begining
        self.snacks.extend(inicial_snacks)
        #save the list to a file
        self.save_snacks_in_file(inicial_snacks)

    def save_snacks_in_file(self, snacks):
        try:
            with open(self.file_name, 'a') as file:
                for snack in snacks:
                    file.write(f'{snack.write_snack()}\n')
        except Exception as e:
            print(f'Error saving snacks in file: {e}')

    def get_snacks(self):
        snacks = []
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    id_snack, name, price = line.strip().split(',')
                    snack = Snack(name, float(price))
                    snacks.append(snack)

        except Exception as e:
            print(f'Error reading file: {e}')
        return snacks
        
    def add_snack(self, snack):
        self.snacks.append(snack)
        self.save_snacks_in_file([snack])

    def show_snacks(self):
        print('---Available Snacks---')
        for snack in self.snacks:
            print(snack)
        
    def getSnacks(self):
        return self.snacks