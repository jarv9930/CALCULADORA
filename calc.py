#calculadora en python 
import math 

def suma(a,b):
    return a + b

def al_cuadrado(a):
    return a ** 2

def resta (a,b):
    return a-b

def calculadora():
    while True:
        print("\n--- Calculadora ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Elevar al cuadrado")
        print("6. Raíz cuadrada")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '7':
            print("Saliendo de la calculadora...")
            break
        
        if opcion in ['1', '2', '3', '4']:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if opcion == '1':
                print("Resultado:", suma(a, b))
            elif opcion == '2':
                print("Resultado:", resta(a, b))
            elif opcion == '3':
                print("Resultado:", multiplicacion(a, b))
            elif opcion == '4':
                print("Resultado:", division(a, b))
                
        elif opcion in ['5', '6']:
            a = float(input("Ingrese el número: "))
            
            if opcion == '5':
                print("Resultado:", al_cuadrado(a))
            elif opcion == '6':
                print("Resultado:", raiz_cuadrada(a))
                
        else:
            print("Opción no válida. Intente de nuevo.")
calculadora()
