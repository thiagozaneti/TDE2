##Criação de arquivo de centralizacao de todos os menus

def initial_menu():
    print("""
        Seja bem vindo a calculadora de formas geométricas 
        --------------------------------------------------
        Qual área você deseja calcular?
        [1]Triangulo
        [2]Retangulo
        [3]Quadrado
        [4]Circulo
    """)
def triangle_menu():
    print("""
        Área do triangulo
        -----------------
        Digite o valor da base
        Digite o valor da altura
    """)
def rectangle_menu():
    print("""
        Área do retangulo
        -----------------
        Digite o valor da base
        Digite o valor da altura
""")

def square_menu():
    print("""
        Área do quadrado
        ----------------
        Digite o valor do lado
""")
    
def circle_menu():
    print("""
        Área do circulo
        ---------------
        Digite o valor do raio
""")