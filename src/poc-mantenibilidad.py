def calcular_nivel_riesgo(
    edad,
    saldo,
    bloqueado,
    intentos,
    pais,
    es_cliente,
    tiene_deuda,
    transacciones,
    alertas,
    vip
):
    resultado = 0

    if es_cliente:
        if edad > 18:
            if saldo > 1000:
                if bloqueado is False:
                    if intentos < 3:
                        if pais == "EC":
                            resultado += 1

                            if tiene_deuda:
                                resultado += 2
                            else:
                                resultado += 3

                            if transacciones > 20:
                                resultado += 4

                                if alertas > 0:
                                    resultado += 5

                                    if vip:
                                        resultado += 10
                                    else:
                                        resultado += 1
                                else:
                                    resultado += 2
                            else:
                                resultado += 1
                        else:
                            resultado += 7
                    else:
                        resultado += 8
                else:
                    resultado += 9
            else:
                resultado += 10
        else:
            resultado += 11
    else:
        resultado += 12

    return resultado


def obtener_tipo_cliente(tipo):
    if tipo == 1:
        return "CLIENTE NORMAL"

    if tipo == 2:
        return "CLIENTE PREMIUM"

    if tipo == 3:
        return "CLIENTE VIP"

    if tipo == 4:
        return "CLIENTE CORPORATIVO"

    if tipo == 5:
        return "CLIENTE EMPRESA"

    if tipo == 6:
        return "CLIENTE TEMPORAL"

    if tipo == 7:
        return "CLIENTE BLOQUEADO"

    return "CLIENTE DESCONOCIDO"


def imprimir_datos(nombre, correo, telefono):
    print("Nombre del cliente: " + nombre)
    print("Correo del cliente: " + correo)
    print("Teléfono del cliente: " + telefono)


def proceso_innecesario(valor):
    resultado = 0
    dato_temporal = "valor que no se utiliza"

    if valor > 0:
        resultado = resultado + valor
    else:
        resultado = resultado + valor

    return resultado
