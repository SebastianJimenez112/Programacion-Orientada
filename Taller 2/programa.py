import random

class Generador:
    
   
    
    def cambiarLimites(self,inicio, fin):
        self.inicio=inicio
        self.final=fin
    
    def cambiarCantidad(self, valor):
        self.cantidad=valor
    
    def generarLista(self):
        self.lista=[]
        for _ in range(0,self.cantidad):
            a=random.randint(self.inicio,self.final)
            self.lista.append(a)        
        return self.lista

miGenerador4=Generador()
miGenerador4.cambiarLimites(0,6)
miGenerador4.cambiarCantidad(2)
for i in range(0,20):
    print(i, miGenerador4.generarLista())
