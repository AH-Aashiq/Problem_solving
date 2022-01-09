#Bhaskara's Formula
import math
A,B,C = map(float,input().split())
D = (B**2)-(4*A*C)
if(D <0 or A==0):
    print("Impossivel calcular")
else:
    D=math.sqrt(D)
    R1 = (-B+D)/(2*A)
    R2 = (-B-D)/(2*A)
    print(f'R1 = {R1:0.5f}\nR2 = {R2:0.5f}')

