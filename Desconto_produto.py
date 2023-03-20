"""
Python: Desconto produto
Elabore uma aplicação que receba o nome de um produto e o seu valor.
O desconto deve ser calculado de acordo com o valor fornecido conforme a Tabela.
________________________________
Valor (R$)        | Desconto(%) |
>= 50 e < 200     |      5      |
>= 200 e < 500    |      6      |
>= 500 e < 1000   |      7      |
>= 1000           |      8      |
________________________________
Apresente em tela o nome do produto, valor original do produto e o novo valor depois de ser realizado o desconto.
Caso o valor digitado seja menor que zero, deve ser emitida uma mensagem de aviso.
"""
import os
os.system('cls')

varValidaValor = False
while varValidaValor == False:
    nomeProduto = input("Nome do produto: ")
    precoProduto = float(input("Preço (R$): "))

    if precoProduto < 0:
        print("TRAPACEIRO(A)! Informe os dados novamente.")
        varValidaValor = False
    else:
        varValidaValor = True

if precoProduto >= 50 and precoProduto < 200:
    novoPreco = (precoProduto * 0.05)

elif precoProduto >= 200 and precoProduto < 500:
    novoPreco = (precoProduto * 0.06)

elif precoProduto >= 500 and precoProduto < 1000:
    novoPreco = (precoProduto * 0.07)

else:
    novoPreco = (precoProduto * 0.08)

novoPreco = (precoProduto - novoPreco)

print("\nProduto: ", nomeProduto, "\nPreço original: R$", precoProduto, "\nPreço com desconto: R$", novoPreco)