"""
Python: 
Faça um programa que leia um vetor de 15 posições de números inteiros e divida todos os seus elementos pelo maior valor do vetor.
Mostre o vetor após os cálculos.
"""
import os

def fLimpaTela():
    os.system('cls')

def fMaior(pVetor):
    vAuxMaior = -999999
    for i in pVetor:
        if i > vAuxMaior:
            vAuxMaior = i
    return vAuxMaior

def fNovoVetor(pVetor):
    vAuxMaior = fMaior(pVetor)
    print("\nNovo vetor:")
    for i in pVetor:
        print(f"\n{i/vAuxMaior}")

def main():
    fLimpaTela()
    vVetor = []
    for i in range(15):
        vAuxInteiro = int(input(f"{i+1}/15 ...Informe um inteiro: "))
        vVetor.append(vAuxInteiro)
    fNovoVetor(vVetor)

main()