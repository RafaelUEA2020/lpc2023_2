from bullet import Bullet
from field import Field
from tank import Tank
from wall import Wall

print("Welcome to Combat!")
print()

parede1 = Wall(1,2)
parede2 = Wall(3,4)
tank1 = Tank(4, 5, "Tank1")
tank2 = Tank(7, 8, "Tank2")

tank1.atirar()
bullet = Bullet(1,1)
bullet.colidiu_parede()

tank2.atirar()
bullet.colidiu_inimigo()

tank1.reseta_posicao()
tank2.reseta_posicao()

tank2.atirar()
bullet.colidiu_parede()

tank1.atirar()
bullet.colidiu_inimigo()

tank1.reseta_posicao()
tank2.reseta_posicao()

tank1.atirar()
bullet.colidiu_parede()
tank2.atirar()
bullet.colidiu_parede()
tank1.atirar()
bullet.colidiu_parede()
bullet.colidiu_inimigo()

tank1.reseta_posicao()
tank2.reseta_posicao()

tank2.atirar()
bullet.colidiu_parede()

tank1.atirar()
bullet.colidiu_inimigo()

print("Fim.")






