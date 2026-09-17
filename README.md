![](imgs/egytp_logo.jpg)

# Introducción a la programación para políticas públicas

**Por Elena Villalobos Nolasco**

- Otoño 2026.

## Generalidades de la clase: 

- Se impartirá de manera presencial en Mixcoac.
- Horario: 18:30 a 21:00.
    - Salón 2.5.
	- Las clases se repartirán entre teóría y práctica, pero será una clase principalmente práctica.
- Todo el contenido del curso se mostrará en este repositorio.
- Las tareas se entregarán y calificarán en **Canvas** pero se desarrollarán en el repositorio.
- Necesitas una computadora para la clase, no tablet. 

## Temario general

1. Introducción a la programación e infraestructura
2. SSH
3. Bash
4. Git/Github/Gitlab
5. Análisis de datos en CLI
6. Introducción a bases de datos 
7. Gestión para Python
8. Variables de entorno
9. Interacción con servidores: TMUX y editores de texto
10. Quarto
11. CI/CD
12. Docker
13. APIs 


## Políticas de la clase

- Enfoque muy práctico.
- Suposición de que quieres aprender:
	- Asistencia importante.
	- Si necesitas faltar avisar con anticipación y hacerte responsable de revisar el material visto.
	- **NO** se grabarán las clases.

- **NO** se permite el uso de teléfonos durante la clase.

- **NO SE CALIFICARÁN TAREAS EXTEMPORÁNEAS**


### Política de uso de modelos de lenguaje (LLMs) en la clase

Con el objetivo de fomentar habilidades de resolución de problemas, pensamiento crítico y lectura técnica, 
el uso de modelos de lenguaje (LLMs) como ChatGPT, Claude, Gemini, Copilot, entre otros, estará 
regulado bajo las siguientes pautas:

1. **NO** esta permitido durante el horario de clase.

2. Uso para propósitos de la clase fuera del horario de clase:
    - Antes de ir al uso de LLMs considera lo siguiente: 
        - Revisar documentación oficial.
        - Consultar recursos previamente compartidos (ej. notas del curso, cheatsheets, manuales, foros recomendados).
        - Si es para resolver un error de programación:
            - Revisar sintaxis detalladamente. 
            - **Leer detalladamente los errores o resultados que arrojen los programas.**
        - Hacer preguntas en clase o discutir con compañeros.

    - En caso de utilizar LLMs para resolver preguntas, errores o apoyo con tareas, el estudiante debe de escribir 
    y entregar el prompt exacto utilizado. 
        - El prompt debe ser planteado de manera crítica y una vez realizado el paso anterior.
        - Se deben evitar prompts genéricos del tipo “hazme el código de…” o “resuélveme esto”, y preferir en su lugar:
            - “¿Por qué este error aparece si estoy usando tal librería?”
            - “¿Cuál es la diferencia entre estos dos métodos?”
            - “¿Qué significa este mensaje en la documentación de pandas?”

3. Documentación del uso:

    - En cualquier entrega (scripts, notebooks, reportes) donde se haya consultado un LLM:
    - Se debe incluir al final una sección titulada “Consultas realizadas con LLMs” que contenga:
    - El prompt exacto usado.
    - Un resumen breve de la respuesta y cómo fue utilizada (o descartada)
    - Ejemplo: 
        - **Prompt:** Estoy limpiando nombres para un proceso de record linkage en Python, y ya normalicé mayúsculas y tildes. 
        Estoy utilizando `SequenceMatcher` para comparar nombres, pero me está fallando cuando hay diferencias menores como 
        un segundo nombre adicional. ¿Hay una mejor métrica que considere esto y que esté disponible en alguna librería estándar?
        - **Respuesta:** El LLM sugirió que `SequenceMatcher` no es la mejor opción para comparar nombres con estructuras distintas
         y que en estos casos es mejor usar `Jaro-Winkler` o `SoftTF-IDF`, ya que son más tolerantes a errores de inserción y 
         transposición. También sugirió usar `jellyfish` o `textdistance` como librerías de Python que implementan estas métricas.
        - **Uso:** Probé con `jellyfish.jaro_winkler_similarity()` y obtuve mejores resultados en pares con nombres compuestos.


4. Evaluación y ética: 
    - El uso no transparente de LLMs será considerado una falta a la honestidad académica.
    - El propósito de esta política no es prohibir herramientas, sino fomentar su uso ético, consciente y crítico.

## Evaluación

| Concepto                  | Porcentaje
| ------------------------  | ----------
| Tareas                    |  60
| Evaluación intermedia     |  20 
| Evaluación final          |  20


## Repositorio

- Los archivos para el curso están la carpeta de `materiales`.
- La estructura de este repo es parte de lo que se enseña en este curso.

## Para conectarte a bastión:

- Sí es tu primera vez en conectarte, tienes que llenar el siguiente formulario: https://docs.google.com/forms/d/e/1FAIpQLSfRTXU4YgjlSsyNYCVw-ZYWuNWnvVlZ4oUV-CivO6i-AlLvEg/viewform?usp=preview


```{.sh}
ssh -i ~/.ssh/id_rsa <tu_usuario>@bastion.egobiernoytp.io -o ServerAliveInterval=60
```

## Para puentes

```{.sh}
ssh -NL localhost:16000:localhost:16000 usuario@bastion.egobiernoytp.io
```

## Contacto
- villalobos_elena@tec.mx

## Office-hours
- A petición a mi correo 


### Referencias 
- Jeroen Janssens (2021) Data Science at the Command Line.
- Reginald Boman & Aingaran Balan Raman, Computational Thinking with Python: An Introductory Approach to Python Programming, Kendall Hunt Publishing, 2021.
- Downey, A. B., hink python: How to think like a computer scientist , 2a. edición, O’Reilly Media, 2015.
- Wickham, H., and Grolemund, G. and Çetinkaya-Rundel, M. , R for Data Science: Import, Tidy, Transform, Visualize, and Model Data, 2a. Edición, O'Reilly Media, 2023.
- Introducción a la programación (2020) Adolfo De Unánue.
