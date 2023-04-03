"""
Python: Usernames
Faça um programa capaz de gerar usernames e senhas para alunos da FATEC de Ribeirão Preto.
O programa recebe como entrada o nome completo do aluno e produzir um username contendo:
• A primeira letra do nome e o sobrenome
O resultado deve ser armazenado em um estrutura da sua preferência: Tupla, Lista, Dicionário ou Conjunto.
O programa deve garantir que não sejam gerados username duplicados
As senhas provisórias deve conter no mínimo 8 caracteres (números, letras e símbolos) com máxima segurança.
"""
import os

def fLimpaTela():
    os.system('cls')

def fGeraUsername(pNomeCompleto, pListaUsernames):
    # Transforma a string recebida no username padrão primeironome.ultimosobrenome
    vPrimeiraLetraNome = pNomeCompleto[0]
    vNomeSeparado = pNomeCompleto.split()
    vUltimoSobrenome = vNomeSeparado[-1]
    vUsernameTemp = vPrimeiraLetraNome + "." + vUltimoSobrenome + "@fatec.sp.gov.br"
    # Aqui começa a validação da lista de alunos
    vContador = 1
    for i in pListaUsernames:
        if vUsernameTemp == i:
            vUsernameTemp = vUsernameTemp + str(vContador)
            vContador += 1
    vUsernameFinal = vUsernameTemp
    pListaUsernames.append(vUsernameFinal)
    return vUsernameFinal

def main():
    fLimpaTela()
    vListaUsernames = []
    vQtdeAlunosRegistrados = int(input("Informe quantos alunos serão registrados: "))
    for i in range(vQtdeAlunosRegistrados):
        vNomeCompleto = input("\nInforme o nome completo: ")
        vSenha = input("Informe a senha, a mesma deve atender aos seguintes requisitos:\n- mínimo 8 caracteres\n- Números\n- Letras\n- Símbolos\n: ")
        print(f"Seu username é: {fGeraUsername(vNomeCompleto, vListaUsernames)}")

main()