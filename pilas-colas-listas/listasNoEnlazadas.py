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

   # def ordenAsc(self):
      
       # actual = self.cabeza
        #lista =[]

        #print(actual.obtenerDato())
        #while actual != None:
            #lista.append(actual)
            #actual = actual.obtenerSig()
           
        #print(len(lista))
        #for i in range(len(lista)):
            #print(lista[i].obtenerDato(),end="/")

        

#def ordAsc(ListaNoOrdenada):
   # def agregar(self,item):
        ##creamos un nodo con el nuevo item
        #nod = Nodo(item)
        #nod.asignarSig(self.cabeza)
        #self.cabeza = nod
    
    #actual = self.cabeza
   # previo = None

    #while actual != None:
        #if(actual > actual.obtenerSig()):
           # previo = ac






    

milista = ListaNoOrdenada()

milista.agregar(31)
milista.agregar(77)
milista.agregar(17)
milista.agregar(93)
milista.agregar(26)
milista.agregar(54)
milista.imprimir()


#print(milista.tamano())
#print(milista.buscar(93))
#print(milista.buscar(100))

#milista.agregar(100)
#print(milista.buscar(100))
#print(milista.tamano())

#milista.remover(54)
#print(milista.tamano())
#milista.remover(93)
#print(milista.tamano())
#milista.remover(31)
#print(milista.tamano())
#print(milista.buscar(93))
#milista.imprimir()