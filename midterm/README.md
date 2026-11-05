# Midterm: Fundamentos técnicos de programación

Este examen evalúa los fundamentos técnicos trabajados durante el curso: CLI, sistema de archivos, rutas, Git, GitHub, ambientes virtuales y organización de proyectos Python.

El examen es **individual**. Pueden consultar las notas del curso, pero no utilizar herramientas de inteligencia artificial ni buscadores. 

## 1. Preparar el espacio de trabajo

El examen se encuentra en la rama `midterm`. Cada estudiante deberá crear una rama individual a partir de ella, **no de `main`**.

Desde la raíz del repositorio, ejecuten:

```bash
# Descargar la información más reciente del repositorio remoto,
# sin integrar cambios en la rama actual
git fetch origin

# Crear una nueva rama a partir de origin/midterm
# y cambiar a ella. Reemplazar nombre por su usuario de GitHub
git switch -c midterm-nombre origin/midterm
```

Verifiquen que están en la rama correcta antes de continuar. No es necesario eliminar sus ramas anteriores.

## 2. Responder el examen

Dentro de la carpeta `midterm/` encontrarán:

```text
midterm_plantilla.py
```

Creen una copia llamada `midterm_<nombre>.py`, utilizando su nombre.

- No modifiquen el archivo original.
- Coloquen su nombre y completen las variables `respuesta_01`, `respuesta_02`, etc.
- En las preguntas de selección múltiple, respeten el formato indicado.
- Mantengan la estructura del script.

## 3. Ejecutar y verificar

Desde la raíz del repositorio, ejecuten:

```bash
uv run python midterm/midterm_<nombre>.py
```

Verifiquen que el programa se ejecuta sin errores y muestra todas sus respuestas.

## 4. Entrega mediante Pull Request

Una vez terminada la evaluación, registren sus cambios con Git, publíquenlos en GitHub y abran un **Pull Request** con las siguientes características:

- **Rama de origen:** `midterm-nombre`
- **Rama de destino:** `midterm`
- **Contenido:** únicamente su archivo individual de respuestas.

**No hagan merge del Pull Request.** Déjenlo abierto para revisión.

La evaluación considerará tanto las respuestas del examen como el uso correcto del flujo de trabajo con Git y GitHub.

¡Éxito!
