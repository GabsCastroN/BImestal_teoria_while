import math

N = int(input("Numero: "))

while N < 0:
    print("Deberia ser un numero positivo")
    N = int(input("Numero: "))
print(f"\nSu raiz cuadrada: {(math.sqrt(N)):2f}")