import random

class Detector:
    def __init__(self, adn, longitud_mutante=4):
        #Constructor de la clase Detector.
        #adn: Lista de listas que representa la matriz de ADN.
        #longitud_mutante: Número mínimo de caracteres consecutivos iguales para identificar una mutación.
        self.adn = adn
        self.longitud_mutante = longitud_mutante
    
    #Detecta si hay mutantes en la matriz de ADN en direcciones horizontal, vertical y diagonal.
    def detectar_mutaciones(self):    
        #True si se encuentra una mutación, False en caso contrario.
        encontrado =(self._verificar_horizontal() or self._verificar_vertical() or self._verificar_diagonal())
        return encontrado
    
    #Verifica mutantes en las filas
    def _verificar_horizontal(self):
        for fila in self.adn:
            if self._verificar_secuencia(fila):
                return True
        return False
    
    #Verifica mutantes en las columnas
    def _verificar_vertical(self):    
        num_columnas = len(self.adn[0])
        for col in range(num_columnas):
            columna = [fila[col] for fila in self.adn]
            if self._verificar_secuencia(columna):
                return True
        return False
    
    #Verifica mutantes en las diagonales
    def _verificar_diagonal(self):
        num_filas = len(self.adn)
        num_columnas = len(self.adn[0])

        # Diagonales de izquierda a derecha
        for i in range(num_filas - self.longitud_mutante + 1):
            for j in range(num_columnas - self.longitud_mutante + 1):
                diagonal = [self.adn[i + k][j + k] for k in range(self.longitud_mutante)]
                if self._verificar_secuencia(diagonal):
                    return True

        # Diagonales de derecha a izquierda
        for i in range(num_filas - self.longitud_mutante + 1):
            for j in range(self.longitud_mutante - 1, num_columnas):
                diagonal = [self.adn[i + k][j - k] for k in range(self.longitud_mutante)]
                if self._verificar_secuencia(diagonal):
                    return True

        return False
    
    #Verifica si en una secuencia de ADN existen caracteres consecutivos iguales que indiquen mutación
    def _verificar_secuencia(self, secuencia):    
        #secuencia: Lista de caracteres de ADN.
        #True si hay una secuencia mutante, False en caso contrario.
        for i in range(len(secuencia) - self.longitud_mutante + 1):
            if len(set(secuencia[i:i + self.longitud_mutante])) == 1:
                return True
        return False

class Mutador:
    def __init__(self, base_nitrogenada, adn_original):
        self.base_nitrogenada = base_nitrogenada  # Base que se repetirá 4 veces
        self.adn_original = adn_original          # ADN original sin mutaciones

    def crear_mutante(self):
        pass

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, adn_original):
        super().__init__(base_nitrogenada, adn_original)

    def crear_mutante(self, adn_original, posicion_inicial, orientacion_de_la_mutacion):
        try:
            fila, columna = posicion_inicial
            fila = fila-1
            columna = columna-1
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
            fila = fila -1
            columna = columna -1
            if fila + 3 >= len(adn_original) or columna + 3 >= len(adn_original[0]):
                raise IndexError("La mutación diagonal se sale de los límites de la matriz.")
            for i in range(4):
                adn_original[fila + i][columna + i] = self.base_nitrogenada
        except IndexError as e:
            print(f"Error de índice: {e}")
        return adn_original

class Sanador:
    def __init__(self, adn, bases):
        self.adn = adn
        self.bases = bases
    
    def sanar_mutaciones(self):
        if Detector(self.adn):
            return self.generar_nuevo_adn()
        return self.adn
        
    def generar_nuevo_adn(self):
        while True:
            # Genera un nuevo ADN de forma aleatoria
            nuevo_adn = [[random.choice(self.bases) for i in range(6)] for j in range(6)]
            
            # Usa Detector para verificar si el nuevo ADN tiene mutaciones
            detector = Detector(nuevo_adn)
            if detector.detectar_mutaciones() == False:
                # Si no tiene mutaciones, devuelve el nuevo ADN
                return nuevo_adn    