from enum import Enum

class Typ(Enum):
    LICZBA = "LICZBA"
    ID = "ID"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MNOZENIE = "MNOZENIE"
    DZIELENIE = "DZIELENIE"
    LNAWIAS = "LNAWIAS"
    PNAWIAS = "PNAWIAS"
    EOF = "EOF"
    ERR = "ERR"