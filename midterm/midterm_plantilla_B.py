"""Midterm — Fundamentos técnicos de programación | Versión B

Evaluación individual. Puedes consultar notas y documentación, pero no utilizar IA.

1. Crea una rama individual desde la rama de examen indicada por la profesora.
2. Copia esta plantilla como midterm_<tu_nombre>.py; no modifiques la original.
3. Escribe una letra ("A", "B", "C" o "D") en respuesta_01 a respuesta_15.
   EXCEPCIÓN: respuesta_07 es una lista de letras, por ejemplo ["A", "C"].
4. Ejecuta desde la raíz del repositorio:
   uv run python midterm/midterm_<tu_nombre>.py
5. Realiza commit, push y Pull Request hacia la rama de examen indicada.
   No hagas merge. No cambies los enunciados ni la sección de impresión.
"""

nombre = "ESCRIBE TU NOMBRE"

# ============================================================
# I. PYTHON, PAQUETES Y AMBIENTES
# ============================================================

# PREGUNTA 01. Rastrear un import
# En un notebook aparece:
#
#     from progra.transformaciones.texto import normalizar
#
# Supón que normalizar está definida directamente en el módulo importado
# y que progra corresponde a un paquete local. ¿Dónde la buscarías primero?
#
# A) progra/transformaciones/normalizar.py
# B) progra/texto/transformaciones.py
# C) progra/transformaciones/texto.py
# D) progra/transformaciones/__init__.py
respuesta_01 = ""


# PREGUNTA 02. Paquetes y módulos
# Observa:
#
# proyecto/
# └── src/
#     └── progra/
#         ├── __init__.py
#         └── features/
#             ├── __init__.py
#             ├── texto.py
#             └── fechas.py
#
# ¿Qué afirmación describe correctamente esta estructura?
#
# A) features es un archivo Python y texto.py es un paquete.
# B) texto y fechas solo pueden importarse si sus funciones están copiadas
#    dentro de progra/__init__.py.
# C) Cada archivo .py dentro de features es un subpaquete independiente.
# D) features es un subpaquete de progra, y texto.py y fechas.py son módulos.
respuesta_02 = ""


# PREGUNTA 03. Reproducir un ambiente
# Una persona clona un proyecto que tiene pyproject.toml y uv.lock,
# pero no incluye .venv/. Quiere reproducir sus dependencias.
# ¿Cuál es el comando más apropiado desde la raíz del proyecto?
#
# A) uv sync
# B) uv venv, porque además de crear el ambiente instala todas las
#    dependencias declaradas en pyproject.toml.
# C) uv python install, porque sincroniza las dependencias del proyecto.
# D) uv add, sin argumentos, porque vuelve a instalar lo ya registrado.
respuesta_03 = ""


# PREGUNTA 04. Notebook y ambiente
# Desde la raíz del proyecto, la terminal muestra:
#
#     $ uv run python -c "import numpy; print(numpy.__version__)"
#     2.2.0
#
# Pero en VS Code el notebook devuelve:
#
#     ModuleNotFoundError: No module named 'numpy'
#
# ¿Cuál sería la primera comprobación más pertinente?
#
# A) Revisar si numpy fue agregado al staging area con git add.
# B) Comprobar si el notebook está ubicado en src/ en vez de notebooks/.
# C) Revisar qué kernel/intérprete utiliza el notebook y si corresponde
#    al ambiente del proyecto usado por uv run.
# D) Volver a ejecutar git pull, porque el error indica que faltan commits.
respuesta_04 = ""


# PREGUNTA 05. Paquete local no encontrado
# Estructura de un proyecto:
#
# proyecto/
# ├── pyproject.toml
# ├── src/
# │   └── progra/
# │       ├── __init__.py
# │       └── validacion.py
# └── notebooks/
#     └── revision.ipynb
#
# En el notebook, "import progra.validacion" produce:
#     ModuleNotFoundError: No module named 'progra'
#
# El archivo src/progra/validacion.py sí existe. ¿Qué revisarías primero?
#
# A) Si validacion.py se ejecutó al menos una vez como script.
# B) Si el proyecto está configurado/instalado de modo que el intérprete
#    del notebook pueda encontrar el paquete progra.
# C) Si __init__.py contiene una copia del código de validacion.py.
# D) Si el archivo .ipynb tiene el mismo nombre que el paquete.
respuesta_05 = ""


# ============================================================
# II. CLI Y SISTEMA DE ARCHIVOS
# ============================================================

# PREGUNTA 06. Archivos ocultos y staging
# En proyecto/ hay un archivo oculto .config_local y otro README.md.
# Ninguno está en .gitignore ni ha sido rastreado por Git.
# Ejecutas:
#
#     ls
#     git add .
#     git status
#
# ¿Qué afirmación es correcta?
#
# A) Como .config_local no aparece con ls, Git tampoco puede agregarlo.
# B) git add . solo prepara archivos con extensión visible, como .md.
# C) git add . ignora automáticamente todos los archivos que empiezan por .
# D) git add . puede preparar también .config_local, aunque sea oculto en ls.
respuesta_06 = ""


# PREGUNTA 07. Qué no versionar (SELECCIÓN MÚLTIPLE)
# Vas a publicar un proyecto. Selecciona TODOS los elementos que deben
# mantenerse fuera del repositorio. Cuando estén dentro del proyecto,
# asegúrate de ignorarlos apropiadamente con .gitignore si corresponde.
#
# A) README.md que explica cómo reproducir el análisis
# B) .env con tokens y contraseñas reales
# C) uv.lock que fija versiones de dependencias del proyecto
# D) .venv/ con el ambiente virtual local
# E) src/limpieza.py con funciones del proyecto
# F) data/pacientes.csv con información personal confidencial
# G) .gitignore con las reglas del proyecto
# H) una copia dentro del repo de id_ed25519 (llave SSH privada)
#
# Escribe una lista de letras, por ejemplo: ["A", "C"].
respuesta_07 = []


# PREGUNTA 08. Directorio de trabajo al ejecutar Python
# Estructura:
#
# proyecto/
# ├── data/
# │   └── muestra.csv
# ├── scripts/
# │   └── prueba.py
# └── pyproject.toml
#
# scripts/prueba.py contiene:
#     archivo = open("../data/muestra.csv")
#
# Estás en proyecto/ y ejecutas:
#     uv run python scripts/prueba.py
#
# Supón que el archivo CSV existe y tienes permisos de lectura.
# ¿Qué ocurre?
#
# A) Se abre proyecto/data/muestra.csv: ../ se calcula desde scripts/.
# B) Se abre proyecto/data/muestra.csv: uv run cambia a scripts/.
# C) La ruta se interpreta desde proyecto/, por lo que ../data/muestra.csv
#    apunta fuera de proyecto/ y no al CSV mostrado.
# D) El programa cambia automáticamente al directorio del notebook.
respuesta_08 = ""


# PREGUNTA 09. Interpretar un pipeline
# Ejecutas sobre un archivo de texto cuyos renglones son categorías:
#
#     grep -v '^#' categorias.txt | sort | uniq -c | sort -nr | head -3
#
# Las líneas que comienzan con # son comentarios. ¿Qué obtienes?
#
# A) Las tres categorías (líneas) más frecuentes, excluyendo líneas
#    que comienzan con #.
# B) Las tres primeras líneas del archivo, incluyendo comentarios.
# C) Las tres categorías que aparecen primero alfabéticamente, sin conteos.
# D) El número de caracteres de las tres líneas más largas.
respuesta_09 = ""


# PREGUNTA 10. Ruta relativa en la terminal
# Estructura:
#
# proyecto/
# ├── data/
# │   └── base.csv
# └── src/
#     └── utils/
#         └── limpieza.py
#
# Estás en proyecto/src/utils/. ¿Qué comando muestra las dos primeras
# líneas de base.csv sin cambiar de directorio?
#
# A) head -n 2 ../data/base.csv
# B) head -n 2 ./data/base.csv
# C) head -n 2 ../../../data/base.csv
# D) head -n 2 ../../data/base.csv
respuesta_10 = ""


# PREGUNTA 11. Redirección de salida
# Ya existe resultados.txt con notas anteriores. Ejecutas:
#
#     grep 'ERROR' logs.txt >> resultados.txt
#
# ¿Qué efecto tiene >> sobre resultados.txt?
#
# A) Lo sobrescribe con las coincidencias nuevas.
# B) Agrega las coincidencias al final sin borrar el contenido existente.
# C) Envía las coincidencias únicamente a la pantalla.
# D) Guarda solo un conteo de las coincidencias.
respuesta_11 = ""


# ============================================================
# III. GIT Y GITHUB
# ============================================================

# PREGUNTA 12. Configuración de git pull
# Al ejecutar git pull, Git avisa que las ramas han divergido y muestra:
#
#     git config pull.rebase false
#     git config pull.rebase true
#     git config pull.ff only
#
# Una persona decide ejecutar:
#     git config pull.rebase false
#
# ¿Qué está configurando?
#
# A) Que git pull utilice merge para reconciliar historiales divergentes,
#    en vez de rebase, cuando sea necesaria esa integración.
# B) Que git pull descarte los commits locales y copie la rama remota.
# C) Que git pull obtenga cambios sin integrarlos, igual que git fetch.
# D) Que Git resuelva todos los conflictos de merge sin intervención.
respuesta_12 = ""


# PREGUNTA 13. Regla en .gitignore
# Un proyecto tiene la regla:
#
#     *.csv
#
# Pero git status sigue mostrando modificaciones de data/historico.csv.
# ¿Cuál explicación es compatible con ese comportamiento?
#
# A) *.csv ignora solamente los archivos CSV de la raíz del repositorio.
# B) .gitignore no funciona hasta que se publique mediante git push.
# C) historico.csv ya estaba rastreado por Git antes de agregar la regla.
# D) Hay que cambiar la extensión del archivo a .CSV para ignorarlo.
respuesta_13 = ""


# PREGUNTA 14. Dos versiones de un archivo en Git
# Después de editar src/cleaning.py, ejecutaste git add src/cleaning.py.
# Luego editaste OTRA VEZ el mismo archivo y git status muestra:
#
# Changes to be committed:
#     modified: src/cleaning.py
# Changes not staged for commit:
#     modified: src/cleaning.py
#
# Si ejecutas git commit -m "Limpieza", ¿qué versión se registra?
#
# A) La versión con las ediciones más recientes, aunque no hicieras git add.
# B) La versión que estaba preparada cuando ejecutaste git add; las
#    ediciones posteriores quedan fuera de ese commit.
# C) Las dos versiones en dos commits diferentes, creados automáticamente.
# D) No se crea el commit porque un archivo no puede aparecer en ambos grupos.
respuesta_14 = ""


# PREGUNTA 15. Push rechazado
# Ejecutas git push y obtienes:
#
#     ! [rejected] main -> main (fetch first)
#     error: failed to push some refs
#     hint: Updates were rejected because the remote contains
#     hint: work that you do not have locally.
#
# ¿Cuál de las siguientes acciones aborda la causa del rechazo sin
# sobrescribir deliberadamente el trabajo de otras personas?
#
# A) Ejecutar git add . y repetir git push, sin revisar el historial remoto.
# B) Ejecutar git fetch origin y repetir git push sin integrar commits.
# C) Ejecutar git push --force para reemplazar el historial de main remoto.
# D) Obtener e integrar los commits remotos en la rama local (resolviendo
#    posibles conflictos), y después volver a intentar git push.
respuesta_15 = ""


# ============================================================
# SALIDA DEL EXAMEN — NO MODIFICAR
# ============================================================

respuestas = [
    respuesta_01, respuesta_02, respuesta_03, respuesta_04, respuesta_05,
    respuesta_06, respuesta_07, respuesta_08, respuesta_09, respuesta_10,
    respuesta_11, respuesta_12, respuesta_13, respuesta_14, respuesta_15,
]

print(f"\nMIDTERM (VERSIÓN B) — {nombre}")
print("=" * 42)
for numero, respuesta in enumerate(respuestas, start=1):
    if isinstance(respuesta, list):
        texto = ", ".join(respuesta) if respuesta else "SIN RESPUESTA"
    else:
        texto = str(respuesta).strip() or "SIN RESPUESTA"
    print(f"Pregunta {numero:02d}: {texto}")
print("=" * 42)
