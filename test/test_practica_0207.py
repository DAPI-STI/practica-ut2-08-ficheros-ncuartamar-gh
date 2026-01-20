import pytest
from pathlib import Path

from src.ex01_count_word import count_word_in_file
from src.ex02_write_final_grade import write_final_grade
from src.ex03_csv_average import csv_average
from src.ex04_phonebook import add_contact, get_phone, remove_contact


def test_ex01_count_word(tmp_path: Path):
    p = tmp_path / "a.txt"
    p.write_text("Hola, hola mundo! holA\nsol solución.", encoding="utf-8")
    assert count_word_in_file(p, "hola") == 3
    assert count_word_in_file(p, "mundo") == 1
    # no debe contar subcadenas (sol vs solución)
    assert count_word_in_file(p, "sol") == 1
    with pytest.raises(ValueError):
        count_word_in_file(p, "   ")
    with pytest.raises(FileNotFoundError):
        count_word_in_file(tmp_path / "noexiste.txt", "hola")


def test_ex02_write_final_grade(tmp_path: Path):
    p = tmp_path / "final.csv"
    write_final_grade(p, "Ana", 7.5)
    write_final_grade(p, "Luis", 6.0)
    assert p.read_text(encoding="utf-8").splitlines() == ["Ana,7.5", "Luis,6.0"]

    with pytest.raises(ValueError):
        write_final_grade(p, "   ", 5.0)
    with pytest.raises(ValueError):
        write_final_grade(p, "Ana", -1)
    with pytest.raises(ValueError):
        write_final_grade(p, "Ana", 10.1)


def test_ex03_csv_average(tmp_path: Path):
    p = tmp_path / "grades.csv"
    p.write_text("name,average\nAna,10\nLuis,6\n", encoding="utf-8")
    assert csv_average(p, "average") == 8.0

    with pytest.raises(ValueError):
        csv_average(p, "nope")

    q = tmp_path / "empty.csv"
    q.write_text("name,average\n", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_average(q, "average")


def test_ex04_phonebook(tmp_path: Path):
    pb = tmp_path / "listin.txt"

    # fichero no existe aún
    assert get_phone(pb, "Ana") is None
    assert remove_contact(pb, "Ana") is False

    add_contact(pb, "Ana", "600")
    add_contact(pb, "Luis", "700")
    assert get_phone(pb, "Ana") == "600"

    # update
    add_contact(pb, "Ana", "111")
    assert get_phone(pb, "Ana") == "111"

    # remove
    assert remove_contact(pb, "Luis") is True
    assert remove_contact(pb, "Luis") is False
    assert get_phone(pb, "Luis") is None
