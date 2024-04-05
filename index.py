import math
print ("Bhaskara")
a = float (input("A:"))
if a != 0:
    b = float (input("B:"))
    c = float (input("C:"))
    delta = math.pow(b,2) - 4 * a*c
    print ("Valor de delta", delta)
    if delta < 0:
        print ("Como o delta é menor que zero, a equação não terá raizes reais.")
    elif delta > 0:
        x1 = (-b + math.sqrt(delta))/ (2*a)
        x2 = (-b - math.sqrt(delta))/ (2*a)
        print ("Quando for + :", x1)
        print ("Quando for - :", x2)
    elif delta == 0:
        x1 = (-b + math.sqrt(delta))/ (2*a)
        print (x1)
else:
        print ("Não há equação de segundo grau")
