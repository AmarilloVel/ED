### ultimo en entrar primero en salir
class Pila:
    def __init__(self):
        self.items = []
    def estavacia(self):
        return self.items == []
    def incluir(self,item):
        self.items.append(item)

    def extraer(self):
        try:
            self.items.pop()
        except IndexError:
            print("La pila esta vacia")

    def inspeccionar(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)

    def imprimirItems(self):

        print("[",end="")
        for i in range(len(self.items)):
            print(self.items[i],end="|")

        print("]")

        ##for i in range(len(itemsAct)-1):
          #  print(itemsAct[i])


p=Pila()

print(p.estavacia())  
p.incluir('perro')
p.incluir('perro')
p.incluir('perro')
p.incluir('tamal')

print(p.tamano())
p.imprimirItems()
p.incluir('tamal')
print(p.inspeccionar())
print(p.inspeccionar())
print(p.estavacia())  
p.imprimirItems()

p.extraer()
