# Introducción a la programación para políticas públicas 

## 1.1 Programación para ciencia de datos

### Motivación

Como científicos de datos diseñamos, construimos y desarrollamos **productos de datos**: sistemas que utilizan información existente y se integran en el contexto específico de las organizaciones para apoyar a los tomadores de decisiones. Estos productos están diseñados para colocar información clave de manera **oportuna**, **confiable** y **accionable**.

- Resuelven problemas específicos.
- Están basados en datos.
- Tienen un impacto directo en la política pública.

A lo largo de todas las etapas del diseño de un producto de datos, es fundamental conocer las herramientas que nos permiten ser más eficientes en el manejo, transformación y análisis de la información.


![](../imgs/pipeline.png)

### ¿Qué significa programar?

> Programar es hablar con las computadoras, decirles qué quieres que hagan, no sólo una vez, sino de formas que persistan; que puedan variar como el lenguaje humano, con una estructura repetible pero con distintos verbos y objetos.  
> — *Tim O'Reilly (2021)*


Programar consiste en escribir instrucciones que una computadora puede ejecutar para realizar una tarea.

En ciencia de datos, estas instrucciones pueden utilizarse para:

* descargar datos;
* limpiar y transformar información;
* consultar bases de datos;
* automatizar procesos;
* construir modelos;
* producir tablas y visualizaciones;
* generar reportes;
* evaluar políticas públicas.

Por ejemplo, un programa puede contener instrucciones para leer una base de datos y calcular el promedio de una variable:

```python
import pandas as pd

df = pd.read_csv("datos.csv")

print(df["ingreso"].mean())
```


Para que este código se ejecute correctamente, necesitamos un **entorno de programación**.


## 1.2 El entorno de programación

Cuando ejecutamos código intervienen diferentes componentes.

Una representación simplificada es:

```text
Computadora
│
├── Sistema operativo
│
├── Sistema de archivos
│
├── Terminal / Shell
│
├── Lenguajes e intérpretes
│   └── Python
│
├── Herramientas
│   └── Git
│
├── Editor de código
│   └── VS Code
│
└── Proyecto
    ├── código
    ├── datos
    ├── dependencias
    └── configuración
```

Durante el curso aprenderemos a interactuar con varias de estas capas.

El objetivo no es convertirnos en especialistas en administración de sistemas, sino entender lo suficiente sobre nuestro entorno para poder:

* ejecutar código;
* identificar errores;
* trabajar de forma reproducible;
* colaborar con otras personas;
* utilizar agentes y herramientas de inteligencia artificial de manera informada.


## 1.3 Sistema operativo

El **sistema operativo** es el software principal que administra los recursos de una computadora.

Algunos ejemplos son:

* Windows;
* macOS;
* Linux.

El sistema operativo administra, entre otras cosas:

* archivos;
* memoria;
* programas;
* procesos;
* dispositivos;
* permisos.

Aunque Python funciona en los tres sistemas operativos, existen diferencias importantes en la manera de interactuar con ellos.

En este curso buscaremos trabajar con un entorno similar a Linux.

### macOS y Linux

macOS y Linux incluyen terminales que permiten utilizar muchas herramientas de tipo Unix directamente.

### Windows

En Windows utilizaremos **WSL2 (Windows Subsystem for Linux)**.

WSL permite ejecutar un entorno Linux dentro de Windows.

Conceptualmente tendremos:

```text
Windows
│
└── WSL
    │
    └── Linux
        ├── terminal
        ├── Python
        ├── Git
        └── otras herramientas
```

Esto permite que quienes utilizan Windows trabajen en un entorno similar al de quienes utilizan macOS o Linux.



## 1.4 Sistema de archivos

El **sistema de archivos** organiza la información almacenada en nuestra computadora.

Los principales elementos son:

* archivos;
* directorios o carpetas;
* rutas.

Por ejemplo:

```text
proyecto/
│
├── data/
│   └── encuesta.csv
│
├── scripts/
│   └── analisis.py
│
└── README.md
```

Aquí `proyecto` contiene dos directorios y un archivo.

### Rutas

Una ruta indica la ubicación de un archivo o directorio.

Por ejemplo:

```text
proyecto/data/encuesta.csv
```

Durante el curso utilizaremos continuamente rutas para indicar dónde se encuentran:

* bases de datos;
* scripts;
* configuraciones;
* resultados.

Más adelante distinguiremos entre:

* rutas absolutas;
* rutas relativas.


## 1.5 Terminal y sheel

La **terminal** es una interfaz que nos permite interactuar con la computadora utilizando texto.

En lugar de abrir una carpeta haciendo clic, podemos escribir:

```bash
cd proyecto
```

En lugar de crear una carpeta desde una interfaz gráfica, podemos escribir:

```bash
mkdir data
```

La terminal será una herramienta central durante el curso.

Nos permitirá:

* navegar entre archivos;
* ejecutar programas;
* utilizar Git;
* instalar herramientas;
* administrar ambientes;
* ejecutar scripts;
* trabajar con Docker;
* interactuar con servidores;
* supervisar acciones realizadas por agentes.


### Terminal y shell no son exactamente lo mismo

Aunque frecuentemente utilizamos ambos términos como sinónimos, conceptualmente son diferentes.

La **terminal** es la interfaz donde escribimos comandos.

La **shell** es el programa que interpreta esos comandos.

Algunas shells comunes son:

* `bash`;
* `zsh`;
* `fish`;
* PowerShell.

Por ejemplo, al escribir:

```bash
pwd
```

la shell interpreta el comando y solicita al sistema operativo mostrar el directorio en el que nos encontramos.

En macOS moderno, la shell predeterminada suele ser `zsh`.

En muchos sistemas Linux es común encontrar `bash`.

Durante el curso los comandos que utilizaremos serán compatibles, en su mayoría, con ambas.


## 1.6 Programas e intérpretes

Python es un **lenguaje de programación**, pero para ejecutar código necesitamos tener instalado un programa capaz de interpretarlo.

Podemos verificar si Python se encuentra disponible escribiendo:

```bash
python --version
```

o, dependiendo del sistema:

```bash
python3 --version
```

Conceptualmente ocurre algo como:

```text
archivo_instrucciones.py
    │
    ▼
Python
    │
    ▼
Sistema operativo
    │
    ▼
Resultado
```


## 1.7 Procesos

Cuando ejecutamos un programa, el sistema operativo crea un **proceso**.

Un proceso es, de manera simplificada, un programa que se encuentra en ejecución.

Por ejemplo, si ejecutamos:

```bash
python analisis.py
```

el sistema operativo crea un proceso de Python.

También son procesos:

* VS Code;
* un navegador;
* PostgreSQL;
* Jupyter;
* Docker.

Esto será importante posteriormente cuando ejecutemos tareas que:

* tardan varios minutos;
* utilizan muchos recursos;
* corren como servicios;
* se ejecutan dentro de contenedores.



## 1.8 Git

Git es un sistema de **control de versiones**.

Nos permite registrar los cambios que hacemos en un proyecto.

Conceptualmente:

```text
Proyecto
│
├── versión 1
│
├── versión 2
│
├── versión 3
│
└── versión actual
```

Con Git podemos:

* conocer qué archivos cambiaron;
* revisar exactamente qué cambió;
* regresar a una versión anterior;
* trabajar con otras personas;
* experimentar sin destruir una versión funcional del proyecto.

Más adelante utilizaremos Git de manera intensiva.

Por ahora únicamente verificaremos que se encuentre instalado:

```bash
git --version
```


## 1.9 ¿Qué es un proyecto reproducible?

Uno de los conceptos centrales del curso será la **reproducibilidad**.

Supongamos que realizamos un análisis para evaluar una política pública.

Tenemos:

```text
datos
  +
código
  +
dependencias
  +
configuración
  ↓
resultados
```

Un análisis es reproducible cuando otra persona puede utilizar esos elementos y obtener los mismos resultados.

No basta con enviar:

```text
analisis_final_v7_ahora_si_final.ipynb
```

También necesitamos conocer:

* qué datos se utilizaron;
* qué versión del código;
* qué paquetes fueron necesarios;
* qué versiones de esos paquetes;
* cómo se configuró el entorno;
* qué pasos produjeron los resultados.

Durante el curso iremos incorporando herramientas para resolver cada una de estas preguntas.


## 1.10 ¿Por qué importa la reproducibilidad en política pública?

Los análisis utilizados en política pública pueden servir para:

* describir un problema;
* asignar recursos;
* identificar población beneficiaria;
* evaluar programas;
* producir indicadores;
* desarrollar modelos predictivos;
* informar decisiones públicas.

Por ello, resulta importante poder responder preguntas como:

* ¿de dónde vienen los datos?;
* ¿qué transformaciones se realizaron?;
* ¿qué código produjo una cifra?;
* ¿qué versión del análisis se utilizó?;
* ¿podemos volver a ejecutar el análisis?;
* ¿otra persona podría auditarlo?;
* ¿podemos actualizarlo cuando lleguen nuevos datos?

La reproducibilidad no es únicamente un problema técnico.

También está relacionada con:

* transparencia;
* trazabilidad;
* colaboración;
* mantenimiento;
* auditoría.

## 1.11 Un modelo mental para el curso

A lo largo del curso construiremos progresivamente un proyecto que puede verse de esta forma:

```text
Proyecto de ciencia de datos
│
├── datos
│
├── código
│
├── base de datos
│
├── dependencias
│
├── configuración
│
├── credenciales
│
├── documentación
│
├── pruebas
│
└── resultados
        │
        ▼
   reproducibilidad
```

Sobre esta estructura iremos incorporando herramientas como:

```text
Bash
Git
GitHub
Python
uv
SQL
Docker
APIs
CI/CD
```

Estas herramientas no son temas aislados.

Cada una resuelve una parte distinta del problema de construir análisis computacionales que puedan ser entendidos, compartidos y reproducidos.



## 1.12 Primer ejercicio: verificar nuestro entorno

El objetivo de este ejercicio es verificar que las herramientas básicas funcionan.

### Paso 1. Abrir una terminal

Abre la terminal correspondiente a tu sistema.

Verifica en qué directorio te encuentras:

```bash
pwd
```


### Paso 2. Crear un directorio para el ejercicio

```bash
mkdir intro-programacion
```

Entra al directorio:

```bash
cd intro-programacion
```

Verifica dónde te encuentras:

```bash
pwd
```


## Para recordar

Durante el curso no necesitamos memorizar todos los comandos.

Lo importante es construir un modelo mental de cómo se relacionan las herramientas.

```text
Sistema operativo
      ↓
Sistema de archivos
      ↓
Terminal / Shell
      ↓
Herramientas
  ├── Python
  └── Git
      ↓
Proyecto
      ↓
Código + Datos + Configuración
      ↓
Resultados reproducibles
```

A partir de la siguiente sesión comenzaremos a interactuar con este entorno utilizando **Bash y la línea de comandos**.


## Detalle de herramientas

### "Social coding"

[<img src="https://about.gitlab.com/images/press/logo/print/jpg/gitlab-logo-150.jpg" width="140"/>](gitlab.com)

Gitlab es una herramienta que permite gestionar, administrar, colaborar, supervisar código por medio de repositorios. Está construido sobre Git, que es un sistema de control de versiones que realiza un seguimiento de los cambios en cualquier conjunto de archivos de computadora. Generalmente se usa para coordinar trabajo entre personas que desarrollan código fuente en colaboración. 

Se tiene un repositorio por proyecto donde se deposita todo el código y se hace la colaboración correspondiente para su desarrollo. 

### Lenguajes de programación 

[<img src="https://www.python.org/static/community_logos/python-logo.png" width="200"/>](https://www.python.org/psf/about/)

Uno de los programas que más se utiliza para Ciencia de datos, es Python por ser un Software libre y de fácil aprendizaje.

### Almacenamiento de bases de datos

[<img src="https://www.postgresql.org/media/img/about/press/elephant.png" width="65"/>](https://www.postgresql.org/)

PostgreSQl es un sistema de gestión de bases de datos relacionales de código abierto y utiliza SQL como lenguaje de consulta.


