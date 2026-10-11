#se voglio utiizzare una classe definita in un altro file o modulo devo usare le
#parole chiave import e from

from quadroGAIA import Quadro

#ora posso utilizzare la classe quadro es. per creare oggett
q = Quadro("Monet", "...", "...", "...")

print(q.__str__())

#qua non stampa lo spazio in memoria perchè ho definito la funz __str__ per l'oggetto
print(q)


lista_di_quadri = []
lista_di_quadri.append(q)
lista_di_quadri.append(Quadro("Cezanne", "...", "...","..."))
lista_di_quadri.append(Quadro("Polloc", "...", "...","..."))

for quadro in lista_di_quadri:
    print(quadro.__str__())

# 1. CON LE CLASSI POSSO DEFINIRE I MIEI TIPI DI DATO (ES. QUADRO)
# 2. POSSO DOTARLI DEI DATI/DEGLI ATTRIBUTI CHE LI CARATTERIZZNO (TENDENZIALMENTE NASCOSTI)
# 3. POSSO DOTARLI DELLE FUNZIONI/DEI METODI PER OPERARE SU QUEI DATI
#    OVVERO METODI GETTER/SETTER (PER ACCEDERE AGLI ATTRIBUTI) O ALTRI (ES. __str__())

