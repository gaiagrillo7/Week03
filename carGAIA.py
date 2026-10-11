#definisco un nuovo tipo di dato la classe Car

class Car:   #classi devono avere iniziale maiuscola per convenzione
    def __init__(self):
        self.licensplate = ""   #attributi o variabili d'istanza
        self.color = "White"
        self.turnedOn = False




c1 = Car()   #creaiamo un oggetto di classe-tipo di car

#print(c1) facendo così non si stampa l'oggetto, ma il riferimento all' oggetto, cioè l'identificativo
#della sua aria di memoria

print("Lincense plate: "+str(c1.licensplate))
print("Color: "+str(c1.color))
print("Turned on: "+str(c1.turnedOn))
