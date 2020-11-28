class Nodo :
    def __init__(self,datoinicial):
        self.dato = datoinicial
        self.siguiente = None

    def obtenerDato(self):
        dato = self.dato
        return (dato)

    def obtenerSig(self):
        sig = self.siguiente
        return (sig)

    def asignarDato(self,nuevoD):
        self.dato = nuevoD

    def asignarSig(self,sigD):
        self.siguiente = sigD


class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self,item):
        ##creamos un nodo con el nuevo item
        nod = Nodo(item)
        nod.asignarSig(self.cabeza)
        self.cabeza = nod

    def tamano(self):
        actual = self.cabeza
        contador=0

        while actual != None:
            contador = contador+1
            actual = actual.obtenerSig()
        return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False

        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSig()
            
        return encontrado

    def remover(self,item):
        nodActual = self.cabeza
        nodPrevio =None
        encontrado = False

        while not encontrado:
            if nodActual.obtenerDato() == item:
                encontrado = True
            else:
                nodPrevio = nodActual
                nodActual = nodActual.obtenerSig()
      
      
        if nodPrevio == None:
            self.cabeza = nodActual.obtenerSig()
        else:
            nodPrevio.asignarSig(nodActual.obtenerSig())

    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual= actual.obtenerSig()

    def ordAsc(self):
        actual = self.cabeza
        previo = None
        cont = 0 
        while actual!= None:
            cont = cont+1


            if(previo.obtenerDato() > actual.obtenerDato()):



                temp = previo.obtenerDato()
                previo = actual.obtenerDato()
                actual = temp
            
class ListaOrdAsc(ListaNoOrdenada):
    def init(self):
        self.cabeza = None

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        stop = False
        while actual != None and not stop:
            if actual.obtenerDato() > item:
                stop = True
            else:
                previo = actual
                actual = actual.obtenerSig()
        temp = Nodo(item)
        if previo == None:
            temp.asignarSig(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSig(actual)
            previo.asignarSig(temp)

    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSig()



class ListaOrdDesc(ListaNoOrdenada):
    def init(self):
        self.cabeza = None

    def agregar(self,item):
        actual = self.cabeza
        previo = None
        stop = False
        while actual != None and not stop:
            if actual.obtenerDato() < item:
                stop = True
            else:
                previo = actual
                actual = actual.obtenerSig()
        temp = Nodo(item)
        if previo == None:
            temp.asignarSig(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSig(actual)
            previo.asignarSig(temp)

    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerDato())
            actual = actual.obtenerSig()

menu = "1. Lista ascendente\n2.lista Descendente\nElige la opcion que deseas:"

r = input(menu)
if(r=="1"):
    milista= ListaOrdAsc()
    for i in range(5):
        print("Ingrese el numero ",i+1,":",end="")
        num = input("")
        milista.agregar(num)
    milista.imprimir()

if(r=="2"):
    milista= ListaOrdDesc()
    for i in range(5):
        print("Ingrese el numero ",i+1,":",end="")
        num = input("")
        milista.agregar(num)
    milista.imprimir()








    


