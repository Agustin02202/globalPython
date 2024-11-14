from clases import Detector

def validar_adn(adn):
    """Valida que una cadena de ADN tenga solo A, T, C, G."""
    return all(base in 'ATCG' for base in adn.upper())

def ingresar_adn():
    """Permite al usuario ingresar 6 líneas de ADN y las valida."""
    matriz_adn = []
    while len(matriz_adn) < 6:
        adn = input("Coloca una línea de ADN (solo A, T, C, G): ").upper()
        if len(adn) != 6:
            print("La línea debe tener exactamente 6 caracteres.")
        elif not validar_adn(adn):
            print("La línea debe contener solo A, T, C o G.")
        else:
            matriz_adn.append(list(adn))
            print(f"Línea añadida: {adn}")
    return matriz_adn


def menu(matriz_adn):
    """Muestra un menú de opciones y realiza las acciones correspondientes."""
    while True:
        print("\n1: Detectar mutante")
        print("2: Mutar ADN")
        print("3: Sanar ADN")
        print("4: Salir")
        opcion = input("Selecciona una opción: ")
        while True:
            # ... (menú)
            if opcion == '1':
                if detector.detectar_mutantes():
                    print("Se encontró una mutación.")
                    break
                else:
                    print("No se encontró ninguna mutación.")
                    break
            else:
                print("Opción inválida.")
                break
        break

# Obtener el ADN del usuario
matriz_adn = ingresar_adn()
# Crear una instancia de la clase Detector y pasarle la matriz de ADN
detector = Detector(matriz_adn)
# Mostrar el menú de opciones
menu(detector)