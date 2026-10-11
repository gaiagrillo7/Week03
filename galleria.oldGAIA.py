
class Quadro:
    def __init__(self, artista, titolo, materiali, anno):
        self.__artista = artista
        self.__titolo = titolo
        self.__materiali = materiali
        self.__anno = anno

    def imposta_anno(self, nuovo_anno):
        if(nuovo_anno>1853 & nuovo_anno<1890):
           self.__anno = nuovo_anno
        else:
            print("L'anno inserito non è validpo)

    def leggi_anno(self):
        return self.__anno

q1 = Quadro("Van Gogh", "Autoritratto", "Olio su tela", "1870")

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} - {q1.__anno}")

#q1.__anno = 1945  avendo chiamato gli attributi con davanti il doppio __, anche se provo a cambiare
#l'attributo del singolo oggetto non me lo permette perche  __ lo rende privato/nascosto

#se voglio cambiare l'anno, quindi per accedere all'attributo, devo usare i metodi/funzioni
q1.imposta_anno(1800)

#print(f"{q1.__artista} {q1.__titolo} {q1.__materiali} - {q1.__anno}")
print("Anno: "+str(q1.leggi_anno()))

