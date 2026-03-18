from token import Token
def skaner(wyr):
    tokens = []
    n = len(wyr)
    for i in range(n):
        napis = ""
        while(wyr[i].isdigit()):
            napis+=wyr[i]
            i+=1
        