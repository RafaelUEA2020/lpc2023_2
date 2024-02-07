from wall import Wall

class Field:
    def __init__(self):
        self.paredes = []
    def add_paredes(self, parede):
        self.paredes.append(parede)

    def quant_paredes(self):
        print("Quantidade de paredes: ", len(self.paredes))

