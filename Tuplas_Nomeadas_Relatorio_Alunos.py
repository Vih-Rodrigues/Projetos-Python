"""
Python: Relatório de Notas com tupla nomeada
Faça um programa que receba o nome e duas notas de seis alunos e mostre o relatório abaixo:

Relatório de notas:
Aluno   1º Prova    2º Prova    Média   Situação
Carlos    8,0         9,0        8,5    Aprovado
Pedro     4,0         5,0        4,5    Reprovado

Média da classe = 
Quantidade de aprovados = %
Quantidade de alunos de exame = %
Quantidade de reprovados = %
"""
import os
import collections

def fLimpaTela():
    os.system('cls')

def fMedia(pAluno):
    vAuxMedia = 0
    for i in pAluno:
        vAuxMedia = vAuxMedia + i.media
    vAuxMedia = vAuxMedia / 6
    return vAuxMedia

def fQtdeAprovados(pAluno):
    vAuxQtdeAprovados = 0
    for i in pAluno:
        if i.situacao == "Aprovado":
            vAuxQtdeAprovados += 1
    return vAuxQtdeAprovados / 0.06

def fQtdeAlunosReprovados(pAluno):
    vAuxQtdeReprovados = 0
    for i in pAluno:
        if i.situacao == "Reprovado":
            vAuxQtdeReprovados += 1
    return vAuxQtdeReprovados / 0.06

def fMostraRelatorio(pAluno):
    print("Relatório de notas:")
    print("|    Aluno   |   1º Prova    |   2º Prova    |   Média   |   Situação    |")
    for i in pAluno:
        print(f"|   {i.nome}    |   {str(i.nota1)}   |   {str(i.nota2)}   |   {str(i.media)}  |   {i.situacao}    |")
    print(f"\nMédia da classe: {fMedia(pAluno)}")
    print(f"Quantidade de alunos aprovados: {fQtdeAprovados(pAluno)} %")
    print(f"Quantidade de alunos reprovados: {fQtdeAlunosReprovados(pAluno)} %")

def main():
    fLimpaTela()
    Alunos = collections.namedtuple("Aluno", "nome nota1 nota2 media situacao") # Tupla nomeada
    vAluno = []
    for i in range(6):
        vAuxNome = input("\nNome do aluno: ")
        vAuxNota1 = float(input("Nota 1º prova: "))
        vAuxNota2 = float(input("Nota 2º prova: "))
        vAuxMedia = ((vAuxNota1 + vAuxNota2) / 2)
        if vAuxMedia >= 6:
            vAuxSituacao = "Aprovado"
        else:
            vAuxSituacao = "Reprovado"
        vAluno.append(Alunos(vAuxNome, vAuxNota1, vAuxNota2, vAuxMedia, vAuxSituacao))
    print("\n")
    fMostraRelatorio(vAluno)

main()