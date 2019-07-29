#se crea una lista enlazada con funciones básicas
class nodo:

    def __init__(self, siguiente = None, anterior = None, valor = None):
        self.siguiente = siguiente
        self.anterior = anterior
        self.valor = ValueError
        self.indice = 0
    

class lst:
    
    def __init__(self):
        self.cabeza = nodo(valor="" )
        self.cabeza.siguiente = None
        self.cola = None
        self.valor = None
        self.auxiliar = nodo()
        self.largo = -1
        print("lista creada")

    def insertarInicio (self, valor = None):
        self.largo = self.largo + 1
        print("Se ingresó el item " + str(self.largo))
        if (self.cabeza is not None):
            self.auxiliar = nodo()
            self.auxiliar.valor  = valor # guarda el valor del nuevo nodo
            self.auxiliar.siguiente = self.cabeza # nuevo.siguiete apunta a nodo inicial
            self.cabeza = self.auxiliar #asigna el nuevo nodo como cabeza
            self.cabeza.indice = self.largo #ingresa le índice
        else:
            self.cabeza.valor = valor
            self.cabeza.indice = 0

    def eliminarInicio(self):
        self.largo = self.largo -1
        print("Se ha eliminado el primer elemento")
        if self.cabeza.siguiente is not None :
            self.auxiliar = nodo() # crea un nuevo nodo auxiliar
            self.auxiliar = self.cabeza # el auxiliar es la cabeza 
            self.cabeza = self.cabeza.siguiente # la cabeza es el siguiente de cabesa
            self.auxiliar = None

    
    def modificarDato (self, indice, valor):
        # veriica que el indice exista
        if int(indice) > self.largo :
            print("El índice indicado, no existe")
        else:
            ndc = 0
            self.auxiliar = self.cabeza

            while (ndc < indice) :
                self.auxiliar = self.auxiliar.siguiente
                ndc = ndc + 1
            
            print("Se ha modificado el valor " + str(self.auxiliar.valor))
            print("Por el siguiente valor " + str(valor))
            self.auxiliar.valor = valor
            
    
    def mostrar (self):
        self.auxiliar = self.cabeza
        while(self.auxiliar.siguiente is not None):
            print("Elemento: " + str(self.auxiliar.valor) + " en índice " + str(self.auxiliar.indice))
            self.auxiliar = self.auxiliar.siguiente


class acciones :
    
    def __init__ (self):
        self.lista = lst()
        self.option = 0
    
    def Iniciar(self):
        
        print("1. Insertar elemento")
        print("2. Eliminar elemento")
        print("3. Editar elemento")
        print("4. Salir")
        self.option = int(input())

        if self.option is 1 :
            print("Ingresa el valor del nuevo elemento")
            self.lista.insertarInicio(input())
            self.lista.mostrar()
            self.Iniciar()
            pass
        elif self.option is 2:
            self.lista.eliminarInicio ()
            self.lista.mostrar()
            self.Iniciar()
            pass
        elif self.option is 3:
            print("Ingresa el índice del elemento que deseas editar")
            indi = input()
            print("Ingresa el nuevo valor del elemento a modificar")
            val = input()

            self.lista.modificarDato(indi, val )

            self.Iniciar()
            pass
        elif self.option is 4:
            print("vuelva pronto")


menu = acciones()
menu.Iniciar()


#insertar un nuevo nodo
