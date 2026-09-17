## Parte 6. Instalar `uv`

Durante el curso utilizaremos **`uv`** para administrar:

* versiones de Python;
* ambientes virtuales;
* dependencias;
* proyectos de Python.

Esto significa que no necesitamos instalar Python manualmente por separado.

En **Ubuntu/WSL y macOS**, ejecuta:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Cuando termine la instalación, **cierra y vuelve a abrir la terminal**.

Después verifica:

```bash
uv --version
```

Deberás observar algo similar a:

```text
uv 0.x.x
```

> La versión exacta puede ser diferente.

---

# Parte 7. Instalar Python con `uv`

Primero consulta las versiones de Python disponibles:

```bash
uv python list
```

Después instala Python 3.12:

```bash
uv python install 3.12
```

Verifica nuevamente:

```bash
uv python list
```

Deberás poder identificar una instalación de Python 3.12 administrada por `uv`.

---


