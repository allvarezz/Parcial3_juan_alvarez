from funciones import Grabar, Buscar, Imprimir
import os
import time

os.system("cls")

sw = True
while sw:
    os.system("cls")  # Esta línea limpia la consola

    print("***    La automotora 'Auto Seguro'    ***")
    print("1. Grabar [1]")
    print("2. Buscar [2]")
    print("3. Imprimir certificados [3]")
    print("4. Salir")

    try:
        op = int(input("Ingrese opción: "))

        if op == 1:
            Grabar()
        elif op == 2:
            Buscar()
        elif op == 3:
            Imprimir()
        elif op == 4:
            sw = False
        else:
            print("Opción no válida")

        time.sleep(2)  

    except ValueError:
        print("Tipo de dato no permitido")
        time.sleep(2)

        
        
        
####
### git add .
# git config user.name "felipe t"
# git config user.email "david1ride@outlook.cl"
# git commit -m "agrego archivo funciones y main"
# git push -u origin main