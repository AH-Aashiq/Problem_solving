#The Greatest 
import math
valor = input().split(" ")
a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
result = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print(f"{int(result)} eh o maior")
