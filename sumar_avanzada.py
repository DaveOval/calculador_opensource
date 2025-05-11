def sumar_avanzada():
    cantidad = int(input("¿Cuántos números desea sumar?: "))
    suma = 0
    for i in range(cantidad):
        numero = int(input(f"Ingrese el número {i+1}: "))
        suma += numero
    print("El resultado de la suma es: ", suma)
    print("================================================")

