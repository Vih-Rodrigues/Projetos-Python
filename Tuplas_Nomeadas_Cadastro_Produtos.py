"""
Python: 
Faça um programa que receba o nome de cinco produtos e seus respectivos preços, calcule e mostre:
- a quantidade de produtos com preço inferior a R$ 50,00
- o nome dos produtos com preço entre R$ 50,00 e R$ 100,00
- a média dos preços dos produtos com preço superior a R$ 100,00
"""
import os
import collections

def fLimpaTela():
    os.system('cls')

def fQtdeProdutosAte49(pVetorProdutos):
    vAuxProdutosAte49 = 0
    for i in pVetorProdutos:
        if i.preco < 50:
            vAuxProdutosAte49 += 1
    return vAuxProdutosAte49

def fProdutosEntre50e100(pVetorProdutos):
    print("\nProdutos com preço entre R$50,00 e R$100,00:")
    for i in pVetorProdutos:
        if i.preco >= 50 and i.preco <= 100:
            print(i.nome)

def fMediaPrecoProdutosSuperior100(pVetorProdutos):
    vAuxMediaPrecoProdutosSuperior100 = 0
    vAuxPrecoTotal = 0
    vAuxQtdeProdutos = 0
    for i in pVetorProdutos:
        if i.preco > 100:
            vAuxPrecoTotal += i.preco
            vAuxQtdeProdutos += 1
    vAuxMediaPrecoProdutosSuperior100 = vAuxPrecoTotal / vAuxQtdeProdutos
    return vAuxMediaPrecoProdutosSuperior100

def main():
    fLimpaTela()
    Produtos = collections.namedtuple("Produto", "nome preco")
    vVetorProdutos = []
    for i in range(5):
        vAuxNome = input("Nome do produto: ")
        vAuxPreco = float(input("Preço: R$"))
        vVetorProdutos.append(Produtos(vAuxNome, vAuxPreco))
    print(f"\nQuantidade de produtos com preço inferior a R$50,00: {fQtdeProdutosAte49(vVetorProdutos)}")
    fProdutosEntre50e100(vVetorProdutos)
    print(f"\nMédia dos preços dos produtos com preço superior a R$ 100,00: R$ {fMediaPrecoProdutosSuperior100(vVetorProdutos)}")
    print("\n")

main()