"""
Pyhton: Palindromo
Create a function checkPalindrome that given the string, check if it is a palindrome.
Example
• For inputString = "aabaa", the output should be checkPalindrome(inputString) = true;
• For inputString = "abac", the output should be checkPalindrome(inputString) = false;
• For inputString = "a", the output should be checkPalindrome(inputString) = true.
"""
import os

def fLimpaTela():
    os.system('cls')

def fVerificaSeEPalindromo(pLista):
    vListaReversa = []
    for caractere in reversed(pLista):
        vListaReversa.append(caractere)
    return vListaReversa

def main():
    fLimpaTela()
    vLista = []
    vSair = False
    while(vSair != True):
        vMenu = input("*** Verifique se é palíndromo ***\nEscolha:\n[1] - Digitar nova palavra\n[0] - Sair\n: ")
        if vMenu == "1":
            vSair = False
            vStringAuxiliar = input("Digite: ")
            for caractere in vStringAuxiliar:
                vLista.append(caractere)
            # uma forma de verificar é utilizando o operador de fatiamento:
            #if vLista == vLista[::-1]: # [::-1] -> inverte os caracteres da lista original
            if vLista == fVerificaSeEPalindromo(vLista):
                print("É palíndromo!\n")
            else:
                print("Não é palíndromo.\n")
        else:
            vSair = True

main()