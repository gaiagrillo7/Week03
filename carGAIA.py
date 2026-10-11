#definisco un nuovo tipo di dato la classe Car

class Car:   #classi devono avere iniziale maiuscola per convenzione
   #per memorizzare informazioni che valgano per tutti gli oggetti
   wheels = 4 #variabile di classe, cioè identica per tutti gli oggetti/istanze della classe car

#Creazione ed inizializzazione dell'oggetto
   def __init__(self, license_plate, color):   #costruttore della classe
        self.license_plate = license_plate  #attributi o variabili dell'istanza/oggetto
        self.color = color
        self.turned_on = False

#METODI, ovvero le funzuoni messe a disposizione di una classe
   def paint(self, color):
       self.color = color

   def turn_on(self):
       self.turned_on = True



#c1 = Car()   #creaiamo un oggetto di classe-tipo di car

#print(c1) facendo così non si stampa l'oggetto, ma il riferimento all' oggetto, cioè l'identificativo
#della sua aria di memoria

c1 = Car("AA123BB","Red")  #qui invoco il costruttore passando due parametri e creo
#l'oggetto 1

print("Lincense plate: "+str(c1.license_plate))
print("Color: "+str(c1.color))
print("Turned on: "+str(c1.turned_on))


c2 = Car("ZZ666ZZ", "Black")  #qua creo l'oggetto 2 o istanza 2

#c1.wheels = 7  #cosi non tocca la variabile wheels ma ne crea una nuova quindi con print(c1.wheels)
#stampa 7

#come si accede alle variabili D'istanza
c1.color = "Green"  #così creo una modifica della variabile colore dell'istanza c1

#come si accede alle variabili di classe
Car.wheels = 7  #così modifico la variabile di classse, cioè sarà una modifica su tutti gli oggetti
#appartenenti alla classe car

#come faccio a cambiare il colore di un oggetto car, stessa cosa che abbiamo fatto alla riga 34
c1.color = "Pink"
c2.turned_on = True


#anzichè accedere direttamente agli attributi posso usare le funzioni
c1.paint("Violet")

c1.numbers_of_doors = 2 #così scrivo una variabile solo per l'oggetto/istanza c1
#fare così è tioicamente un ERRORE, le variabili si creano all'interno della finzione init

pass