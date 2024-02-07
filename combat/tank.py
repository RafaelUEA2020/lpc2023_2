from bullet import Bullet
class Tank:
    def __init__(self, x, y, nome):
        self.x = x
        self.y = y
        self.nome = nome


    def atirar(self):
        print(self.nome, " atirou.")

    def movimento(self):
        print("Movimentou.")

    def reseta_posicao(self):
        print(self.nome, "com posicao resetada.")