from menu import initial_menu, circle_menu, rectangle_menu, square_menu, triangle_menu

##nessa lógica, usarei um while e match case 

PI =  3.14159

def logic():
    while True:
        initial_menu() ##menu inicial
        initial_user_select = int(input("Digite sua seleção")) ## seleção do usuario
        match initial_user_select:
            case 1:
                triangle_menu()
                triangle_user_base = float(input("Digite o valor da base:"))
                triangle_user_height = float(input("Digite o valor da altura:"))
                print(f"O valor da área do triangulo é: {(triangle_user_base*triangle_user_height)/2}")
                break
            case 2: 
                rectangle_menu()
                rectangle_user_base = float(input("Digite o valor da base:"))
                rectangle_user_height = float(input("Digite o valor da altura: "))
                print(f"O valor da área do retangulo é:{rectangle_user_base*rectangle_user_height}")
                break
            case 3:
                square_menu()
                square_user_side = float(input("Digite o valor do lado do quadrado: "))
                print(f"O valor da área do quadrado é: {square_menu*square_menu}")
                break
            case 4: 
                circle_menu()
                circle_user_raio = float(input("Digite o valor do raio do circulo: "))
                print(f"O valor da área do raio é {PI*(circle_user_raio**2)}")
                break
            case _:
                print("Valor inválido")
        

