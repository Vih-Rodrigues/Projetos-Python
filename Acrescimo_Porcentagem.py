"""
Python: acréscimo de 12%
"""
import math
import decimal

varProduto = (input("Informe o preço do produto: "))
varProdutoPosAcrescimo = (varProduto + (varProduto * 0.12))

#Saída
print("\nNovo preço = %.2f" %varProdutoPosAcrescimo)