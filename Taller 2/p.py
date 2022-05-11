import random
class generador:
    def __init__(self):
        self.cantidad=200
        self.lista=[]
    def cambiarlista(self,valor):
        self.cantidad=valor              
    def generarlista(self):
        for _ in range(0,self.cantidad):
            a=random.randint(0,20)
            self.lista.append(a)
        return self.lista
migenerador=generador()
print(migenerador.generarlista())
