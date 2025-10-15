import os
from time import sleep

# EJERCICIO FINAL MODULO 1 - CRUD EMPRESAS
# NOMBRE: BRANDON CONTRERAS

dic_empresas = {
    '20454545': {
        'nombre_empresa': 'EMPRESA SAC',
        'dir_empresa': 'CALLE EL SOL 123',
    }
}

ANCHO = 50

while True:
    os.system("cls")  
    print("=" * ANCHO)
    print(" " * 10 + "GESTIÓN DE EMPRESAS")
    print("=" * ANCHO)
    print("""
         [1] REGISTRAR EMPRESA
         [2] MOSTRAR EMPRESAS
         [3] ACTUALIZAR EMPRESA
         [4] ELIMINAR EMPRESA
         [5] SALIR
          """)
    print("=" * ANCHO)

    opcion = int(input("INGRESE OPCIÓN: "))
    os.system("cls")

    if opcion == 1:
        print("=" * ANCHO)
        print(" " * 10 + "REGISTRAR EMPRESA")
        print("=" * ANCHO)
        ruc = input("Ingrese el RUC de la Empresa: ")
        nombre_empresa = input("Ingrese el nombre de la Empresa: ")
        dir_empresa = input("Ingrese la dirección de la Empresa: ")

        nueva_empresa = {
            "nombre_empresa": nombre_empresa,
            "dir_empresa": dir_empresa
        }

        dic_empresas[ruc] = nueva_empresa
        print("\n Empresa registrada correctamente.")

 

    if opcion == 2:
        print("=" * ANCHO)
        print(" " * 10 + "MOSTRAR EMPRESAS")
        print("=" * ANCHO)

        for ruc, info in dic_empresas.items():
            print(f"RUC: {ruc}")
            print(f"Empresa: {info['nombre_empresa']}")
            print(f"Dirección: {info['dir_empresa']}")
            print("*" * ANCHO)

    if opcion == 3:
        print("=" * ANCHO)
        print(" " * 10 + "ACTUALIZAR EMPRESA")
        print("=" * ANCHO)
        ruc=input("Ingrese la empresa a Actualizar: ")
        if ruc in dic_empresas:
            print(f"Empresa encontrada {dic_empresas[ruc]['nombre_empresa']}")
            nuevo_nombre=input("Ingrese el nuevo nombre(dejar en blanco si no desea actualziar): ")
            nueva_direccion=input("Ingrese la nueva direccion(dejar en blanco si no desea actualziar): ")
            if nuevo_nombre:
                dic_empresas[ruc]['nombre_empresa']=nuevo_nombre
            if nueva_direccion:    
                dic_empresas[ruc]['dir_empresa']=nueva_direccion
            print("Empresa actualizada correctamente    ")    
        else:
            print("No se encontro empresa") 

    if opcion == 4:
        print("=" * ANCHO)
        print(" " * 10 + "ELIMINAR EMPRESA")
        print("=" * ANCHO)
        ruc=input("Ingrese la empresa a eliminar: ")
        if ruc in dic_empresas:
            del dic_empresas[ruc]
        else:
            print("No se encontro empresa")

    if opcion == 5:
        print("=" * ANCHO)
        print(" " * 10 + "SALIENDO DEL SISTEMA...")
        print("=" * ANCHO)
        sleep(2)
        break
    
    input("Presione ENTER para continuar...")