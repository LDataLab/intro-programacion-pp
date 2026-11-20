# Práctica: Neo4j con Docker

En esta práctica utilizaremos Docker para levantar una **base de datos de grafos con Neo4j**, crear una pequeña red de colaboración entre personas y proyectos y explorarla desde el navegador.

A diferencia de las bases de datos relacionales, que organizan la información en tablas, Neo4j representa la información mediante **nodos**, **relaciones** y **propiedades**. Para crear y consultar el grafo utilizaremos **Cypher**.

## 1. Estructura de archivos

Esta práctica forma parte de la carpeta `docker/` del repositorio:

```text
docker/
├── bashquiz/
├── api/
├── neo4j/
│   ├── Dockerfile
│   └── README.md
└── compose.yaml
```

Ejecutaremos los comandos de Docker Compose desde `docker/`, donde está el archivo `compose.yaml`.

## 2. Dockerfile de Neo4j

En `docker/neo4j/Dockerfile`:

```dockerfile
# Imagen oficial de Neo4j Community Edition
FROM neo4j:2026.10.2-community
```

Por ahora basta con la imagen oficial: ya incluye el servidor Neo4j. Conservamos un `Dockerfile` porque más adelante podríamos personalizar esta imagen agregando configuraciones, scripts o extensiones compatibles.

**Importante:** el software y la configuración pueden incorporarse a una imagen; los datos de una base que queremos conservar normalmente se guardan en un volumen.

## 3. Configurar el servicio en Compose

En `docker/compose.yaml`, agrega el servicio `neo4j` **dentro de `services:`**, junto a `bashquiz` y `api`:

```yaml
  neo4j:
    build: ./neo4j
    image: neo4jclase
    ports:
      - "127.0.0.1:7474:7474"
      - "127.0.0.1:7687:7687"
    environment:
      NEO4J_AUTH: neo4j/dockerclase123
    volumes:
      - neo4j_data:/data
```

Al final de `compose.yaml`, **fuera de `services:`**, declara el volumen:

```yaml
volumes:
  neo4j_data:
```

¿Qué significa cada elemento?

- `build`: indica dónde está el contexto de construcción de la imagen.
- `image`: asigna el nombre `neo4jclase` a nuestra imagen.
- `7474`: puerto HTTP utilizado por Neo4j Browser.
- `7687`: puerto Bolt para conectarse a la base de datos.
- `127.0.0.1`: limita el acceso a los puertos publicados a nuestra computadora local.
- `NEO4J_AUTH`: establece el usuario y la contraseña iniciales para esta práctica.
- `neo4j_data:/data`: almacena los archivos de la base en un volumen administrado por Docker.

> **Nota de seguridad:** `dockerclase123` es una contraseña de ejemplo para uso local. No debe utilizarse para una base de datos real ni publicarse junto con credenciales privadas.

## 4. Construir y ejecutar Neo4j

Desde la carpeta `docker/`:

```bash
docker compose build neo4j
docker compose up -d neo4j
```

Verifica el estado del servicio:

```bash
docker compose ps
```

Consulta los mensajes de inicio:

```bash
docker compose logs -f neo4j
```

Neo4j puede tardar un poco en iniciar la primera vez. Cuando esté listo, abre:

**http://localhost:7474**

En Neo4j Browser, conecta con:

```text
URI: bolt://localhost:7687
Usuario: neo4j
Contraseña: dockerclase123
```

Si ya habías creado la base con otra contraseña, cambiar `NEO4J_AUTH` en Compose **no cambia** la contraseña del volumen existente.

## 5. Crear nuestro primer grafo

Vamos a representar una red de personas que participan en proyectos de ciencia de datos:

- **Personas:** Ana, Luis, María y Pedro.
- **Proyectos:** Machine Learning, Datos Abiertos e IA para Gobierno.
- **Relaciones:** `COLABORA_EN` y `CONOCE`.

En Neo4j Browser, copia y ejecuta esta consulta **una sola vez**:

```cypher
CREATE
  (ana:Persona {nombre: 'Ana'}),
  (luis:Persona {nombre: 'Luis'}),
  (maria:Persona {nombre: 'María'}),
  (pedro:Persona {nombre: 'Pedro'}),

  (ml:Proyecto {nombre: 'Machine Learning'}),
  (datos:Proyecto {nombre: 'Datos Abiertos'}),
  (ia:Proyecto {nombre: 'IA para Gobierno'}),

  (ana)-[:COLABORA_EN]->(ml),
  (luis)-[:COLABORA_EN]->(ml),
  (luis)-[:COLABORA_EN]->(datos),
  (maria)-[:COLABORA_EN]->(datos),
  (maria)-[:COLABORA_EN]->(ia),
  (pedro)-[:COLABORA_EN]->(ia),

  (ana)-[:CONOCE]->(maria),
  (pedro)-[:CONOCE]->(luis);
```

### Entender la sintaxis

Un **nodo** se escribe entre paréntesis:

```cypher
(ana:Persona {nombre: 'Ana'})
```

- `ana`: variable utilizada dentro de la consulta.
- `Persona`: etiqueta del nodo.
- `nombre`: propiedad del nodo.
- `'Ana'`: valor de esa propiedad.

Una **relación** se representa con corchetes y flechas:

```cypher
(ana)-[:COLABORA_EN]->(ml)
```

Esto representa que Ana colabora en el proyecto Machine Learning.

> **Importante:** volver a ejecutar `CREATE` agregará otro conjunto de nodos y relaciones. Para esta práctica, ejecuta la creación solamente una vez.

## 6. Visualizar el grafo

Ejecuta:

```cypher
MATCH (a)-[r]->(b)
RETURN a, r, b;
```

Selecciona la vista **Graph** en Neo4j Browser. Podrás explorar los nodos y sus conexiones de forma interactiva.

- `MATCH` busca patrones dentro del grafo.
- `RETURN` especifica qué elementos queremos ver.
- `(a)-[r]->(b)` busca una relación dirigida entre dos nodos.

## 7. Consultas sencillas con Cypher

### ¿Quiénes participan en Machine Learning?

```cypher
MATCH (p:Persona)-[:COLABORA_EN]->(proyecto:Proyecto)
WHERE proyecto.nombre = 'Machine Learning'
RETURN p.nombre;
```

### ¿En qué proyectos participa Luis?

```cypher
MATCH (p:Persona)-[:COLABORA_EN]->(proyecto:Proyecto)
WHERE p.nombre = 'Luis'
RETURN proyecto.nombre;
```

### ¿Cuántas personas colaboran en cada proyecto?

```cypher
MATCH (p:Persona)-[:COLABORA_EN]->(proyecto:Proyecto)
RETURN
  proyecto.nombre AS proyecto,
  count(p) AS participantes
ORDER BY participantes DESC;
```

### ¿Qué parejas de personas colaboran en un mismo proyecto?

```cypher
MATCH (p1:Persona)-[:COLABORA_EN]->(proyecto:Proyecto)<-[:COLABORA_EN]-(p2:Persona)
WHERE p1.nombre < p2.nombre
RETURN
  p1.nombre AS persona_1,
  p2.nombre AS persona_2,
  proyecto.nombre AS proyecto;
```

En este ejemplo, la condición `p1.nombre < p2.nombre` evita mostrar cada pareja dos veces, suponiendo que los nombres son únicos.

En una base relacional, para responder estas preguntas probablemente trabajaríamos con tablas como `personas`, `proyectos` y `colaboraciones`, utilizando operaciones `JOIN`. En Neo4j consultamos directamente los patrones de relaciones.

## 8. Comprobar que los datos persisten

Detén Neo4j:

```bash
docker compose stop neo4j
```

Vuelve a iniciarlo:

```bash
docker compose start neo4j
```

Cuando esté listo, regresa a Neo4j Browser y ejecuta:

```cypher
MATCH (n)
RETURN count(n) AS total_nodos;
```

Si ejecutaste `CREATE` una sola vez, deberías obtener **7 nodos**.

También puedes eliminar los contenedores del proyecto y recrear el servicio:

```bash
docker compose down
docker compose up -d neo4j
```

Los datos permanecen porque el volumen `neo4j_data` sigue existiendo.

> **Cuidado:** `docker compose down -v` elimina también los volúmenes administrados por el proyecto, incluido el de Neo4j. No lo ejecutes si necesitas conservar los datos. Si hay otros servicios con volúmenes en el mismo `compose.yaml`, también podrían verse afectados.

## 9. ¿Qué aprendimos?

En esta práctica utilizamos Docker para ejecutar una base de datos completa sin instalar Neo4j directamente en nuestro sistema operativo.

- **Imagen:** contiene Neo4j y las instrucciones necesarias para ejecutarlo.
- **Contenedor:** ejecuta el servidor de la base de datos.
- **Servicio de Compose:** define cómo construir, configurar y ejecutar Neo4j.
- **Volumen:** permite conservar los datos independientemente del ciclo de vida de los contenedores.

Nuestro Dockerfile es deliberadamente pequeño, pero puede servir como punto de partida para personalizar una imagen de Neo4j sin incorporar los datos de la base dentro de la imagen.

## Referencias

- [Neo4j: introducción a Docker](https://neo4j.com/docs/operations-manual/current/docker/introduction/)
- [Neo4j: Docker Compose](https://neo4j.com/docs/operations-manual/current/docker/docker-compose-standalone/)
- [Neo4j: volúmenes y persistencia](https://neo4j.com/docs/operations-manual/current/docker/mounting-volumes/)
- [Cypher Manual](https://neo4j.com/docs/cypher-manual/current/)
