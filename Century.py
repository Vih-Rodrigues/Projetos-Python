"""
Python: Century
Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.
Example
• For year = 1905, the output should be centuryFromYear(year) = 20;
• For year = 1700, the output should be centuryFromYear(year) = 17.
"""
import math
import os
os.system('cls')

while True:
    try:
        ano = int(input("Entre com o ano: "))
        print(f"Ano {ano} seculo {math.ceil(ano/100)}")
    except ValueError:
        print("Valor inválido!")