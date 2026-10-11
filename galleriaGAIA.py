
class Quadro:
    #metodo che costruisce e inizializza gli oggetti della classe quadro
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista = artista
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno

#altri metodi s. getter e setter per accesso ad attributi nascosti in scrittura e lettura (_scoraggiare
#accesso, __per vietare l'accesso
    @property       #GETTER METHOD per leggere l'anno dalla pancia dell'attributo
    def anno(self):      #metodo per leggere il valore dell'attributo nascosto(__)anno
        return self.__anno

    @anno.setter   #SETTER METHOD per imopostare il valore
    def anno(self, anno):
        self.__anno = anno  #eventualmente posso aggiungere coduce per controllo errori

#Metodo/funzione che consente al quadro di descriversi come stringa
    #__str__ alternativa a nomi più bizzarri come descriviti, stampatiecc..
    def __str__(self):
        return f"{self.__artista} - {self.__titolo} - {self.__materiali} - {self.__anno}"


q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", "1870")

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} - {q1.__anno}")

#q1.__anno = 1945  avendo chiamato gli attributi con davanti il doppio __, anche se provo a cambiare
#l'attributo del singolo oggetto non me lo permette perche  __ lo rende privato/nascosto

#se voglio cambiare l'anno, quindi per accedere all'attributo, devo usare i metodi/funzioni
#q1.imposta_anno(1800)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} - {q1.__anno}")
#print("Anno: "+str(q1.leggi_anno()))

print("Anno :" + str(q1.anno))

#come faccio a stampare il quadro? con tutti i suoi attributi visto che sono nascosti=
#chiedo al quadro di stamparsi, chi lo sa mrgio di lui come stamparsi? creo un metodo far si che
# si dwscriva (sopra nei metodi)
print(q1.__str__())  #cosi ho delegato al quadro il compito di stamparsi