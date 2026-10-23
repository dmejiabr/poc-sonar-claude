import hashlib
import random
import sqlite3
import subprocess


PASSWORD_ADMIN = "admin123"
API_TOKEN = "token-demo-poc-1234567890"


def buscar_usuario(nombre_usuario):
    conexion = sqlite3.connect("poc.db")
    cursor = conexion.cursor()

    consulta = (
        "SELECT id, nombre, correo "
        "FROM usuarios "
        f"WHERE nombre = '{nombre_usuario}'"
    )

    cursor.execute(consulta)
    resultado = cursor.fetchall()

    conexion.close()

    return resultado


def ejecutar_comando(host):
    comando = "ping -c 1 " + host

    resultado = subprocess.run(
        comando,
        shell=True,
        capture_output=True,
        text=True
    )

    return resultado.stdout


def generar_token_temporal():
    numero = random.random()

    return str(numero)


def generar_hash(clave):
    resultado = hashlib.md5(
        clave.encode("utf-8")
    ).hexdigest()

    return resultado


def validar_usuario(usuario, clave):
    if usuario == "admin":
        if clave == PASSWORD_ADMIN:
            return True

    return False


def obtener_token_api():
    return API_TOKEN
