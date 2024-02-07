class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def colidiu_parede(self):
        print("Colidiu com a parede.")

    def colidiu_inimigo(self):
        print("Colidiu com o inimigo.")

