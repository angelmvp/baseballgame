import random


class jugador:
    pass
    nombre = "Pitcher"
    equipo ="DEFAULT"
    numero = 0
    fuerza=0
    resistencia= 0
    def __init__(self, nombre, equipo,numero,fuerza,resistencia):
        self.nombre=nombre
        self.equipo=equipo
        self.numero=numero
        self.fuerza=fuerza
        self.resistencia=resistencia
    def estadisticas(self):
        print("el nombre es ", self.nombre)
        print("el equipo es  ",self.equipo)
        print("su numero es  ",self.numero)
        print("su fuerza  es  ",self.fuerza)
        print(" la resitencia es  ",self.resistencia)
    def lanzamiento(self):
        self.resistencia= self.resistencia-1
    def tienelanzamientoS(self):
        return self.resistencia>0
    def cambiarlanzador(self):
        self.tienelanzamientos=0
        print(self.nombre, "se quedo sin lanzamientos")
    def enfrentamiento(self,bateador):
        return self.fuerza/bateador.fuerza
    def pitcheo(self,bateador):
        self.lanzamiento()
        if random.uniform(0,1.7) > self.enfrentamiento(bateador):
            print("el bateador ha pegado de hit")
        else:
            print("el bateador esta fuera")

pitcher = jugador("Shohei","dodgers",17,95,86)
bateador= jugador("judge","yankees",99,90,0)
pitcher.estadisticas()
pitcher.lanzamiento()
bateador.estadisticas()

pitcher.pitcheo(bateador)

