"""
Python: IMC
"""
import math
import decimal

varPeso = int(input("Informe o peso: "))
varAltura = int(input("Informe a altura em centímetros: "))
varIMC = (varPeso / (varAltura^2))

#Saída
if varIMC <= 18.5:
    print("\nIMC = %.2f" %varIMC)
    print("Abaixo do peso.")
elif varIMC > 18.5 and <= 24.9:
    print("\nIMC = %.2f" %varIMC)
    print("Peso normal.")
elif varIMC > 24.9 and <= 29.9:
    print("\nIMC = %.2f" %varIMC)
    print("Acima do peso.")
elif varIMC > 29.9 and <= 34.9:
    print("\nIMC = %.2f" %varIMC)
    print("Obesidade grau I.")
elif varIMC > 34.9 and <= 39.9:
    print("\nIMC = %.2f" %varIMC)
    print("Obesidade grau II.")
else:
    print("\nIMC = %.2f" %varIMC)
    print("Obesidade grau II.")
