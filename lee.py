"""El Departamento de Turismo de Chile ha solicitado un sistema para procesar y analizar datos
de turistas que ingresan al país. Los datos se almacenan en un diccionario donde cada llave
es un identificador y el valor una lista con los datos del turista. Los datos son: Nombre, País
de origen y fecha de ingreso a Chile. Un ejemplo del diccionario es como el siguiente, pero
considere que podría haber muchos más registros:
turistas = 
{“001”: [“John Doe”, “Estados Unidos”, “12-01-2024”],
 “002”: [“Emily Smith”, “Estados Unidos”, “23-03-2024”],
 “012”: [“Julian Martinez”, “Argentina”, “19-09-2023”],
 “014”: [“Agustin Morales”, “Argentina”, “28-03-2024”],
 “005”: [“Carlos Garcia”, “Mexico”, “10-05-2024”],
 “006”: [“Maria Lopez”, “Mexico”, “08-12-2023”],
 “007”: [“Joao Silva”, “Brasil”, “20-06-2024”],
 “003”: [“Michael Brown”, “Estados Unidos”, “05-07-2023”],
 “004”: [“Jessica Davis”, “Estados Unidos”: “15-11-2024”],
 “008”: [“Ana Santos”, “Brasil”, “03-10-2023”],
 “010”: [“Martin Fernandez”, “Argentina”, “13-02-2023”],
 “011”: [“Sofia Gomez”, “Argentina”, “07-04-2024”],
 }
Se pide un menú que tengas las siguientes funciones:
*** MENU PRINCIPAL ***
1.- Turistas por país.
2.- Turista por mes.
3.- Eliminar turista.
4.- Salir
Cada opción del menú principal debe estar programada en una función externa al código principal (main)."""


turistas = [
{'numero_de_identificacion' : '001', 'nombre':'John Doe',         'pais':'Estados Unidos', 'fecha_de_ingreso':'12-01-2024'},
{'numero_de_identificacion' : '002', 'nombre':'Emily Smith',      'pais':'Estados Unidos', 'fecha_de_ingreso':'23-03-2024'},
{'numero_de_identificacion' : '012', 'nombre':'Julian Martinez',  'pais':'Argentina',      'fecha_de_ingreso':'19-09-2023'},
{'numero_de_identificacion' : '014', 'nombre':'Agustin Morales',  'pais':'Argentina',      'fecha_de_ingreso':'28-03-2024'},
{'numero_de_identificacion' : '005', 'nombre':'Carlos Garcia',    'pais':'Mexico',         'fecha_de_ingreso':'10-05-2024'},
{'numero_de_identificacion' : '006', 'nombre':'Maria Lopez',      'pais':'Mexico',         'fecha_de_ingreso':'08-12-2023'},
{'numero_de_identificacion' : '007', 'nombre':'Joao Silva',       'pais':'Brasil',         'fecha_de_ingreso':'20-06-2024'},
{'numero_de_identificacion' : '003', 'nombre':'Michael Brown',    'pais':'Estados Unidos', 'fecha_de_ingreso':'05-07-2023'},
{'numero_de_identificacion' : '004', 'nombre':'Jessica Davis',    'pais':'Estados Unidos', 'fecha_de_ingreso':'15-11-2024'},
{'numero_de_identificacion' : '008', 'nombre':'Ana Santos',       'pais':'Brasil',         'fecha_de_ingreso':'03-10-2023'},
{'numero_de_identificacion' : '010', "nombre":'Martin Fernandez', 'pais':'Argentina',      'fecha_de_ingreso':'13-02-2023'},
{'numero_de_identificacion' : '011', "nombre":'Sofia Gomez',      'pais':'Argentina',      'fecha_de_ingreso':'07-04-2024'}
]

def menu():
    
    while True:

        print("""\n
          
        ***MENU PRINCIPAL*** 
          
        1.- Turistas por país.
        2.- Turista por mes.
        3.- Eliminar turista.
        4.- Salir
          
        """)
        return input("Ingrese su seleccion: ")
    
def turista_por_pais(turistas):
    while True:
        print("Buscar turistas por país")
        print("[ Estados Unidos | Argentina | Brasil | Mexico ]")
        pais_buscado = input("Ingrese un país o escriba 'salir' para terminar: ")

        if pais_buscado.lower() == "salir":
            break

        encontrado = False

        for turista in turistas:
            if turista["pais"].lower() == pais_buscado.lower():
                print(f"{turista['nombre']} (ID: {turista['numero_de_identificacion']}) - Fecha de ingreso: {turista['fecha_de_ingreso']}")
                encontrado = True

        if not encontrado:
            print("No se encontraron turistas para ese país.\n")

def turistas_por_mes(turistas, mes):
    total = len(turistas)
    if total == 0:
        return 0.0

    cantidad_en_mes = sum(
        1 for turista in turistas if int(turista['fecha_de_ingreso'].split('-')[1]) == mes
    )

    porcentaje = (cantidad_en_mes / total) * 100
    return round(porcentaje, 1)

def turista_por_mes(turistas):
    while True:
        print("\nBuscar turista por mes")
        print("Enero (1), Febrero(2), Marzo(3), Abril(4), Mayo(5), Junio(6)")
        print("Julio (7), Agosto (8), Septiembre (9), Octubre (10), Noviembre (11), Diciembre (12)")
        mesSeleccionado = input("Ingrese el número del mes o escriba 'salir': ")

        if mesSeleccionado.lower() == "salir":
            break

        if not mesSeleccionado.isdigit():
            print("Por favor ingrese un número válido.")
            continue

        mesSeleccionado = int(mesSeleccionado)

        if mesSeleccionado < 1 or mesSeleccionado > 12:
            print("Ingrese un número de mes entre 1 y 12.")
            continue

        porcentaje = turistas_por_mes(turistas, mesSeleccionado)
        print(f"El porcentaje de turistas que ingresaron durante el mes {mesSeleccionado} es: {porcentaje}%")

        


def eliminar_turista(turistas):
    print("\nLista de turistas registrados:")
    for turista in turistas:
        print(f"ID: {turista['numero_de_identificacion']} - Nombre: {turista['nombre']}")

    id_buscado = input("\nIngrese el ID del turista que desea eliminar (o escriba 'salir' para cancelar): ")

    if id_buscado.lower() == "salir":
        print("Eliminación cancelada.")
        return

    encontrado = False
    for turista in turistas:
        if turista["numero_de_identificacion"] == id_buscado:
            turistas.remove(turista)
            print(f"Turista {turista['nombre']} (ID: {turista['numero_de_identificacion']}) eliminado correctamente.")
            encontrado = True
            break

    if not encontrado:
        print("❌ No se encontró un turista con ese ID.")