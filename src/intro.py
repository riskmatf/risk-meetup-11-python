#python je dinamicki tipiziran jezik, tako da nije potrebno navoditi tip promenljive
a = 5
b = "Zdravo!"
#tip promenljive se moze videti pozivom funkcije type()
type(b)

#podrzane su sve osnovne aritemticke operacije, uz dodatak stepenovanja
c = a**2 # c = a^2

#operator + primenjen na stringovima spaja stringove
b = "Zdravo " + "svete!"
#stringovi se mogu pisati izmedju '' ili izmedju ""
s1 = 'Ovaj string ima "navodnike"'
s2 = "Ovaj string ima 'apostrofe'"

#naredba print podrazumevano stavlja novi red na kraju ispisa
print(b)

#opcioni argument 'end' nam omogucava da mi kazemo cime se ispis da se zavrsi
print(b, end=' ') #ovaj print ce na kraju ispisati razmak umesto novog reda

#unos se vrsi funkcijom input(), koja kao opcioni argument prima string koji opisuje sta se unosi
br1 = input("Unesite prvi broj: ")

#input podrazumevnao vraca string. Mozete izvrsiti konverziju u zeljeni tip sa ime_tipa(input()), npr int(input())
br2 = int(input("Unesite drugi broj: "))

#ili mozete pustiti jezik da sam zakljuci tip
br3 = eval(input("Unesite treci broj: "))

#Nizovi
l = [1,2,3]
print(l)

#nizovi mogu cuvati razlicite tipove u sebi
l = [1,2,3.14, "pozdrav"]

#indeksiranje krece od 0, duzinu niza dobijate sa len(niz)
#takodje mozete indeksirati sa minusom, to vrsi indeksiranje od nazad
print(l[0])
print(len(l))
print(l[-1])

#mozete uzeti proizvoljan segment niza
print(l[0:3])#uzima l[0], l[1] i l[2]

#niz moze sadrzati i druge nizove u sebi
l1 = ["neki string", l, 4,5,6]
print(l1)

#u toj situaciji, promena niza l utice na niz l1
l[0] = 89
print(l1)

#takodje, ukoliko u l1 promenimo niz l, menja se i originalni niz l
l1[1][2] = 787
print(l)

#Grananja

if a < 10:
	print(f"{a} je manje od 10")
elif b.startswith("Zdravo"):
	print(f'{b} pocinje za Zdravo') 
else:
	print("nijedan uslov nije ispunjen")


#petlje
#postoje while i for petlje

#for petlja je kolekcijska
for i in l:
	print(i, end=' ')

#na ovaj nacin mozemo proci kroz niz sa indeksima
for i in range(len(l)):
	print(l[i], end=' ')

#range moze da ide i u nazad
for i in range(10,0,-2):
	print(i, end = ' ')

i = 0
while i < 10:
	print(i, end=' ')
	i+=1


#funkcije
def saberi(a,b):
	print(a)
	print(b)
	return a+b

print(saberi(br2, br3))

#funkcije imaju imenovane argumente. To znaci da ne morate postovati redosled argumenata u potpisu funkcije
#ukoliko eksplicitno navodite koji argument dobija koju vrednost

print(saberi(a = br3, b = br2))

#takodje, argumenti funkcije mogu imati podrazumevane vrednosti. Ukoliko ne navedete vrednost nekog argumnenta
#on dobije podrazumevanu vrednost

def nadovezi_string(s1="prva rec ", s2="druga rec "):
    return s1 + s2

print(nadovezi_string())
print(nadovezi_string("treca rec "))
print(nadovezi_string(s2 = "svete!", s1 = 'Zdravo '))

#recnici(mape)

recnik = {'a':5,'b':78}
print(recnik)
print(recnik['a'])
recnik['a'] = 17 #dodela vrednosti
recnik['c'] = 67 #ukoliko kljuc ne postoji, bice napravljen

#list comprehension
#opsti oblik: [<izraz> for <promenljiva> in <lista>]

l = [x for x in range(10)]
l1 = [x**2 for x in l]