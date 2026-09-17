## Temario general

### 1. Introducción a la programación e infraestructura

- ¿Qué significa programar en un proyecto de ciencia de datos?
- Cómo funciona un entorno de programación:
  - sistema operativo;
  - sistema de archivos;
  - terminal;
  - procesos.
- Diferencia entre trabajar de manera local y remota.
- Configuración del entorno local:
  - instalación de Python;
  - instalación de Git;
  - VS Code;
  - WSL2 en Windows;
  - terminal en macOS/Linux.
- Estructura básica de un proyecto de ciencia de datos.
- Relación entre:
  - código;
  - datos;
  - dependencias;
  - configuración;
  - resultados.
- Reproducibilidad en proyectos de ciencia de datos para políticas públicas.

### 2. Bash y CLI esencial

- ¿Qué es una shell?
- Navegación por el sistema de archivos:
  - `pwd`;
  - `ls`;
  - `cd`.
- Rutas relativas y absolutas.
- Manipulación de archivos y directorios:
  - `mkdir`;
  - `touch`;
  - `cp`;
  - `mv`;
  - `rm`.
- Visualización de archivos:
  - `cat`;
  - `head`;
  - `tail`;
  - `less`.
- Búsqueda de información:
  - `grep`;
  - `find`.
- Entrada y salida estándar.
- Redirecciones:
  - `>`;
  - `>>`.
- Pipes:
  - `|`.
- Permisos básicos.
- Ejecución de scripts desde terminal.
- Uso de CLI para inspeccionar datos, logs y resultados de procesos.

### 3. Git y GitHub: versionamiento y colaboración

- ¿Por qué versionar código y análisis?
- Repositorio local y repositorio remoto.
- Flujo básico de Git:
  - `git status`;
  - `git add`;
  - `git commit`;
  - `git push`;
  - `git pull`.
- Historial de cambios:
  - `git log`.
- Revisión de modificaciones:
  - `git diff`.
- Ramas:
  - creación;
  - cambio entre ramas;
  - integración mediante `merge`.
- Resolución básica de conflictos.
- GitHub como plataforma de colaboración.
- Pull requests.
- Issues.
- `.gitignore`.
- Buenas prácticas para commits.
- Git como herramienta para documentar y auditar cambios en análisis de datos.

### 4. Proyectos de Python reproducibles

- ¿Qué es un ambiente virtual?
- Dependencias y versiones.
- Problemas de reproducibilidad.
- Estructura de un proyecto de Python para ciencia de datos.
- Introducción a `uv`.
- Crear y administrar ambientes.
- Instalar y eliminar dependencias.
- `pyproject.toml`.
- `uv.lock`.
- Sincronización de ambientes:
  - `uv sync`.
- Ejecución de código dentro del ambiente:
  - `uv run`.
- Diferencia entre notebooks y scripts.
- Organización de:
  - código;
  - datos;
  - resultados;
  - documentación.
- Reproducibilidad entre distintas computadoras y personas.

### 5. Variables de entorno, credenciales y configuración

- Diferencia entre código y configuración.
- ¿Qué es una variable de entorno?
- Consultar y definir variables desde terminal.
- Uso de variables de entorno desde Python.
- Archivos `.env`.
- `.env.example`.
- Manejo de:
  - passwords;
  - API keys;
  - tokens.
- Por qué no deben almacenarse credenciales directamente en el código.
- Relación con `.gitignore`.
- Configuración de proyectos en diferentes entornos.
- Riesgos al compartir repositorios.
- Manejo responsable de información sensible y datos administrativos.

### 6. Datos, SQL y bases de datos

- Archivos tabulares versus bases de datos.
- Limitaciones de CSV y Excel.
- Introducción al modelo relacional.
- Tablas, filas y columnas.
- Llaves primarias.
- Llaves foráneas.
- Relaciones entre tablas.
- SQL básico:
  - `SELECT`;
  - `FROM`;
  - `WHERE`;
  - `ORDER BY`;
  - `GROUP BY`;
  - funciones de agregación.
- Combinación de tablas mediante `JOIN`.
- Conexión desde Python a una base de datos.
- Introducción a PostgreSQL.
- Separación entre:
  - almacenamiento;
  - consulta;
  - procesamiento;
  - análisis.
- Consideraciones para trabajar con datos administrativos en política pública.

### 7. Análisis de datos en CLI

- Inspección rápida de archivos de datos.
- Conteo de observaciones:
  - `wc`.
- Búsqueda de patrones:
  - `grep`.
- Ordenamiento:
  - `sort`.
- Eliminación de duplicados:
  - `uniq`.
- Composición de comandos mediante pipes.
- Inspección rápida de archivos grandes.
- Revisión de logs.
- Verificación de resultados sin abrir un notebook.
- Cuándo utilizar CLI y cuándo utilizar Python.

### 8. Docker y ambientes reproducibles

- El problema de “en mi computadora funciona”.
- ¿Qué es un contenedor?
- Diferencia entre imagen y contenedor.
- Docker versus máquina virtual.
- Introducción al `Dockerfile`.
- Construcción de imágenes:
  - `docker build`.
- Ejecución de contenedores:
  - `docker run`.
- Puertos.
- Volúmenes.
- Variables de entorno en contenedores.
- Introducción a `docker compose`.
- Ejemplo de servicios múltiples:
  - Python;
  - PostgreSQL.
- Uso de contenedores para análisis reproducibles.
- Contenedores como entornos controlados para ejecutar código.

### 9. APIs y servicios externos

- ¿Qué es una API?
- Cliente y servidor.
- Introducción a HTTP.
- URLs y endpoints.
- Métodos principales:
  - `GET`;
  - `POST`.
- Parámetros.
- Headers.
- Códigos de respuesta.
- JSON.
- Consumo de APIs desde Python.
- Uso de `requests`.
- Autenticación.
- API keys y tokens.
- Paginación.
- Manejo básico de errores.
- Límites de uso.
- Lectura de documentación de APIs.
- Obtención de datos públicos mediante APIs.

### 10. Automatización y verificación automática

- ¿Qué tareas de ciencia de datos conviene automatizar?
- Scripts para procesos repetitivos.
- Introducción a workflows.
- GitHub Actions.
- Eventos:
  - `push`;
  - `pull request`.
- Ejecución automática de scripts.
- Instalación automática de dependencias.
- Ejecución de pruebas.
- Verificación de que un proyecto corre correctamente.
- Introducción a:
  - tests;
  - linters;
  - formatters.
- CI como mecanismo de control de calidad.
- Automatización de pipelines de ciencia de datos.

### 11. Agentes de programación

- Diferencia entre:
  - chatbot;
  - asistente de código;
  - agente.
- ¿Qué puede hacer un agente?
  - leer archivos;
  - explorar repositorios;
  - modificar código;
  - ejecutar comandos;
  - consultar documentación;
  - correr pruebas.
- Dar contexto a un agente.
- Formular tareas computacionales.
- Pedir que explore antes de modificar.
- Planeación antes de ejecución.
- División de problemas grandes en tareas pequeñas.
- Supervisión del trabajo de un agente.
- Revisión de:
  - archivos modificados;
  - `git diff`;
  - comandos ejecutados;
  - resultados;
  - pruebas.
- Verificación de código generado.
- Detección de soluciones plausibles pero incorrectas.
- Uso de documentación oficial para validar resultados.
- Permisos y niveles de autonomía:
  - lectura;
  - modificación;
  - ejecución;
  - acceso a red.
- Riesgos relacionados con:
  - datos confidenciales;
  - credenciales;
  - información institucional.
- Uso responsable de agentes en proyectos de ciencia de datos para políticas públicas.
- Git como mecanismo para auditar y revertir cambios producidos por agentes.
