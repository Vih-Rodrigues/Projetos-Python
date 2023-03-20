"""
Python: conversão, string, função //, input/output.
"""
import math
import decimal
import os
os.system("cls")

# Conversões
y = 12
print("binario =" + bin(y))
print("hexa =" + hex(y))
print("octal =" + oct(y))

z = "25"
w = 3 + int(z)
print(w)

# String - cadeia/lista de caracteres
s = "João da Silva"
print(s[0])
print(s[1])
print(s[:4]) # Imprimi em tela do primeiro ao 3º caractere
print(s[5:7]) # Imprimi em tela do 5º ao 6º caractere
print(s[0]*20) # multiplica o que estiver na primeira posição 20 vezes
print("a" in s) # retorna um booleano
print("x" not in s) # retorna um booleano

print("\n")

s = "Abcdefg   "
print(chr(65)) # Retorna o caractere da tabela ASCII correspondente ao número 65
print(ord(s[0])) # Retorna o número da tabela ASCII correspondente ao caractere passado como parâmetro
print(repr(s)) # representação explícita
print(len(s)) # retorna número de bytes da string
print(len(s.strip())) # retira espaços, tabs e newlines
print(s.upper()) # Maiúsculas
print(s.lower()) # minusculas
print(s.capitalize()) # Primeira Maiúscula Por Paravra

print("\n")

# função //
a = 2
b = 3
print(a//b) # Pega só a parte inteira! 0,6 -> 0

# Entrada e Saída de dados
#Entrada
num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))

soma = (num1+num2)

# Saída
print("Soma = %.2f" %soma)
print("Soma = ", soma)
print("Soma = {0}".format(soma))
print(f"Soma = {soma}")

print("\n")

strTeste = "Vitoria"
for v in strTeste:
    print(v, end=' * ')