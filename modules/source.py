__autor__ = "Влад Гурбатов"

def sa(a:int, b:int):
    return a+b/2
def sg(a:int, b:int):
    return (a*b)**1/2

def diaposon(low:int, high:int, a:int):
    if low < a < high:
        return True