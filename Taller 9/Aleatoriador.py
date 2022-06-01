import random 
class Aleatoriador: 

    def generar_lista_aleatoria(self):
        self.lista=[]
        for _ in range (0,100):
            a=random.randint(0,50)
            self.lista.append(a)

    def getlista(self):
        return self.lista
