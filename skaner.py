from token import Token
from typ import Typ

class Skaner:
    def skaner(tekst, i) -> Token:
        n = len(tekst)
        if i < n:
            x = tekst[i]


            if x.isdigit():
                napis = x
                i += 1
                while i < n and tekst[i].isdigit():
                    napis += tekst[i]
                    i += 1
                return Token(Typ.LICZBA, int(napis), i)

            if x.isalpha():
                napis = x
                i += 1
                while (i < n and tekst[i].isalpha()):
                    napis += tekst[i]
                    i += 1
                return Token(Typ.ID, napis, i)
            i+=1
            if x == '+':
                return Token(Typ.PLUS, x, i)
            elif x == '-':
                return Token(Typ.MINUS, x,i)
            elif x == '*':
                return Token(Typ.MNOZENIE, x, i)
            elif x == '/':
                return Token(Typ.DZIELENIE, x, i)
            elif x == '(':
                return Token(Typ.LNAWIAS, x, i)
            elif x == ')':
                return Token(Typ.PNAWIAS, x, i)
            else:
                return Token(Typ.ERR, x, i)

        return Token(Typ.EOF, None, i)