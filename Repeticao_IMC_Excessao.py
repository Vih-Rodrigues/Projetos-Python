"""
Python: Elabore uma aplicação que receba o peso e altura de um número indeterminado de pessoas.
Utilize tratamento de exceção para garantir que os valores informados são válidos.
Após a entrada correta dos dados apresente o IMC.
Para cada entrada de dados pergunte ao usuário “Deseja continuar?”
"""
import os

def fLimpaTela():
    os.system('cls')

def fCalculaIMC(pAltura, pPeso):
    vIMC = (pPeso / ((pAltura/100) * (pAltura/100)))
    if vIMC <= 18.5:
        vRetornoIMC = (str("\nIMC = %.2f\nAbaixo do peso." %vIMC))
    elif vIMC > 18.5 and vIMC <= 24.9:
        vRetornoIMC = (str("\nIMC = %.2f\nPeso normal." %vIMC))
    elif vIMC > 24.9 and vIMC <= 29.9:
        vRetornoIMC = (str("\nIMC = %.2f\nAcima do peso." %vIMC))
    elif vIMC > 29.9 and vIMC <= 34.9:
        vRetornoIMC = (str("\nIMC = %.2f\nObesidade grau I." %vIMC))
    elif vIMC > 34.9 and vIMC <= 39.9:
        vRetornoIMC = (str("\nIMC = %.2f\nObesidade grau II." %vIMC))
    else:
        vRetornoIMC = (str("\nIMC = %.2f\nObesidade grau II." %vIMC))
    return vRetornoIMC

def main():
    fLimpaTela()
    while True:
        try:
            vAltura = float(input("\nInforme a altura em centímetros: "))
            vPeso = float(input("Informe o peso: "))
            print(fCalculaIMC(vAltura, vPeso))
        except ValueError:
            print("Valor inválido!")

main()