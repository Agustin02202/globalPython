import random

class Detector:
    def __init__(self, matriz_adn, secuencia_a_buscar = "ATCG"):
        self.matriz_adn = matriz_adn
        self.secuencia_a_buscar = secuencia_a_buscar

    def detectar_mutantes_horizontal(self):
        for fila in self.matriz_adn:
            for i in range(len(fila) - 3):
             if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                return True
        return False
    def detectar_mutantes_vertical(self):
        for j in range(len(self.matriz_adn[0])):  # Iterar sobre las columnas
            columna = [fila[j] for fila in self.matriz_adn]  # Crear una lista con los elementos de la columna
            for i in range(len(columna) - 3):
                if columna[i] == columna[i+1] == columna[i+2] == columna[i+3]:
                    return True
            return False

    def detectar_mutantes_diagonal(self):
        n = len(self.matriz_adn)
        for i in range(n - 3):  # Iteramos hasta n-3 para asegurar que tengamos al menos 4 elementos en la diagonal
            # Diagonales principales
            for j in range(n - i - 3):
                if all(self.matriz_adn[i + k][j + k] == self.matriz_adn[i][j] for k in range(4)):
                    return True
            # Diagonales secundarias
            for j in range(i + 3, n):
                if all(self.matriz_adn[i + k][j - k] == self.matriz_adn[i][j] for k in range(4)):
                    return True
        return False

    def detectar_mutantes(self):
        return self.detectar_mutantes_horizontal() or self.detectar_mutantes_vertical() or self. detectar_mutantes_diagonal()

class Mutador:
    def __init__(self, base_nitrogenada, matriz_adn):
        self.base_nitrogenada = base_nitrogenada
        self.matriz_adn = matriz_adn

    def crear_mutante(self):
        """Método base, debe ser implementado por las clases hijas."""
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, adn_original):
        super().__init__(base_nitrogenada, adn_original)

    def crear_mutante(self, adn_original, posicion_inicial, orientacion_de_la_mutacion):
        try:
            fila, columna = posicion_inicial
            if orientacion_de_la_mutacion == "H":
                if columna + 3 >= len(adn_original[0]):
                    raise IndexError("La mutación se sale de los límites de la matriz.")
                for i in range(4):
                    adn_original[fila][columna + i] = self.base_nitrogenada
            elif orientacion_de_la_mutacion == "V":
                if fila + 3 >= len(adn_original):
                    raise IndexError("La mutación se sale de los límites de la matriz.")
                for i in range(4):
                    adn_original[fila + i][columna] = self.base_nitrogenada
            else:
                raise ValueError("Orientación inválida para Radiacion. Use 'H' o 'V'.")
        except IndexError as e:
            print(f"Error de índice: {e}")
        except ValueError as e:
            print(f"Error de valor: {e}")
        return adn_original

class Virus(Mutador):
    def __init__(self, base_nitrogenada, adn_original):
        super().__init__(base_nitrogenada, adn_original)

    def crear_mutante(self, adn_original, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            if fila + 3 >= len(adn_original) or columna + 3 >= len(adn_original[0]):
                raise IndexError("La mutación diagonal se sale de los límites de la matriz.")
            for i in range(4):
                adn_original[fila + i][columna + i] = self.base_nitrogenada
        except IndexError as e:
            print(f"Error de índice: {e}")
        return adn_original

class Virus(Mutador):
    def crear_mutante(self, adn_original, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            # Verificación más precisa de los límites
            if not (0 <= fila <= len(adn_original) - 4 and 0 <= columna <= len(adn_original[0]) - 4):
                raise IndexError("La mutación diagonal se sale de los límites de la matriz.")

            # Modificación para asegurar que siempre se muestren las últimas 4 posiciones
            for i in range(4):
                adn_original[fila + i][columna + i] = self.base_nitrogenada

        except IndexError as e:
            print(f"Error de índice: {e}")
        return adn_original
    
class Sanador:
    def __init__(self, matriz_adn, base_nitrogenada='ACGT'):
        self.matriz_adn = matriz_adn
        self.base_nitrogenada=base_nitrogenada

    def sanar_mutantes(self):
        """Genera un nuevo ADN aleatorio si se detectan mutaciones."""
        if Detector(self.matriz_adn).detectar_mutantes():
            return self.generar_nuevo_adn()
        return self.matriz_adn

    def generar_nuevo_adn(self):
        while True:
            # Genera un nuevo ADN de forma aleatoria
            nuevo_adn = [[random.choice(self.base_nitrogenada) for i in range(6)] for j in range(6)]
            detector = Detector(nuevo_adn)
            if detector.detectar_mutantes():
                # Si no tiene mutaciones, devuelve el nuevo ADN
                continue
            else:
                return nuevo_adn