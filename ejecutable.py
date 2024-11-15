from clases import Detector,Mutador,Radiacion,Virus,Sanador
def validarAdn (adn):
    #funcion para validar los datos de entrada
    #contructor para que unicamente puedan entrar estos caracteres y convertimos en mayuscula si entra en minuscula
    adn_valido = set("ATCG")
    adn = adn.upper()

    return all(base in adn_valido for base in adn)


#Input para recibir la opcion que desea operar el usuario, y ejecutar la correcta
def ingresar_adn(cantidad):
    adn = []
    print("Introduce las secuencias de ADN para analizar mutaciones('A','T','G','C'):")

    for i in range(cantidad):
        secuencia = input(f"Secuencia {i + 1}:").upper()
        if len(secuencia) == 6 and validarAdn(secuencia):
            adn.append(secuencia)
        else:
            print("El adn contiene una cantidad equivocada, vuelve a intentarlo (solo 6 caracteres)")
            break
    return adn

#Convierte cada string en una lista de caracteres
def separar_adn(adn):
    adn_separado = []
    for secuencia in adn:
        adn_separado.append(list(secuencia))
    return adn_separado

#Aplica la mutacion dependiendo la orientacion seleccionada
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

def sanar_mutacion(adn,bases_validas):
    sanador = Sanador(adn, bases_validas)
    adn_curado = sanador.sanar_mutaciones()
    return adn_curado

#Pedir primero el ADN al Usuario
num_secuencias = 6
adn = ingresar_adn(num_secuencias)
adn_separado = separar_adn(adn)
bases_nitrogenadas = ('A','T','G','C')

for i in range(6):
   print(adn_separado[i])

opcion = 0
while opcion != 4:
    opcion = int(input("Que quiere realizar con el ADN \n1.Detectar Mutaciones \n2.Mutar \n3.Sanar \n4.Salir \n"))
    if opcion == 1:
        detector = Detector(adn_separado, 4)
        if detector.detectar_mutaciones():
            print("Mutante encontrado")
        else:
             print("Mutante no encontrado")
    elif opcion == 2:
        print("Mutando el ADN...")
        tipo_mutador = input("Selecciona el tipo de mutador (1: Radiación, 2: Virus): ")

        if tipo_mutador == '1':
            base_nitrogenada = input("Ingresa la base nitrogenada para la mutación (A, T, C o G): ").upper()
            posicion_inicial = (int(input("Ingresa la fila de inicio (1-6): ")), int(input("Ingresa la columna de inicio (1-6): ")))
            orientacion = input("Ingresa la orientación de la mutación ('H' para horizontal, 'V' para vertical): ").upper()
            mutador = Radiacion(base_nitrogenada, adn_separado)
            adn_separado = mutador.crear_mutante(adn_separado, posicion_inicial, orientacion)
            print("Mostrando ADN mutado")
            for i in range(6):
                print(adn_separado[i])
        if tipo_mutador	== '2':
            base_nitrogenada = input("Ingresa la base nitrogenada para la mutación (A, T, C o G): ").upper()
            posicion_inicial = (int(input("Ingresa la fila de inicio (1-6): ")), int(input("Ingresa la columna de inicio (1-6): ")))
            mutador = Virus(base_nitrogenada, adn)
            adn_separado = mutador.crear_mutante(adn_separado, posicion_inicial)
            print("Mostrando ADN mutado")
            for i in range(6):
                print(adn_separado[i])
    elif opcion == 3:
        print("Sanando ADN...")
        sanador = Sanador(adn,bases_nitrogenadas)
        adn_separado = sanador.sanar_mutaciones()
        print("ADN curado \nMostrando...")
        for i in range(6):
            print(adn_separado[i])
    elif opcion == 4:
        print("Saliendo del programa \n¡Muchas Gracias!")
    else :
        print("Opcion no valida")