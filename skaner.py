from token import Token
def skaner(wyr):
    tokens = []
    n = len(wyr)
    i=0
    while i<n:
        napis = ""
        while(wyr[i].isdigit()):
            napis+=wyr[i]
            i+=1
        if napis!="":
            tokens.append(Token('LICZBA',int(napis)))
        
        if (wyr[i].isalpha()):
            napis = ""
            while(wyr[i].isalpha()):
                napis+=wyr[i]
                i+=1
            tokens.append(Token('ID',napis))
        if(wyr[i]=='+'):
            tokens.append(Token('PLUS','+'))
        elif(wyr[i]=='-'):
            tokens.append(Token('MINUS','-'))
        elif(wyr[i]=='*'):
            tokens.append(Token('MNOZENIE','*'))
        elif(wyr[i]=='/'):
            tokens.append(Token('DZIELENIE','/'))
        elif(wyr[i]=='('):
            tokens.append(Token('LNAWIAS','('))
        elif(wyr[i]==')'):
            tokens.append(Token('PNAWIAS',')'))
        elif(wyr[i]==" "):
            pass
        else:
            tokens.append(Token('ERR',wyr[i]))
        i+=1
    tokens.append(Token('EOF',''))
    for token in tokens:
        print(token.typ, token.wartosc)