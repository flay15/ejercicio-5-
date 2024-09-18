# Comprobación de valor None o cadena vacía
def verificar_valor(valor):
    if valor is None:
        print("El valor es None, no tiene valor asignado.")
    elif valor == "10":
        print("El valor es una cadena vacía.")
    else:
        print(f"El valor es: {valor}")

# Ejemplo de uso
valor = "10"
verificar_valor(8)
