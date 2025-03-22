from menu import initial_menu, circle_menu, rectangle_menu, square_menu, triangle_menu
##importação de funções que exibem os menus do arquivo menu.py

##nessa lógica, usarei um while e match case 

PI =  3.14159 ##constante PI


def logic():
    while True:
        initial_menu() ##menu inicial
        initial_user_select = int(input("Digite sua seleção")) ## seleção inicial do usuário
        match initial_user_select:
            case 0:
                print("Encerrando o programa") 
                break
            ##caso o usuario digite 0, o programa encerra
            case 1:
                triangle_menu()
                triangle_user_base = float(input("Digite o valor da base:"))
                triangle_user_height = float(input("Digite o valor da altura:"))
                print(f"O valor da área do triangulo é: {(triangle_user_base*triangle_user_height)/2}")
            ##caso o usuário digite 1, calcula a área do tringulo
            case 2: 
                rectangle_menu()
                rectangle_user_base = float(input("Digite o valor da base:"))
                rectangle_user_height = float(input("Digite o valor da altura: "))
                print(f"O valor da área do retangulo é:{rectangle_user_base*rectangle_user_height}")
            ##caso o usuário digite 2, calcula a área do retangulo 
            case 3:
                square_menu()
                square_user_side = float(input("Digite o valor do lado do quadrado: "))
                print(f"O valor da área do quadrado é: {square_user_side*square_user_side}")
            ##caso o usuário digite 3, calcular a área do quadrado 
            case 4: 
                circle_menu()
                circle_user_raio = float(input("Digite o valor do raio do circulo: "))
                print(f"O valor da área do raio é {PI*(circle_user_raio**2)}")
            ##caso o usuário digite 4, calcula a área do circulo
            case _:
                print("Valor inválido")
                break
            ##caso o usuário digite algo que não possa digitar, o programa quebra
        

