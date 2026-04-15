import html
from skaner import Skaner
from typ import Typ

KOLORY_TOKENOW = {
    Typ.KEYWORD: "color: #ff79c6; font-weight: bold;",
    Typ.OPERATOR: "color: #50fa7b;",
    Typ.COMMENT: "color: #6272a4; font-style: italic;",
    Typ.STRING: "color: #f1fa8c;",
    Typ.NUMBER: "color: #bd93f9;",
    Typ.IDENTIFIER: "color: #f8f8f2;",
    Typ.ERR: "color: #ff5555; text-decoration: underline;"
}
def generate_html(lista_tokenow,nazwa_p):
    with open(nazwa_p,'w',encoding='utf-8') as f:
        f.write('<html><body style="background: #282a36;"><pre>')
        for t in lista_tokenow:
            styl = KOLORY_TOKENOW.get(t.typ, "")
            value = html.escape(str(t.wartosc))
            f.write(f'<span style="{styl}">{value}</span>')
        f.write('</pre></body></html>')

if __name__=="__main__":
    with open("example.txt","r")as f:
        kod=f.read()

    tokeny=[]
    idx=0
    while idx < len(kod):
        token = Skaner.skaner(kod, idx)
        tokeny.append(token)
        idx = token.kolumna

        if token.typ == Typ.EOF:
            break

    generate_html(tokeny, "wynik.html")
