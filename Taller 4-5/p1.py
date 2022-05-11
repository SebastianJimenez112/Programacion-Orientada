import random
n=[]
#LanzarDados
class GenerarAleatorios:
    def lanzardados(self):
        n.append (random.randint(1,6))
    for i in range(1):
        lanzardados(n)
    print(n)    
#Mezclar Cartas
    def MezclarCartas(Cartas):
        Cartas = Cartas[:]
        longitud = len(Cartas)
        for i in range(longitud):
            desordenar = random.randint(0, longitud-1)
            Cartas[i] = Cartas[desordenar]
        return Cartas
    Cartas = ["A♥","A♦","A♣","A♠","2♥","2♦","2♣","2♠","3♥","3♦","3♣","3♠","4♥","4♦","4♣","4♠","5♥","5♦","5♣","5♠","6♥","6♦","6♣","6♠","7♥","7♦","7♣","7♠","8♥","8♦","8♣","8♠","9♥","9♦","9♣","9♠","10♥","10♦","10♣","10♠","J♥","J♦","J♣","J♠","Q♥","Q♦","Q♣","Q♠","K♥","K♦","K♣","K♠"]
    Mezcladas= MezclarCartas(Cartas)
    print("Las cartas son=",Cartas)
    print("Cartas mezcladas=",Mezcladas)   
#Ordenar y desordenar lista
class Ordenador(GenerarAleatorios):
    lista = [2,2,43,45,56,67,87,8,99,100,181,1,3,4,15]
    def ordenarLista():
        print()  
    lista.sort()
    print("La lista ordenada de menor a mayor es=",lista)
    random.shuffle(lista)
    print("La lista desordenada es=",lista)
#Repartir Cartas a Jugadores
class JugadorCartas(Ordenador):
    def RepartirCartas(self):
       jugador1=[]
       jugador2 =[]
       jugadores=[jugador1,jugador2]
       for i in range(5):
        baraja=["A♥","A♦","A♣","A♠","2♥","2♦","2♣","2♠","3♥","3♦","3♣","3♠","4♥","4♦","4♣","4♠","5♥","5♦","5♣","5♠","6♥","6♦","6♣","6♠","7♥","7♦","7♣","7♠","8♥","8♦","8♣","8♠","9♥","9♦","9♣","9♠","10♥","10♦","10♣","10♠","J♥","J♦","J♣","J♠","Q♥","Q♦","Q♣","Q♠","K♥","K♦","K♣","K♠"]       
        for j in range(2):
                jugadores.append(baraja.pop(0))
    for i in range(2):
        print("jugador{}:".format(i+1))
        for j in range(5):
            baraja=["A♥","A♦","A♣","A♠","2♥","2♦","2♣","2♠","3♥","3♦","3♣","3♠","4♥","4♦","4♣","4♠","5♥","5♦","5♣","5♠","6♥","6♦","6♣","6♠","7♥","7♦","7♣","7♠","8♥","8♦","8♣","8♠","9♥","9♦","9♣","9♠","10♥","10♦","10♣","10♠","J♥","J♦","J♣","J♠","Q♥","Q♦","Q♣","Q♠","K♥","K♦","K♣","K♠"]
            print("{:10}".format(baraja[i+j]), end="")              