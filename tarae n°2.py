def obtener_indice_momento_dia(momento):
    momentos_del_dia = {"mañana": 0, "tarde": 1, "noche": 2}
    return momentos_del_dia.get(momento.lower(), -1)

def evaluar_temperatura(momento, temperatura):
    # Definición de los valores predeterminados de temperatura para cada momento del día y nivel
    valores_predeterminados = {
        "mañana": {"muy buena": 15, "normal": 25, "peligrosa": 35},
        "tarde": {"muy buena": 20, "normal": 30, "peligrosa": 40},
        "noche": {"muy buena": 10, "normal": 20, "peligrosa": 30}
    }

    # Obtener el índice del momento del día ingresado por el usuario
    indice_momento = obtener_indice_momento_dia(momento)
    
    if indice_momento == -1:
        return "Error: Momento del día no válido."
    
    # Obtener los valores predeterminados de temperatura para el momento del día especificado
    valores = valores_predeterminados[momento]

    # Evaluar la temperatura registrada en relación con los valores predeterminados
    if temperatura < valores["muy buena"]:
        return "Muy Buena"
    elif temperatura < valores["peligrosa"]:
        return "Normal"
    else:
        return "Peligrosa"

def main():
    # Solicitud de datos al usuario
    momento = input("Por favor, ingrese el momento del día (mañana, tarde, noche): ")
    temperatura = float(input("Ingrese la temperatura actual del tanque de combustible: "))
    
    # Evaluación de la temperatura
    resultado_evaluacion = evaluar_temperatura(momento, temperatura)
    
    # Resultado de la evaluación
    print("La temperatura del tanque de combustible en la", momento, "es:", resultado_evaluacion)

if __name__ == "__main__":
    main()
