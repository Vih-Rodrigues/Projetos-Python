"""
Python: Resistencia equivalente
Na área da eletrônica, em um circuito em série temos que a resistência equivalente (total) desse circuito é obtida mediante a soma de todas as resistências existentes
(RE = r1 + r2 + ... + rn).
Faça uma aplicação que receba o valor de quatro resistências ligadas em série, calcule e mostre a resistência equivalente, a maior e a menor resistência. 
"""
import os
os.system('cls')

varQtdeResistencias = int(input("Informe a quantidade de resistências ligadas em série: "))

vetResistencias = []

for i in range(varQtdeResistencias):
    vetResistencias.append(int(input("Informe a resistencia: ")))

print(f"\nResistência equivalente: {sum(vetResistencias)}") # f = format, utilizado para interpolação
print(f"\nMaior resistência: {max(vetResistencias)}\nMenor resistência: {min(vetResistencias)}")