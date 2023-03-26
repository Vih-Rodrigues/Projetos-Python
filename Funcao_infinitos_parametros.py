"""
Python: Elabore uma aplicação que receba um número indeterminado de valores informados pelo usuário.
Crie funções para determinar:
• Quantidade de números pares
• Quais são os números ímpares
• O maior número
• O menor número
• A média dos números
Apresente os resultados na tela.
"""
import os

def limpaTela():
    os.system('cls')

def fPares(lista):
    contPares = 0
    for i in lista:
        if i % 2 == 0:
            contPares += 1
    return contPares

def fImpares(lista):
    vImpares = ' - '.join(str(x) for x in lista if x % 2 != 0)
    return vImpares

def fMaior(lista):
    return max(lista)

def fMenor(lista):
    return min(lista)

def fMedia(lista):
    return (sum(lista)) / (len(lista))

def main():
    limpaTela()
    vLista = []
    vAuxiliar = 1
    print("A seguir, informe os valores que entrarão na lista.\nPara sair informe 0.")
    while vAuxiliar != 0:
        try:
            vAuxiliar = int(input("> "))
            if vAuxiliar == 0:
                break
            vLista.append(vAuxiliar)
        except ValueError:
            print("Valor inválido!")
    print(f"Quantidade de pares: {fPares(vLista)}")
    print(f"Ímpares: {fImpares(vLista)}")
    print(f"Maior valor da lista: {fMaior(vLista)}")
    print(f"Menor valor da lista: {fMenor(vLista)}")
    print(f"Média dos valores informados na lista: {fMedia(vLista)}")

main()