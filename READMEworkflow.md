# Documentación del Código

## Descripción
Este código implementa un flujo usando Prefect en Python para obtener datos JSON de una API de tragos y procesarlos para mostrar información sobre un trago aleatorio. El código utiliza la biblioteca `requests` para hacer solicitudes HTTP a la API.

## Estructura del Código
El código está estructurado en dos partes principales: la definición de clases y funciones, y la creación y ejecución del flujo Prefect.

### Clases
- `colores`: Esta clase define una serie de códigos de escape ANSI para dar formato al texto en la consola con colores y estilos.

- `Drink`: Esta clase representa un trago y tiene atributos como nombre, categoría, indicador alcohólico, instrucciones y lista de ingredientes y medidas.

### Funciones
- `obtener_json(url)`: Esta función es una tarea de Prefect que hace una solicitud HTTP GET a una URL dada y devuelve los datos JSON obtenidos. Si hay un error durante la solicitud, imprime un mensaje de error y devuelve `None`.

- `procesarData(data)`: Esta función es otra tarea de Prefect que procesa los datos JSON obtenidos por la tarea anterior. Crea una instancia de la clase `Drink` con los datos del trago y formatea un mensaje para imprimir en la consola con información sobre el trago.

### Flujo Prefect
El flujo Prefect se crea y ejecuta dentro de un bloque `with Flow`. El flujo consta de dos tareas: `obtener_json` y `procesarData`. Estas tareas están conectadas en secuencia, lo que significa que `procesarData` se ejecutará después de que `obtener_json` haya completado su ejecución con éxito.

## Ejecución
Para ejecutar el código, simplemente ejecuta el script en un entorno de Python que tenga instaladas las dependencias necesarias. El flujo se ejecutará y mostrará información sobre un trago aleatorio en la consola.

Recuerda tener una conexión a internet activa para poder obtener datos de la API de cocteles.


