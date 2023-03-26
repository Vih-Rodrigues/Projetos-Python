"""
Python: Elabore uma aplicação capaz de gerar o currículo de uma pessoa em HTML.
Os parâmetros para o currículo são: nome, endereço, telefone, e-mail, escolaridade e experiência profissional.
Você pode utilizar as tags HTML da sua preferência.
Utilize funções para organizar o código fonte da aplicação.
"""
import os
import webbrowser

def fLimpaTela():
    os.system('cls')

def main():
    fLimpaTela()
    html = f"""
    <h1><b>Nome:</b> {input("Entre com o nome: ")}</h1>
    <h2><b>Formação:</b> {input("Entre com a formação: ")}</h2>
    <h3><b>Endereço:</b> {input("Entre com o endereço: ")}</h3>
    <h3><b>Telefone:</b> {input("Entre com o telefone: ")}</h3>
    <h3><b>Email:</b> {input("Entre com o email: ")}</h3>
    <h3><b>Experiência:</b> {input("Entre com a experiência profissional: ")}</h3>
    """
    arquivo = open("curriculo.html", "w") # w = write
    arquivo.write(html)
    arquivo.close()
    filename = 'file:///'+os.getcwd()+'/'+'curriculo.html'
    webbrowser.open_new_tab(filename)

main()