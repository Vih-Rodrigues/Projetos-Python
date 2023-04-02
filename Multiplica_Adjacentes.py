"""
Python: 
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
Example
• For inputArray = [3, 6, -2, -5, 7, 3], the output should be adjacentElementsProduct(inputArray) = 21.
7 and 3 produce the largest product.
"""
import os

def fLimpaTela():
    os.system('cls')

def fVetorMultiplicaAdjacentes(pVetorInteiros):
    vVetorMultiplicaAdjacentes = []
    for i in range(len(pVetorInteiros)-1): # Pega os elementos até o penultimo, pois o ultimo nao tera um a direita para ser seu adjacente
        vAuxiliarEsquerda = pVetorInteiros[i]
        vAuxiliarDireita = pVetorInteiros[i+1]
        vVetorMultiplicaAdjacentes.append(vAuxiliarEsquerda * vAuxiliarDireita)
    return vVetorMultiplicaAdjacentes

def fMaiorAdjacentes(pVetorInteiros):
    vAuxVetor = fVetorMultiplicaAdjacentes(pVetorInteiros)
    vAuxMaiorAdjacentes = -999999
    for i in vAuxVetor:
        if i > vAuxMaiorAdjacentes:
            vAuxMaiorAdjacentes = i
    return vAuxMaiorAdjacentes

def main():
    fLimpaTela()
    vVetorInteiros = []
    vQtdePosicoes = int(input("Informe a quantidade de posições do vetor/lista: "))
    for i in range(vQtdePosicoes):
        vAuxInsereVetor = int(input(f"{i+1}/{vQtdePosicoes}... informe o inteiro: "))
        vVetorInteiros.append(vAuxInsereVetor)
    print(f"\nOs maiores adjacentes resultam em: {fMaiorAdjacentes(vVetorInteiros)}\n")

main()