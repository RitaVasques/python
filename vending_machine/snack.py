class Snack:
    nbr_snacks = 0;
    def __init__(self, name='', price=0.0):
        Snack.nbr_snacks += 1
        self.id_snack = Snack.nbr_snacks
        self.name = name
        self.price = price

    def __str__(self):
        return (f'Snack: id_snack = {self.id_snack}, name = {self.name}, '
                f'price = {self.price}')
    
    def write_snack(self):
        return f'{self.id_snack},{self.name}, {self.price}'