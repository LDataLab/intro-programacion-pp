# Tarea 1. Configuración del entorno de programación

El objetivo de esta tarea es configurar el entorno de programación que utilizaremos durante el curso.

Al finalizar deberás contar con:

```text
Windows                         macOS
   │                               │
   ▼                               ▼
WSL2                           Terminal
   │                               │
   ▼                               ▼
Ubuntu                         macOS / Unix
   │                               │
   └──────────────┬────────────────┘
                  │
                  ▼
              bash / zsh
                  │
                  ▼
           Git + uv + Python
```

A partir de este punto buscaremos que, independientemente del sistema operativo de tu computadora, trabajemos con herramientas y comandos lo más similares posible.


## Parte 1. Identifica tu sistema operativo

Sigue únicamente las instrucciones correspondientes a tu computadora:

* **Windows:** continúa con la Parte 2A.
* **macOS:** continúa con la Parte 2B.
* **Linux:** puedes seguir las instrucciones de macOS/Linux a partir de la instalación de Git.


## Parte 2A. Windows: instalar WSL2 y Ubuntu

En Windows utilizaremos **WSL2 (Windows Subsystem for Linux)**.

WSL nos permite tener un entorno Linux dentro de Windows. Durante el curso trabajaremos principalmente dentro de este entorno.

### 1. Abrir PowerShell como administrador

Busca **PowerShell** en el menú de inicio.

Haz clic derecho y selecciona:

> Ejecutar como administrador


### 2. Instalar WSL

Ejecuta:

```powershell
wsl --install
```

Este comando instalará WSL y, de manera predeterminada, una distribución de Ubuntu.

Es posible que tu computadora solicite reiniciarse.

Después de reiniciar, abre **Ubuntu** desde el menú de inicio.


### 3. Crear tu usuario de Ubuntu

La primera vez que abras Ubuntu se te pedirá crear:

* un nombre de usuario;
* una contraseña.

Esta cuenta pertenece a tu entorno Linux y es independiente de tu usuario de Windows.

> **Importante:** cuando escribas la contraseña en la terminal no aparecerán caracteres en pantalla. Esto es normal.


### 4. Verificar que estás utilizando WSL2

Desde PowerShell ejecuta:

```powershell
wsl -l -v
```

Deberás observar tu distribución de Ubuntu y, en la columna `VERSION`, el número:

```text
2
```

Si Ubuntu aparece utilizando WSL2, la instalación fue exitosa.


### 5. Abrir Ubuntu

A partir de este punto, salvo que se indique lo contrario, los comandos del curso deberán ejecutarse **dentro de la terminal de Ubuntu**, no en PowerShell.

Puedes reconocerla porque tu prompt tendrá una apariencia similar a:

```text
usuario@computadora:~$
```

### 6. Actualizar Ubuntu

Dentro de Ubuntu ejecuta:

```bash
sudo apt update
```

y posteriormente:

```bash
sudo apt upgrade -y
```

Es posible que Ubuntu solicite la contraseña que creaste anteriormente.


## Parte 2B. macOS: abrir la terminal

macOS ya cuenta con un entorno tipo Unix, por lo que **no** necesitamos instalar WSL.

### 1. Abrir Terminal

Puedes encontrarla en:

```text
Aplicaciones → Utilidades → Terminal
```

También puedes abrir Spotlight y buscar:

```text
Terminal
```


### 2. Identificar la shell

Ejecuta:

```bash
echo $SHELL
```

Probablemente observarás algo similar a:

```text
/bin/zsh
```

Durante el curso utilizaremos principalmente comandos que funcionan tanto en `zsh` como en `bash`.


## Parte 3. Verificar la terminal

A partir de aquí, tanto usuarios de **Windows con Ubuntu/WSL** como usuarios de **macOS** pueden seguir instrucciones muy similares.

Ejecuta:

```bash
pwd
```

Este comando muestra el directorio en el que te encuentras.

Después ejecuta:

```bash
whoami
```

Este comando muestra tu usuario.

Finalmente:

```bash
uname -a
```

Este comando muestra información sobre el sistema en el que estás trabajando.

No es necesario entender todavía toda la información que aparece.


## Parte 4. Instalar Git

Git será el sistema de control de versiones que utilizaremos durante el curso.

### Windows + WSL / Ubuntu

Dentro de Ubuntu ejecuta:

```bash
sudo apt install git -y
```

Después verifica la instalación:

```bash
git --version
```

Deberás observar algo similar a:

```text
git version 2.x.x
```


### macOS

Primero verifica si Git ya se encuentra disponible:

```bash
git --version
```

Si Git no está instalado, macOS puede solicitar automáticamente la instalación de las **Command Line Tools**.

También puedes iniciar manualmente la instalación con:

```bash
xcode-select --install
```

Al terminar, vuelve a ejecutar:

```bash
git --version
```

## Parte 5. Configurar Git

Configura el nombre que aparecerá en tus commits:

```bash
git config --global user.name "Tu Nombre"
```

Configura también tu correo electrónico:

```bash
git config --global user.email "tu_correo@ejemplo.com"
```

Verifica la configuración:

```bash
git config --global --list
```

Deberás poder identificar tu nombre y correo.


## Parte 6. Crear nuestro espacio de trabajo

Crearemos un directorio donde podremos guardar proyectos del curso.

Ejecuta:

```bash
mkdir -p ~/projects
```

Entra al directorio:

```bash
cd ~/projects
```

Verifica tu ubicación:

```bash
pwd
```

## Nota para usuarios de Windows

Si utilizas WSL, procura guardar los proyectos del curso dentro de tu sistema de archivos Linux, por ejemplo:

```text
~/projects
```

y no directamente dentro de:

```text
C:\Users\...
```

Más adelante veremos con mayor detalle qué significa esta diferencia.


## Parte 11. Inicializar Git

Dentro de tu proyecto ejecuta:

```bash
git init
```

Después:

```bash
git status
```

No es necesario hacer ningún commit todavía.

Por ahora solamente queremos comprobar que Git puede reconocer nuestro proyecto.


## Parte 12. Verificación final

Ejecuta los siguientes comandos:

```bash
pwd
```

```bash
uname -a
```

```bash
git --version
```

```bash
git status
```


# Entrega

Entrega **una captura de pantalla de tu terminal** en la que puedan observarse los resultados de los siguientes comandos:

```bash
git --version
pwd
```

La captura debe permitir verificar que los comandos se ejecutaron correctamente.

---

# Checklist

Antes de entregar verifica que:

* [ ] Puedo abrir la terminal que utilizaré durante el curso.
* [ ] Si tengo Windows, instalé WSL2 y Ubuntu.
* [ ] Si tengo Windows, estoy ejecutando los comandos dentro de Ubuntu.
* [ ] Git está instalado.
* [ ] Configuré mi nombre y correo en Git.
* [ ] Creé el directorio `~/projects`.
* [ ] Creé el proyecto `tarea-1`.
* [ ] Puedo ejecutar `git status`.
* [ ] El mensaje `Todo listo para comenzar` aparece correctamente.

---

# ¿Qué acabamos de configurar?

Al finalizar esta tarea tenemos:

```text
Sistema operativo
      │
      ▼
Terminal / Shell
      │
      ▼
Git 
      │
      ▼
Python
      │
      ▼
Proyecto
```

Todavía no necesitamos entender en detalle cómo funciona cada una de estas piezas.

A lo largo del curso iremos estudiando **qué hace cada herramienta, cómo se relacionan y por qué son importantes para construir proyectos reproducibles de ciencia de datos**.

