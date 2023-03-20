"""
Python: Estrutura de repetição: For
"""
import os
os.system('cls')

for i in range(5):
    print(i)

print("\n")

for i in range(1,10,2):
    print(i)

print("\n")

for i in range(10,1,-1):
    print(i)

print("\n")

soma = 0
for i in range(5):
    soma += i
else:
    # Após terminar a iteração
    print("Soma = %d" %soma)

dados = "abcdefg"
for pos, valor in enumerate(dados):
    print("Posição: {0}, Valor: {1}".format(pos,valor))