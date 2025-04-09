import random

# Definimos las ciudades y días de la semana
ciudades = ["Ciudad Arajuno", "Ciudad Puyo", "Ciudad Macas "]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Creamos una matriz 3D para almacenar las temperaturas
# Dimensiones: [ciudades][días de la semana][semanas]
temperaturas = [[[random.randint(15, 30) for _ in range(len(dias_semana))] for _ in range(semanas)] for _ in range(len(ciudades))]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_semana)):
            suma_temperaturas += temperaturas[i][semana][dia]
        promedio = suma_temperaturas / len(dias_semana)
        print(f"Promedio de temperaturas en {ciudad} para la Semana {semana + 1}: {promedio:.2f}°C")