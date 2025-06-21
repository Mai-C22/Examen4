import lee as fun


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

while True:

        opc = int(fun.menu())

        if opc == 1:
            fun.turista_por_pais(turistas)
        elif opc == 2:
            fun.turista_por_mes(turistas)
        elif opc == 3:
            fun.eliminar_turista(turistas)
        elif opc == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
