from typ import Typ
class Token:
    typ: Typ
    def __init__(self, typ, wartosc):
        self.typ = typ
        self.wartosc = wartosc
