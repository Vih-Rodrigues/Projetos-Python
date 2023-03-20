"""
Python: Função com indeterminados parâmetros
"""
import os

def limpaTela():
    os.system('cls')

def fPares(lista):
    contPares = 0
    for i in lista:
        if lista[i] % 2 == 0:
            contPares =+ 1
    return contPares

def fImpares(lista):
    contImpares = 0
    for i in lista:
        if lista[i] % 2 != 0:
            contImpares =+ 1
    return contImpares

def fMaior(lista):
    return max(lista)

def fMenor(lista):
    return min(lista)

def fMedia(lista):
    return (sum(lista)) / (len(lista))

def main():
    limpaTela()
    numLista = int(input("Informe os valores que entrarão na lista: "))
    print(f"Pares: {qtdPares(numLista)}")

main()