"""
Midterm — Fundamentos técnicos de programación

Instrucciones:
1. Ejecuta git fetch origin para actualizar las referencias del remoto.
2. Crea tu rama midterm-nombre a partir de origin/midterm.
3. Copia este archivo con el nombre midterm_<tu_nombre>.py.
4. Completa las variables respuesta_01 a respuesta_15.
   - Para preguntas de una sola opción, utiliza una letra: "A", "B", "C" o "D".
   - Para la pregunta 07 (selección múltiple), utiliza una lista de letras:
     por ejemplo, ["A", "C"].
5. Ejecuta desde la raíz del proyecto:
   uv run python midterm/midterm_<tu_nombre>.py
6. Comprueba que se impriman tus respuestas, haz commit, push y abre un
   Pull Request hacia midterm. No hagas merge del Pull Request.

Puedes consultar tus notas y documentación.
No modifiques las preguntas ni la sección que imprime las respuestas.
"""

nombre = "Dulce Alicia Torres Hernández"

# ============================================================
# I. PYTHON Y ESTRUCTURA DE PROYECTOS
# ============================================================

# PREGUNTA 01. Imports y estructura de paquetes
# En un notebook encuentras:
#
#     from progra.preprocessing.cleaning import remove_strs
#
# Suponiendo que progra es un paquete local y que remove_strs está definida
# directamente en el módulo importado, ¿en qué archivo buscarías la función?
#
# A) progra/cleaning.py
# B) progra/preprocessing/__init__.py
# C) progra/preprocessing/remove_strs.py
# D) progra/preprocessing/cleaning.py
respuesta_01 = "D"


# PREGUNTA 02. Organización de paquetes Python
# Observa la estructura:
#
# proyecto/
# ├── pyproject.toml
# └── src/
#     └── progra/
#         ├── __init__.py
#         └── preprocessing/
#             ├── __init__.py
#             ├── cleaning.py
#             └── validation.py
#
# ¿Cuál afirmación es correcta?
#
# A) preprocessing es un subpaquete de progra; cleaning.py es un módulo suyo.
# B) preprocessing es un módulo de progra; cleaning.py es un subpaquete.
# C) cleaning.py y validation.py son subpaquetes independientes de progra.
# D) __init__.py debe contener todas las funciones de preprocessing.
respuesta_02 = "A"


# PREGUNTA 03. Dependencias y ambientes virtuales
# Clonas un repositorio que contiene pyproject.toml, uv.lock, src/ y notebooks/,
# pero no contiene la carpeta .venv/. ¿Cómo preparas el ambiente?
#
# A) Ejecutar uv venv; esto también instala todas las dependencias del proyecto.
# B) Ejecutar uv add sin argumentos para instalar dependencias registradas.
# C) Ejecutar uv sync desde la raíz del proyecto.
# D) Ejecutar uv python install para instalar dependencias de pyproject.toml.
respuesta_03 = "C"


# PREGUNTA 04. Diagnóstico de ambientes Python
# En VS Code, un notebook produce:
#
#     ModuleNotFoundError: No module named 'pandas'
#
# Sin embargo, desde la terminal en la raíz del proyecto se ejecuta:
#
#     uv run python -c "import pandas; print(pandas.__version__)"
#
# y se obtiene un número de versión. ¿Cuál es una explicación probable?
#
# A) pandas no se agregó a Git mediante git add.
# B) El notebook usa otro kernel/intérprete, distinto al ambiente de uv run.
# C) Es necesario ejecutar uv add pandas al iniciar cada sesión del notebook.
# D) El notebook debe estar dentro de la carpeta donde se instaló pandas.
respuesta_04 = "C"


# PREGUNTA 05. Importación de paquetes locales
# Tienes la siguiente estructura:
#
# proyecto/
# ├── pyproject.toml
# ├── src/
# │   └── progra/
# │       ├── __init__.py
# │       └── cleaning.py
# └── notebooks/
#     └── exploracion.ipynb
#
# En el notebook ejecutas "from progra import cleaning" y recibes:
#
#     ModuleNotFoundError: No module named 'progra'
#
# ¿Qué revisarías primero?
#
# A) Si cleaning.py fue ejecutado antes desde la terminal.
# B) Si __init__.py contiene todas las funciones de cleaning.py.
# C) Si progra está disponible en las paqueterías de PyPi e instalarlo correctamente. 
# D) Si el proyecto está correctamente configurado e instalado en el ambiente virtual utilizado por el notebook.
respuesta_05 = "D"


# ============================================================
# II. CLI, ARCHIVOS Y RUTAS
# ============================================================

# PREGUNTA 06. Archivos ocultos y Git
# Un proyecto contiene .gitignore, .secrets, .venv/, README.md y src/.
# Ejecutas ls -a y observas todos esos elementos. Luego, en git status,
# .secrets aparece como archivo sin seguimiento (untracked).
# ¿Qué puedes concluir?
#
# A) .secrets está protegido por ser un archivo oculto, aunque aparezca en git status.
# B) .secrets está automáticamente en staging porque aparece en git status.
# C) .secrets no está versionado, pero Git lo detecta y podría agregarse si no hay una regla que lo ignore.
# D) .secrets ya está publicado en GitHub y hace falta un git pull.
respuesta_06 = "B"


# PREGUNTA 07. Archivos que no deben incorporarse al repositorio
# Vas a publicar un repositorio en GitHub. Selecciona TODOS los archivos o
# directorios que no deberían incorporarse al repositorio y que, cuando
# corresponda, debes asegurarte de excluir mediante .gitignore.
#
# A) .secrets con credenciales de una base de datos
# B) README.md
# C) .venv/
# D) pyproject.toml
# E) src/cleaning.py
# F) ~/.ssh/id_ed25519 (llave SSH privada)
# G) .gitignore
# H) data/datos.csv con información personal confidencial
#
# Escribe una lista de letras, por ejemplo: ["A", "C"].
# Ten presente que una llave en ~/.ssh/ suele estar fuera del repositorio;
# no necesita figurar literalmente en el .gitignore del proyecto.
respuesta_07 = ["A", "C", "F", "H"]


# PREGUNTA 08. Rutas relativas al ejecutar Python
# Estructura:
#
# proyecto/
# ├── data/
# │   └── datos.csv
# ├── src/
# │   └── analisis.py
# └── pyproject.toml
#
# En analisis.py: archivo = open("data/datos.csv")
# Desde proyecto/ ejecutas: uv run python src/analisis.py
# Suponiendo que existe el CSV y tienes permiso de lectura, ¿qué sucede?
#
# A) Busca proyecto/data/datos.csv porque la ruta parte del directorio actual.
# B) Busca proyecto/src/data/datos.csv porque la ruta parte del script.
# C) Busca proyecto/src/data/datos.csv porque uv cambia a src/.
# D) Busca proyecto/data/datos.csv, pero marca error porque no estás corriendo el comando desde src/.
respuesta_08 = "B"


# PREGUNTA 09. Interpretación de pipelines de Bash
# Ejecutas:
#
# tail -n +2 data/datos.csv | cut -d',' -f3 | sort | uniq -c | sort -nr | head -5
#
# Suponiendo un CSV simple (sin comas dentro de campos entrecomillados),
# ¿qué información busca obtener?
#
# A) Los cinco valores numéricamente más grandes de la tercera columna.
# B) Las primeras cinco observaciones de la tercera columna, en orden descendente.
# C) Los cinco primeros valores distintos de la tercera columna, por alfabeto.
# D) Los cinco valores más frecuentes de la tercera columna, sin encabezado.
respuesta_09 = "B"


# PREGUNTA 10. Rutas relativas desde CLI
# Estructura:
#
# proyecto/
# ├── data/
# │   └── muestra.csv
# ├── notebooks/
# │   └── exploracion.ipynb
# └── src/
#     └── limpieza.py
#
# Estás en proyecto/notebooks/. ¿Cómo muestras las primeras diez líneas de
# muestra.csv sin cambiar de directorio?
#
# A) head -n 10 data/muestra.csv
# B) head -n 10 ./data/muestra.csv
# C) head -n 10 ../data/muestra.csv
# D) head -n 10 ../../data/muestra.csv
respuesta_10 = "C"


# PREGUNTA 11. Redirección de salida
# Ejecutas:
#
#     grep "CDMX" data/datos.csv > resultados.txt
#
# ¿Qué sucede?
#
# A) Muestra las líneas con CDMX; resultados.txt no se modifica.
# B) Guarda las líneas con CDMX, creando o sobrescribiendo resultados.txt.
# C) Agrega las líneas con CDMX al final de resultados.txt.
# D) Guarda únicamente el número de líneas con CDMX en resultados.txt.
respuesta_11 = "B"


# ============================================================
# III. GIT Y GITHUB
# ============================================================

# PREGUNTA 12. Ramas divergentes
# Ejecutas git pull origin main y Git muestra:
#
# hint: You have divergent branches and need to specify
# hint: how to reconcile them.
# hint:   git config pull.rebase false
# hint:   git config pull.rebase true
# hint:   git config pull.ff only
# fatal: Need to specify how to reconcile divergent branches.
#
# ¿Qué significa?
#
# A) Existen commits distintos en local y remoto, y debes especificar cómo integrar ambas historias.
# B) Solo el remoto tiene commits nuevos, y debes hacer git pull.
# C) Hay cambios sin guardar que deben agregarse a staging para descargar.
# D) Las ramas local y remota tienen nombres distintos y falta configurarlos.
respuesta_12 = "A"


# PREGUNTA 13. .gitignore y archivos ya versionados
# Agregaste estas reglas a .gitignore:
#
#     .secrets
#     *.csv
#     .venv/
#
# Pero Git sigue mostrando cambios después de modificar data/ventas.csv.
# ¿Cuál es la explicación más probable?
#
# A) Hay que ejecutar git add .gitignore para activar la regla localmente.
# B) Las reglas se activan después de hacer push al remoto.
# C) *.csv solo aplica a CSV en la raíz del repositorio.
# D) ventas.csv ya estaba registrado por Git antes de agregar esa regla.
respuesta_13 = "D"


# PREGUNTA 14. Interpretación de git status
# Ejecutas git status:
#
#   On branch analisis-ana
#
#   Changes to be committed:
#       modified: src/cleaning.py
#
#   Changes not staged for commit:
#       modified: README.md
#
#   Untracked files:
#       docs/notas.md
#
# Luego ejecutas: git commit -m "Actualiza limpieza"
# ¿Qué cambios se incluyen?
#
# A) cleaning.py, porque es el único archivo en staging.
# B) cleaning.py y README.md, porque faltan por rastrear.
# C) cleaning.py y notas.md, porque uno está preparado y el otro es nuevo.
# D) Los tres archivos, porque commit registra todo el directorio de trabajo.
respuesta_14 = "A"


# PREGUNTA 15. Rechazo de git push
# Después de un commit ejecutas git push y aparece:
#
#   To github.com:LDataLab/fiscus.git
#       ! [rejected] main -> main (fetch first)
#   error: failed to push some refs
#   hint: Updates were rejected because the remote
#   hint: contains work that you do not have locally.
#   hint: If you want to integrate the remote changes,
#   hint: use 'git pull' before pushing again.
#
# ¿Por qué fue rechazado y qué deberías hacer?
#
# A) Hay cambios locales sin registrar; ejecutar git add y git commit.
# B) Hay archivos diferentes; usar git push --force para reemplazar el remoto.
# C) El remoto tiene commits no integrados localmente y tienes que incorporarlos antes de publicar tus commits.
# D) Basta git fetch origin y repetir push para integrar los commits que no tiene el remoto.
respuesta_15 = "D"


# ============================================================
# SALIDA DEL EXAMEN — NO MODIFICAR
# ============================================================

respuestas = [
    respuesta_01, respuesta_02, respuesta_03, respuesta_04, respuesta_05,
    respuesta_06, respuesta_07, respuesta_08, respuesta_09, respuesta_10,
    respuesta_11, respuesta_12, respuesta_13, respuesta_14, respuesta_15,
]

print(f"\nMIDTERM — {nombre}")
print("=" * 42)
for numero, respuesta in enumerate(respuestas, start=1):
    if isinstance(respuesta, list):
        texto = ", ".join(respuesta) if respuesta else "SIN RESPUESTA"
    else:
        texto = str(respuesta).strip() or "SIN RESPUESTA"
    print(f"Pregunta {numero:02d}: {texto}")
print("=" * 42)

