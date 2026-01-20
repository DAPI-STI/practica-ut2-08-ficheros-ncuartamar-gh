[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/yITl1O86)
# Práctica 02.07 · Ficheros (texto y CSV)

En esta práctica vas a trabajar con **lectura y escritura de ficheros** en Python con ejercicios
muy parecidos a los que encontrarías en aplicaciones reales:

1) Leer un fichero de **texto** y buscar una palabra  
2) Escribir un **CSV** con calificaciones finales (añadiendo líneas)  
3) Leer un **CSV** de calificaciones y calcular la **media** de una columna  
4) Gestionar un **listín telefónico** guardado en un fichero (alta, consulta y baja)

La corrección se realiza automáticamente con **pytest** (tests).
También tienes `src/__main__.py` para hacer pruebas manuales sin lanzar los tests.

---

## Estructura del proyecto

```text
practica_0207_ficheros/
├─ src/                 # Tu código (EDITA AQUÍ)
│  ├─ __init__.py
│  ├─ __main__.py        # Pruebas manuales (no se evalúa)
│  ├─ ex01_count_word.py
│  ├─ ex02_write_final_grade.py
│  ├─ ex03_csv_average.py
│  └─ ex04_phonebook.py
├─ test/                # Tests (NO TOCAR)
│  └─ test_practica_0207.py
├─ README.md
├─ requirements.txt
└─ .gitignore
```

✅ Regla principal: **solo debes editar `src/`**.  
❌ No modifiques los tests.

---

## Primeros pasos

### 1) (Opcional) Crear entorno virtual

```bash
python -m venv .venv
# Windows (PowerShell/CMD):
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate
```

### 2) Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3) Ejecutar los tests

> Para ejecutar los tests usa siempre:
```bash
python -m pytest -q
```

### 4) Probar sin tests (opcional)

```bash
python -m src
```

---

## Flujo recomendado

1) Ejecuta tests → verás fallos al principio (es normal)  
2) Implementa una función en `src/`  
3) Vuelve a ejecutar tests  
4) Repite hasta pasar todo ✅
