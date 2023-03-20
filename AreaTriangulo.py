"""
Python: área de um triângulo retângulo
"""
import math
import decimal

varBase = float(input("Informe a base em metros: "))
varAltura = float(input("Informe a altura em metros: "))
varArea = ((varBase * varAltura) / 2)

# Saída
print("\nÁrea do triângulo = %.2f" %varArea)