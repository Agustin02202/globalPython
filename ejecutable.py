from clases import *  #Importamos las clases de clses.py

def validar_adn(adn):
    """Validar que el ADN tenga solo 6 caracteres A, T, C, G."""
    return len(adn) == 6 and all(base in 'ATCG' for base in adn.upper())

def ingresar_adn():
    """Permite al usuario ingresar 6 líneas de ADN y las valida."""
    matriz_adn = []
    print("Coloca una línea de ADN (6 caracteres, A, T, C, G)")
    while len(matriz_adn) < 6:
        adn = input("Colocar linea de ADN: ").upper()
        if validar_adn(adn):
            matriz_adn.append(list(adn))
            print(f"Línea añadida: {adn}")
        else:
            print("Entrada inválida. Intenta de nuevo.")
    return matriz_adn


def imprimir_matriz_adn(matriz_adn):
    """Imprime la matriz de ADN"""
    for fila in matriz_adn:
        print(" ".join(fila))

def aplicar_mutacion(adn, base_nitrogenada, posicion_inicial, orientacion):
    if orientacion == "H" or orientacion == "V":
        mutador = Radiacion(base_nitrogenada, adn)
        adn_mutado = mutador.crear_mutante(adn, posicion_inicial, orientacion)
    elif orientacion == "D":
        mutador = Virus(base_nitrogenada, adn)
        adn_mutado = mutador.crear_mutante(adn, posicion_inicial)
    else:
        print("Orientación no válida. Use 'H' para horizontal, 'V' para vertical o 'D' para diagonal.")
    return adn_mutado

# Ingresar ADN al inicio
print("Bienvenido. Primero, ingresa el ADN (6 líneas de 6 caracteres).")
matriz_adn = ingresar_adn()
imprimir_matriz_adn(matriz_adn)

# Menú de opciones
while True:
    print("\nSelecciona una opción:")
    print("1: Detectar mutación")
    print("2: Mutarlo")
    print("3: Sanarlo")
    print("4: Salir")

    opcion = input("Elige una opción (1, 2, 3 o 4): ")

    if opcion == '1':
        # Detectar mutación
        print("Detectando mutación...")
        detector = Detector(matriz_adn)
        if detector.detectar_mutantes():
            print("Se detectó una mutación.")
        else:
            print("No se detectaron mutaciones.")


    elif opcion == '2':
        while True:    
            # Mutar el ADN
            print("Mutando el ADN...")
            tipo_mutador = input("Selecciona el tipo de mutador (1: Radiación, 2: Virus): ")

            if tipo_mutador == '1':
                # Mutador de tipo Radiación
                base_nitrogenada = input("Introduce la base nitrogenada (A, T, C, G): ").upper()
                fila = int(input("Fila de la posición inicial: "))
                columna = int(input("Columna de la posición inicial: "))
                orientacion = input("Orientación de la mutación (H para horizontal, V para vertical): ").upper()
                # Crear la instancia de la clase Radiacion sin el argumento innecesario
                mutador = Radiacion(base_nitrogenada, matriz_adn, fila, columna)
                # Crear el mutante
                matriz_mutada = mutador.crear_mutante(matriz_adn, orientacion)

                if matriz_mutada:
                    matriz_adn = matriz_mutada
                    print("ADN mutado:")
                    imprimir_matriz_adn(matriz_adn)
                    break
                else:
                    print("Error al mutar el ADN.")
                    break

            elif tipo_mutador == '2':  # Virus

                base_nitrogenada = input("Introduce la base nitrogenada (A, T, C, G): ").upper()
                fila = int(input("Fila de la posición inicial: "))
                columna = int(input("Columna de la posición inicial: "))
                mutador = Virus(base_nitrogenada, matriz_adn, fila, columna)
                # Crear el mutante
                matriz_mutada = mutador.crear_mutante(matriz_adn, fila, columna)

                if matriz_mutada:
                    matriz_adn = matriz_mutada
                    print("ADN mutado:")
                    imprimir_matriz_adn(matriz_adn)  # Imprimir la matriz después de mutarla
                    break
                else:
                    print("Error al mutar el ADN.")
                    break
            else: 
                print("Opción no valida, elija una de las opciones proporcionadas...")

    elif opcion == '3':
        # Se sana el adn
        print("Sanando el ADN...")
        sanador = Sanador(matriz_adn)
        matriz_adn = sanador.sanar_mutantes()
        print("ADN sanado:")
        imprimir_matriz_adn(matriz_adn)

    elif opcion == '4':
        # Salir
        print("Saliendo. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Elige una opción correcta.")