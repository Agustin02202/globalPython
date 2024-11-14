import random


class Detector:
    def __init__(self, matriz_adn, secuencia_a_buscar = "ATCG"):
        self.matriz_adn = matriz_adn
        self.secuencia_a_buscar = secuencia_a_buscar

    def detectar_mutantes_horizontal(self):
        for fila in self.matriz_adn:
            fila_str = ''.join(fila)  # Convertir la fila en una cadena
            if self.secuencia_a_buscar in fila_str:
                return True
        return False

    def detectar_mutantes_vertical(self):
        # Transponemos la matriz para analizar columnas como filas
        list(zip(*self.matriz_adn))
        return self.detectar_mutantes_horizontal()

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
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada, matriz_adn)

    def crear_mutante(self, posicion_inicial, orientacion):
        """Realiza una mutación horizontal o vertical."""
        fila, col = posicion_inicial
        if orientacion == "H":
            if col + 3 < 6:
                for i in range(4):
                    self.matriz_adn[fila][col + i] = self.base_nitrogenada
        elif orientacion == "V":
            if fila + 3 < 6:
                for i in range(4):
                    self.matriz_adn[fila + i][col] = self.base_nitrogenada
        return self.matriz_adn


class Virus(Mutador):
    def __init__(self, base_nitrogenada, matriz_adn):
        super().__init__(base_nitrogenada, matriz_adn)

    def crear_mutante(self, posicion_inicial):
        """Realiza una mutación diagonal (↘ o ↙)."""
        fila, col = posicion_inicial
        # Mutación diagonal derecha (↘)
        if fila + 3 < 6 and col + 3 < 6:
            for i in range(4):
                self.matriz_adn[fila + i][col + i] = self.base_nitrogenada
        # Mutación diagonal izquierda (↙)
        if fila + 3 < 6 and col - 3 >= 0:
            for i in range(4):
                self.matriz_adn[fila + i][col - i] = self.base_nitrogenada
        return self.matriz_adn


class Sanador:
    def __init__(self, matriz_adn):
        self.matriz_adn = matriz_adn

    def sanar_mutantes(self):
        """Genera un nuevo ADN aleatorio si se detectan mutaciones."""
        if Detector(self.matriz_adn).detectar_mutantes():
            return self.generar_nuevo_adn()
        return self.matriz_adn

    def generar_nuevo_adn(self):
        """Genera un nuevo ADN aleatorio sin mutaciones."""
        bases = "ATCG"
        return [[random.choice(bases) for _ in range(6)] for _ in range(6)]