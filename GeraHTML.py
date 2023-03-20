"""
Python: aplicação que gera o currículo de uma pessoa em HTML
"""
import os
import webbrowser

def fLimpaTela():
    os.system('cls')

def main():
    fLimpaTela()
    html = f"""
    <h1><b>Nome:</b> {input("Entre com o nome: ")}</h1>
    <h2><b>Endereço:</b> {input("Entre com o endereço: ")}</h2>
    <h3><b>Formação:</b> {input("Entre com a formação: ")}</h3>
    """
    arquivo = open("curriculo.html", "w") # w = write
    arquivo.write(html)
    arquivo.close()
    filename = 'file:///'+os.getcwd()+'/'+'curriculo.html'
    webbrowser.open_new_tab(filename)

main()