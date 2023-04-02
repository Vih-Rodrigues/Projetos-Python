"""
Python: Matriz
Uma imagem é formada por pixels.
Considere uma imagem com dimensão de 10 x 10 e faça uma aplicação que contenha um estrutura bidimensional com essas dimensões.
A seguir, para cada posição da estrutura bidimensional armazene um valor aleatório entre 0 e 255 (esses valores correspondem às tonalidades aplicadas sobre a imagem).
Apresente em tela os valores gerados.
"""
import os
import random

def fLimpaTela():
    os.system('cls')

def fPreencheImagem(pMatrizImagem):
    for i in range(10):
        vAuxiliar = random.randint(0, 255)
        pMatrizImagem.append(vAuxiliar)
    return pMatrizImagem

def fMostraMatriz(pMatrizImagem):
    for i in pMatrizImagem:
        print(pMatrizImagem)

def main():
    vMatrizImagem = []
    fLimpaTela()
    fPreencheImagem(vMatrizImagem)
    fMostraMatriz(vMatrizImagem)

main()