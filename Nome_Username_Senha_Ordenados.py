"""
Python: Usernames
Faça um programa capaz de gerar usernames e senhas para alunos da FATEC de Ribeirão Preto.
O programa recebe como entrada o nome completo do aluno e produzir um username contendo:
• A primeira letra do nome e o sobrenome
O resultado deve ser armazenado em um estrutura da sua preferência: Tupla, Lista, Dicionário ou Conjunto.
O programa deve garantir que não sejam gerados username duplicados
As senhas provisórias deve conter no mínimo 8 caracteres (números, letras e símbolos) com máxima segurança.
Permita a exibição dos dados na tela conforme a seguinte tabela, ordenados por nome:
Nome | Username | Password
"""
import os

def fLimpaTela():
    os.system('cls')

def fGeraUsernamePadrao(pNomeCompleto):
    # Transforma a string recebida no username padrão primeironome.ultimosobrenome
    vPrimeiraLetraNome = pNomeCompleto[0]
    vNomeSeparado = pNomeCompleto.split()
    vUltimoSobrenome = vNomeSeparado[-1]
    vUsernameTemp = vPrimeiraLetraNome + "." + vUltimoSobrenome
    return vUsernameTemp.lower()

def fContaUsernamesIguais(pUsernameTemp, pListaUsernames):
    # Valida a lista de alunos pelos seus username padrão primeironome.ultimosobrenome
    vContador = -1
    for i in pListaUsernames:
        if pUsernameTemp == i:
            vContador += 1
    return vContador

def fGeraUsernameComNumero(pContador, pUsernameGerado):
    if pContador != 0:
        vUsernameFinal = pUsernameGerado + str(pContador) + "@fatec.sp.gov.br"
    else:
        vUsernameFinal = pUsernameGerado + "@fatec.sp.gov.br"
    return vUsernameFinal

def fListaCadastros(pListaNomes, pListaEmails, pListaPassword):
    print("\n\nNome             |Username           |Password")
    for i in range(len(pListaNomes)):
        print(pListaNomes[i] + "|" + pListaEmails[i] + "|" + pListaPassword[i])

def main():
    fLimpaTela()
    vListaNomes = []
    vListaPaswords = []
    vListaUsernames = []
    vListaEmails = []
    vQtdeAlunosRegistrados = int(input("Informe quantos alunos serão registrados: "))
    for i in range(vQtdeAlunosRegistrados):
        vNomeCompleto = input("\nInforme o nome completo: ")
        vListaNomes.append(vNomeCompleto)
        vSenha = input("Informe a senha, a mesma deve atender aos seguintes requisitos:\n- mínimo 8 caracteres\n- Números\n- Letras\n- Símbolos\n: ")
        vListaPaswords.append(vSenha)
        vUsername = fGeraUsernamePadrao(vNomeCompleto)
        vListaUsernames.append(vUsername)
        vContadorUsernameIguais = fContaUsernamesIguais(vUsername, vListaUsernames)
        vUsernameFinal = fGeraUsernameComNumero(vContadorUsernameIguais, vUsername)
        vListaEmails.append(vUsernameFinal)
        print(f"\nSeu username é: {vUsernameFinal}")
    fListaCadastros(vListaNomes, vListaEmails, vListaPaswords)
    print("\n")

main()