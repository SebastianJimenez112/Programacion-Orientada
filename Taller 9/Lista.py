from Aleatoriador import Aleatoriador
from Aleatoriador import Ordenador



miOrdenador=Ordenador()
miAleatoriador=Aleatoriador()

miAleatoriador.generar_lista_aleatoria()
miLista=miAleatoriador.getlista()


miLista=miOrdenador.ordenarLista(miLista)
miOrdenador.imprimirLista(miLista)
