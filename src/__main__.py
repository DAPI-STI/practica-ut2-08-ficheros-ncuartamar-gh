"""
Archivo principal del proyecto.

Desde aquí puedes probar las funciones SIN usar pytest.
Este archivo NO se evalúa automáticamente.
"""

from pathlib import Path

from .ex01_count_word import count_word_in_file
from .ex02_write_final_grade import write_final_grade
from .ex03_csv_average import csv_average
from .ex04_phonebook import add_contact, get_phone, remove_contact


def main() -> None:
    print("=== Pruebas manuales ===")

    # EX01
    text_path = Path("demo.txt")
    text_path.write_text("Hola mundo. Hola Navarra! hola\nAdiós.", encoding="utf-8")
    print("EX01 count 'hola' ->", count_word_in_file(text_path, "hola"))
    text_path.unlink(missing_ok=True)

    # EX02 + EX03 (CSV)
    grades_path = Path("final_grades.csv")
    write_final_grade(grades_path, "Ana", 7.5)
    write_final_grade(grades_path, "Luis", 6.0)
    print("EX02 contenido CSV ->")
    print(grades_path.read_text(encoding="utf-8"))
    # Nota: aquí la cabecera es name,average (porque la usa EX03)
    # Puedes crear tu propio CSV con esa cabecera para probar EX03 manualmente.
    tmp_csv = Path("grades.csv")
    tmp_csv.write_text("name,average\nAna,10\nLuis,6\n", encoding="utf-8")
    print("EX03 media ->", csv_average(tmp_csv, "average"))
    grades_path.unlink(missing_ok=True)
    tmp_csv.unlink(missing_ok=True)

    # EX04 (listín)
    pb = Path("listin.txt")
    add_contact(pb, "Ana", "600123123")
    add_contact(pb, "Luis", "600000000")
    print("EX04 get_phone(Ana) ->", get_phone(pb, "Ana"))
    print("EX04 remove_contact(Luis) ->", remove_contact(pb, "Luis"))
    print("EX04 get_phone(Luis) ->", get_phone(pb, "Luis"))
    pb.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
