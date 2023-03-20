"""
Python: Tabuada
Faça uma aplicação que apresente em tela a tabuada de qualquer número.
O usuário fornece o número desejado e a aplicação apresenta a relação de todos os cálculos de 1 a 10.
"""
import os
os.system('cls')

varNumero = int(input("Informe o número desejado: "))

for i in range(11):
    print(f"\n{i} x {varNumero} = {varNumero*i}")