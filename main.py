from sumar import sumar
from resta import resta
from multiplicacion import multiplicacion
from dividir import dividir
from sumar_avanzada import sumar_avanzada
print("================================================")
print("Bienvenido a la calculadora OPEN SOURCE")
print("================================================")


while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Suma avanzada")
    print("6. Salir")
    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("Entrando a la suma...")
        sumar()
    elif opcion == 2:
        print("Entrando a la resta...")
        resta()
    elif opcion == 3:
        print("Entrando a la multiplicación...")
        multiplicacion()
    elif opcion == 4:
        print("Entrando a la división...")
        dividir()
    elif opcion == 5:
        print("Suma avanzada...")
        sumar_avanzada()
    elif opcion == 6:
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida")

