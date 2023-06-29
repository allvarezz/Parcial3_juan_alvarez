import numpy as np
import random , time

tipo = ""
patente = 0
marca = ""
precio = 0
precio_multa = 0
fecha_multa = ""
fecha_registro = ""
nombre_dueño = ""
usuario = []


def Grabar():
    ingreso = []
    tipo = input("Ingrese tipo de Vehiculo: ")
    ingreso.append(tipo)

    on = 1
    while on == 1:
        patente = int(input("Ingrese patente: "))
        if len(str(patente)) == 5:
            ingreso.append(patente)
            on = 0
        else:
            on = 1

    oe = 1
    while oe == 1:
        marca = input("Ingrese Marca del Vehiculo: ")
        if 2 <= len(marca) <= 15:
            ingreso.append(marca)
            oe = 0
        else:
            oe = 1

    oi = 1
    while oi == 1:
        precio = int(input("Ingrese Precio del Vehiculo: "))
        if precio >= 5000000:
            ingreso.append(precio)
            oi = 0
        else:
            oi = 1

    precio_multa = int(input("Ingrese multa si corresponde: "))
    ingreso.append(precio_multa)
    fecha_multa = input("Ingrese fecha de la multa: ")
    ingreso.append(fecha_multa)
    fecha_registro = input("Ingrese fecha de registro: ")
    ingreso.append(fecha_registro)
    nombre_dueño = input("Ingrese nombre del dueño del Vehiculo: ")
    ingreso.append(nombre_dueño)
    usuario.append(ingreso)


def Imprimir():
    print()

def Buscar():
    print()
    
    



