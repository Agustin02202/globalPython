# Global Pyhton :snake:
# 🧬 Guía de Uso: Programa de Análisis de ADN

## 📌 Introducción
Este programa te permite analizar secuencias de ADN para detectar mutantes, realizar mutaciones o sanar cadenas de ADN mutadas.
El mismo cuenta con **dos archivos**:  
1. *ejecutable.py*: Script principal que permite interactuar con el programa, ingresar una secuencia de ADN y elegir entre detectar mutaciones, generar mutaciones o sanar el ADN.
2. *clases.py*: Contiene las clases Detector, Mutador, Radiacion, Virus y Sanador, cada una con métodos específicos para la manipulación y análisis de la secuencia de ADN.

---

## 🚀 **Iniciando el Programa**
1. **Da click** en el triángulo ubicado en la esquina superior derecha.  
   ![Imagen del Triángulo](image)
   O en su defecto, abre una terminal en el directorio del archivo y ejecuta el comando **python ejecutable.py**
   ![Imagen de terminal](image)

2. **Ingresa la Matriz de ADN:**  
   - La matriz debe estar compuesta por **cadenas de texto de exactamente 6 caracteres**.
   - Solo puede contener los caracteres: `A`, `G`, `T` y `C`.  
   - Si introduces un formato incorrecto, el programa mostrará un mensaje de error.  
   
   **Ejemplo de entrada válida:**  
   ![Ejemplo de Matriz](image)

---

## 🔢 **Opciones del Menú Principal**
Introduce el número correspondiente a la acción que deseas realizar:  
1️⃣ **Detectar mutantes**  
2️⃣ **Mutar el ADN**  
3️⃣ **Sanar el ADN**  
4️⃣ **Salir del programa**  

![Imagen del Menú](image)

---

## 🧪 **Detección de Mutantes**
- Si seleccionas la opción `1`, el programa analizará la cadena de ADN y determinará si contiene un gen mutante.  
  - Si **se detecta un gen mutante**, selecciona la opción `3` para **sanar el ADN**.  
  - Si **no se detecta un gen mutante**, selecciona la opción `2` para **mutar el ADN**.

---

## 🔄 **Mutar el ADN**
Al seleccionar la opción `2`, puedes elegir cómo deseas mutar el ADN:  
1. **Radiación**: Presiona la tecla `1`. Lo que ejecuta es una mutación de tipo horizontal `H` o vertical `V`.  
2. **Virus**: Presiona la tecla `2`. Ejecuta una mutación de tipo diagonal `D` por defecto sobre el ADN.  

![Imagen de Mutación](image)

### **Seleccionar Base Nitrogenada**
Después de elegir la dirección de la mutación, selecciona la base nitrogenada que deseas cambiar:  
- `A` para **Adenina**  
- `G` para **Guanina**  
- `T` para **Timina**  
- `C` para **Citosina**  

Una vez seleccionada, el programa mostrará en pantalla la cadena de ADN **mutada**.  
![Imagen de ADN Mutado](image)

---

## 🩺 **Sanar el ADN**
Selecciona la opción `3` para restaurar la cadena de ADN a su estado original si contiene mutaciones.  
- Esto es especialmente útil si se detectaron mutantes en la cadena.  
![Imagen de Sanación](image)
---

## ✅ **Finalizando el Programa**
Cuando desees salir, presiona el número `4`.  
El programa finalizará y todos los cambios quedarán registrados.

![Imagen Final](image)

---

## 🎯 **Notas Importantes**
- Asegúrate de ingresar una matriz válida para evitar errores.  
- Puedes volver a los pasos anteriores para realizar análisis adicionales antes de salir.  

¡Explora las posibilidades de este programa y transforma tus cadenas de ADN! 🚀

---
### :tea: Integrantes del grupo
- Emiliano Orobello
- Tiago Funes 
- Haquin Sergio
- Lemos Sofía
- Barrios Pablo 