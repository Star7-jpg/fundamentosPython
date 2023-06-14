comidas = []

def show_comidas():
    for comida in comidas:
        print(f"comida {comida}")
        
def add_comidas(comida):
    comidas.append(comida)
        
def del_comidas(comida):
    try:
        comidas.remove(comida)
    except Exception:
        print("No se encuentra en la lista")
        
text_menu = '''
Elige una opción:
    1- Agregar comida
    2- Eliminar comida
    3- Mostar comida
    4- Salir
'''

while True:
    choice_user = int(input(text_menu))
    if choice_user == 1:
        comida = input("Escriba una comida: ")
        add_comidas(comida)
    elif choice_user == 2: 
        comida = input("Escriba una comida: ")
        del_comidas(comida)
    elif choice_user == 3:
        show_comidas()
    elif choice_user == 4:
        break
    else:
        print("Escribe bien:/")