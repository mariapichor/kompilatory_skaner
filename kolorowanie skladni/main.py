from skaner import Skaner 
from typ import Typ

wyr = "2+3*(76+8/3)+ 3*($9-3)"
tokens = []

i=0
while i < len(wyr):
    if wyr[i] == " ":
        i += 1
        continue
    token = Skaner.skaner(wyr, i)
    if token:
        i = token.kolumna
        tokens.append(token)

for token in tokens:
        if(token.typ != Typ.ERR):
            print(token.typ.value, token.wartosc)
        else:
            print("Rozpoznano nieprawidłowy znak:", token.wartosc, " numer kolumny:", token.kolumna)