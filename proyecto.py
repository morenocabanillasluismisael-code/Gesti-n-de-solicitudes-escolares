"""Mesa de partes digital - I.E. N. 81770 "Maria Inmaculada Concepcion".

    Ejecutar:  py IE_MARIA_INMACULADA.py
"""
import os
import sys
from datetime import date, datetime

MAX_SOLICITUDES = 200
MAX_INTENTOS = 3

CARPETA = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_TRAMITE = os.path.join(CARPETA, "Tramite.txt")
ARCHIVO_SEGUIMIENTO = os.path.join(CARPETA, "Seguimiento.txt")

# Tramites (posicion 1-6 del catalogo) que puede pedir cada condicion.
# 1 Constancia de estudios, 2 Certificado de estudios, 3 Matricula o traslado,
# 4 Justificacion de inasistencia, 5 Actualizacion de datos, 6 Otros
TRAMITES_ESTUDIANTE = [1, 2, 3, 4, 5, 6]
TRAMITES_EGRESADO = [1, 2, 5, 6]

CAT_ESTADOS = ["Registrado", "En revision", "Observado", "Aprobado",
               "Rechazado"]
