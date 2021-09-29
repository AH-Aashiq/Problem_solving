#Area
a,b,c = list(map(float,input().split()))
triangle=0.5*a*c
circle=3.14159*c*c
trapezium=(a+b)/2.0*c
square=b*b
rectangle=a*b

print(f"TRIANGULO: {triangle:.3f}")
print(f"CIRCULO: {circle:.3f}")
print(f"TRAPEZIO: {trapezium:.3f}")
print(f"QUADRADO: {square:.3f}")
print(f"RETANGULO: {rectangle:.3f}")

