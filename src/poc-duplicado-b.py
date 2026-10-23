def procesar_cliente(cliente):
    resultado = {}

    resultado["nombre"] = cliente.get("nombre")
    resultado["apellido"] = cliente.get("apellido")
    resultado["correo"] = cliente.get("correo")
    resultado["telefono"] = cliente.get("telefono")
    resultado["direccion"] = cliente.get("direccion")
    resultado["ciudad"] = cliente.get("ciudad")
    resultado["pais"] = cliente.get("pais")
    resultado["saldo"] = cliente.get("saldo")
    resultado["estado"] = cliente.get("estado")
    resultado["tipo"] = cliente.get("tipo")

    if resultado["saldo"] is None:
        resultado["saldo"] = 0

    if resultado["estado"] is None:
        resultado["estado"] = "DESCONOCIDO"

    if resultado["tipo"] is None:
        resultado["tipo"] = "NORMAL"

    if resultado["pais"] is None:
        resultado["pais"] = "EC"

    if resultado["ciudad"] is None:
        resultado["ciudad"] = "QUITO"

    if resultado["telefono"] is None:
        resultado["telefono"] = "NO DISPONIBLE"

    return resultado
