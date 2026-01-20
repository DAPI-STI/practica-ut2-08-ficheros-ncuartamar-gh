"""
EX02 (CSV) · Registrar calificaciones finales

Objetivo:
- Practicar escritura en ficheros en modo "append" (añadir al final).
- Guardar datos en un formato estándar: CSV (separado por comas).

En una app real esto sería el típico "registro" de resultados.
"""

from __future__ import annotations

from pathlib import Path


def write_final_grade(path: str | Path, name: str, average: float) -> None:
    """
    Añade una línea al fichero CSV en `path` con este formato:

    nombre,nota

    Ejemplo:
    Ana,7.5

    Reglas:
    - El fichero se crea si no existe.
    - Si ya existe, se añade una línea al final (NO se sobrescribe).
    - name no puede estar vacío tras strip(). Si lo está, ValueError.
    - average debe estar entre 0 y 10 (incluidos). Si no, ValueError.

    Nota:
    - No hace falta escribir cabecera para este ejercicio.
    """
    raise NotImplementedError("Implementa write_final_grade(path, name, average)")
