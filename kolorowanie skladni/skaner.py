from token import Token
from typ import Typ

class Skaner:
    def skaner(tekst, i) -> Token:
        operators = {'+', '-', '/', '*', '>', '<'}
        keywords = {'if', 'else', 'while', 'for', 'return', 'print'}
        separators = {',', ';', ':', '(', ')', '{', '}'}
        n = len(tekst)
        if i < n:
            x = tekst[i]
            if x.isdigit():
                napis = x
                i += 1
                while i < n and tekst[i].isdigit():
                    napis += tekst[i]
                    i += 1
                return Token(Typ.NUMBER, int(napis), i)

            if x.isalpha():
                napis = x
                i += 1
                while (i < n and (tekst[i].isalpha() or tekst[i].isdigit())):
                    napis += tekst[i]
                    i += 1
                if napis in keywords:
                    return Token(Typ.KEYWORD, napis, i)
                return Token(Typ.IDENTIFIER, napis, i)
            
            if x == '"':
                napis = '"'
                i += 1
                while i < n and tekst[i] != '"':
                    napis += tekst[i]
                    i += 1
                if i < n and tekst[i] == '"':
                    napis += '"'
                    i += 1 
                    return Token(Typ.STRING, napis, i)
                return Token(Typ.ERR, napis, i)
            
            if x=='#':
                napis = x
                i+=1
                while i<n and tekst[i]!='\n':
                    napis+=tekst[i]
                    i+=1
                return Token(Typ.COMMENT, napis, i)
            if x == '=':
                napis = x
                i+=1
                if i<n and tekst[i] == "=":
                    napis+=tekst[i]
                    i+=1
                    return Token(Typ.OPERATOR, napis, i)
                return Token(Typ.OPERATOR, x, i)
            if x == ' ' or x=='\t':
                napis = x
                i+=1
                while i<n and (tekst[i]==' ' or tekst[i]=='\t'):
                    napis+=tekst[i]
                    i+=1
                return Token(Typ.WHITESPACE, napis, i)
            i+=1
            if x in operators:
                return Token(Typ.OPERATOR, x,i)
            elif x in separators:
                return Token(Typ.SEPARATOR, x,i)
            elif x == '\n':
                return Token(Typ.NEWLINE, x, i)
            else:
                return Token(Typ.ERR, x, i)

        return Token(Typ.EOF, None, i)