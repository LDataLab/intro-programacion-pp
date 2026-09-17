# Instalación de Python

Para trabajar con Python de manera local necesitamos instalarlo directamente en nuestra computadora.

A continuación se presentan las instrucciones para **Windows** y **macOS**.

---

## Windows

### 1. Descargar Python

Ingresa al sitio oficial de Python:

https://www.python.org/downloads/

Descarga una versión reciente de **Python 3** para Windows.

### 2. Ejecutar el instalador

Abre el archivo que descargaste.

Antes de comenzar la instalación, asegúrate de seleccionar la opción:

```text
☑ Add python.exe to PATH
```

> **Importante:** Esta opción permite ejecutar Python directamente desde la terminal.

Después selecciona **Install Now** y espera a que termine la instalación.

### 3. Abrir una terminal

En Windows utilizaremos **PowerShell**.

Puedes abrirlo buscando:

```text
PowerShell
```

en el menú de inicio.

### 4. Comprobar la instalación

En PowerShell escribe:

```powershell
python --version
```

Deberías obtener algo parecido a:

```text
Python 3.13.7
```

El número exacto de versión puede ser diferente.

Si el comando `python` no funciona, prueba:

```powershell
py --version
```

Si alguno de los dos comandos muestra una versión de **Python 3**, la instalación fue exitosa.

---

## macOS

### 1. Descargar Python

Ingresa al sitio oficial de Python:

https://www.python.org/downloads/

Descarga una versión reciente de **Python 3** para macOS.

El sitio debería detectar automáticamente que estás utilizando una Mac.

### 2. Ejecutar el instalador

Abre el archivo `.pkg` que descargaste y sigue los pasos del instalador.

Puedes conservar las opciones predeterminadas.

### 3. Abrir la Terminal

Puedes abrir Spotlight utilizando:

```text
⌘ + espacio
```

Escribe:

```text
Terminal
```

y presiona **Enter**.

### 4. Comprobar la instalación

En la Terminal escribe:

```bash
python3 --version
```

Deberías obtener algo parecido a:

```text
Python 3.13.7
```

El número exacto de versión puede ser diferente.

En macOS utilizaremos normalmente el comando `python3` en lugar de `python`.

---

## Comprobación final

Al terminar la instalación debes poder obtener la versión de Python desde una terminal.

| Sistema operativo | Comando |
|---|---|
| Windows | `python --version` |
| Windows (alternativa) | `py --version` |
| macOS | `python3 --version` |

No es necesario que todas las personas tengan exactamente la misma versión de Python. Lo importante por ahora es tener instalada una versión reciente de **Python 3** y poder ejecutarla desde la terminal.

> **¿Algo no funcionó?**
>
> No realices instalaciones adicionales ni modifiques variables del sistema por tu cuenta. Anota el error o toma una captura de pantalla para revisarlo durante la clase.