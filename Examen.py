# Roberto_Medina_ET
planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,
'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}

inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],
}

def leer_opcion():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=====================================")

        try:
            opcion = int(input("Escoga una opcion del 1 - 6: "))
            if opcion <= 0 or opcion > 6:
                print("Debe seleccionar una opcion valida")
            else:
                return opcion
        except ValueError:
            print("Debe seleccionar una opcion valida")

def cupos_tipo(tipo, dicc_plan, dicc_inscripcion):
    total = 0
    tipo = tipo.lower().strip()

    for num in dicc_plan:
        datos_plan = dicc_plan[num]
        tipo_plan = datos_plan[1].lower()
        if tipo_plan == tipo:
            datos_inscripcion = dicc_inscripcion[num]
            cupos = datos_inscripcion[1]
            total += cupos
    print(f"El total de cupos disponibles es: {cupos}")


def busqueda_precio(p_min, p_max, dicc_plan, dicc_inscripcion):
    resultados = []

    for num in dicc_inscripcion:
        datos_inscripcion = dicc_inscripcion[num]
        precio = datos_inscripcion[0]
        cupos = datos_inscripcion[1]

        if precio >= p_min and precio <= p_max and cupos > 0:
            datos_plan = dicc_plan[num]
            nombre = datos_plan[0]
            resultados.append(f"{nombre}--{num}")
   
def buscar_codigo(codigo, dicc_inscripcion):
    for num in dicc_inscripcion:
        if num.lower() == codigo.lower():
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, dicc_inscripcion):
    if buscar_codigo(codigo, dicc_inscripcion):
        for num in dicc_inscripcion:
            if num.lower() == codigo.lower():
                return True
        return False
    
def validar_codigo(codigo, dicc_plan):
    if codigo.strip() == "":
        return False
    for num in dicc_plan:
        if num.lower() == codigo.lower():
            return False
    return True

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_tipo(tipo):
    return tipo in ['mensual', 'trimestral', 'anual']

def validar_duracion(duracion):
    return duracion > 0

def validar_respuesta(respuesta):
    return respuesta in ['s', 'n']

def validar_horario(horario):
    return horario.strip() != ""

def validar_precio(precio):
    return precio > 0

def validar_cupos(cupos):
    return cupos >= 0

def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, dicc_plan, dicc_inscripcion):
    num_upper = codigo.upper()
    piscina_bool = (acceso_piscina == 's')
    clases_bool = (incluye_clases == 's')

    dicc_plan[num_upper] = [nombre, tipo, duracion, piscina_bool, clases_bool, horario]
    dicc_inscripcion[num_upper] = [precio, cupos]
    return True

def eliminar_plan(codigo, dicc_plan, dicc_inscripcion):
    if buscar_codigo(codigo, dicc_plan):
        for num in list(dicc_plan.keys()):
            if num.lower() == codigo.lower():
                del dicc_plan[num]
                del dicc_inscripcion[num]
                return True
    return False


while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por tipo de plan")
        print("2. Búsqueda de planes por rango de precio")
        print("3. Actualizar precio de plan")
        print("4. Agregar plan")
        print("5. Eliminar plan")
        print("6. Salir")
        print("=====================================")
        
        opcion_elegida = leer_opcion()
        
        if opcion_elegida == 1:
            tipo_buscado = input("Ingrese tipo de plan a consultar: ")
            cupos_tipo(tipo_buscado, planes, inscripciones)
        
        elif opcion_elegida == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    p_max = int(input("Ingrese precio maximo: "))

                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max, planes, inscripciones)
                        break
                    else:
                        print("El precio minimo debe ser menor o igual a al maximo")
                except ValueError:
                    print("Debe ingresar valores enteros.")
        
        elif opcion_elegida == 3:
            while True:
                num = input("Ingrese codigo del plan: ")
                try:
                    nuevo_p = int(input("Ingrese nuevo precio: "))
                    if nuevo_p <= 0:
                        print("Debe ser un precio mayor a 0")
                        continue
                except ValueError:
                    print("Debe ingresar un numero entero")
                    continue
                if actualizar_precio(num, nuevo_p, inscripciones):
                    print("precio actualizado.")
                else:
                    print("El codigo no existe.")
                
                resp = input("¿Desea actualizar este precio? (s/n): ").lower()
                if resp == 'n':
                    break
                    
        elif opcion_elegida == 4:
            print("nop")

        elif opcion_elegida == 5:
            print("nope")

        elif opcion_elegida == 6:
            print("Programa finalizado.")
            break
