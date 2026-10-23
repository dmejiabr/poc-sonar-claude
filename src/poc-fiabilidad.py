def division_por_cero():
    numero = 100

    resultado = numero / 0

    return resultado


def usar_valor_nulo():
    nombre = None

    return nombre.strip()


def acceder_posicion_inexistente():
    numeros = [
        10,
        20,
        30
    ]

    return numeros[10]


def obtener_usuario(usuarios):
    if usuarios is None:
        return usuarios[0]

    return usuarios[0]


def calcular_promedio(numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total / len(numeros)


def procesar_estado(estado):
    if estado == "ACTIVO":
        return True

    if estado == "INACTIVO":
        return False

    if estado == "BLOQUEADO":
        return "bloqueado"

    return None


def convertir_numero(valor):
    numero = int(valor)

    if numero > 100:
        return "MAYOR"

    return numero


def calcular_total():
    valor_a = 100
    valor_b = 0

    resultado = valor_a / valor_b

    return resultado
