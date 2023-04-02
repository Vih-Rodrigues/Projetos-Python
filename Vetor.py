"""
Python: Vetor

Faça um programa que carregue um vetor de seis elementos numéricos inteiros, calcule e mostre:
• A quantidade de números pares
• Quais números são ímpares
• A soma dos números
• O maior número
• O menor número
• A quantidade de números positivos
"""
import os

def fLimpaTela():
    os.system('cls')

def fQtdeNumerosPares(pVetorNumerico):
    vAuxQtdePares = 0
    for i in pVetorNumerico:
        if i % 2 == 0:
            vAuxQtdePares += 1
    return vAuxQtdePares

def fNumerosImpares(pVetorNumerico):
    vAuxNumerosImpares = []
    for i in pVetorNumerico:
        if i % 2 != 0:
            vAuxNumerosImpares.append(i)
    return vAuxNumerosImpares

def fSoma(pVetorNumerico):
    return sum(pVetorNumerico)

def fMaior(pVetorNumerico):
    return max(pVetorNumerico)

def fMenor(pVetorNumerico):
    return min(pVetorNumerico)

def fQtdePositivos(pVetorNumerico):
    vAuxQtdePositivos = 0
    for i in pVetorNumerico:
        if i >= 0:
            vAuxQtdePositivos += 1
    return vAuxQtdePositivos

def fMostraVetor(pVetorNumerico):
    print(f"Vetor: {pVetorNumerico}\n")

def main():
    vVetorNumerico = []
    fLimpaTela()
    for i in range(6):
        vIntAux = int(input(f"{i+1}/6... Digite um número inteiro: "))
        vVetorNumerico.append(vIntAux)
    print("\n")
    fMostraVetor(vVetorNumerico)
    print(f"\nQuantidade de pares: {fQtdeNumerosPares(vVetorNumerico)}")
    print(f"\nNúmeros impares: {fNumerosImpares(vVetorNumerico)}")
    print(f"\nSoma: {fSoma(vVetorNumerico)}")
    print(f"\nMaior: {fMaior(vVetorNumerico)}")
    print(f"\nMenor: {fMenor(vVetorNumerico)}")
    print(f"\nQuantidade de positivos: {fQtdePositivos(vVetorNumerico)}\n")

main()