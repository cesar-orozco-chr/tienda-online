# **Tienda Online**
## **Trabajo de la asignatura de Informática I.**

## **Realizado por**:

- Camilo Andres Nuñez Zabaleta - 20221099022
- Jorge Hernan Moreno Linares - 20221099021
- Jorge Luis Roncancio Turriago - 20221099019
- Cesar Augusto Orozco Manotas - 20221099023
- Carlos Enrique Hernandez Blanco - 20221099030


## **Introduccion**

>El siguente proyecto es una simulacion de una tienda online, se ve limitada a la interaccion entre clientes, productos y compras por lo cual para funcionar realiza el consumo de una serie de servicios tipo **REST** que realizan todas las acciones asociadas al CRUD de la base de datos, estos servicios estan cada uno en contenedores de Docker al igual que la base de datos (segun la premisa del ejercicio). La organizacion y ejecucion del proyecto se realizo utilizando **Scrum** simplificando un poco por temas de tiempo pero de igualmanera realizando el planning correspondiente y sus dailys o seguimientos respectivos de las tareas planeadas por el equipo, en el siguiente enlace se puede ver la ejecucion de SCRUM: https://trello.com/b/754aWgjQ/informaticai

>La tienda esta compuesta por un backend codificado en python, separando la logica de negocio utilizando una estructura de servicios que utilizan modelos para la representacion de las entidades de la base de datos, conexiones estandar que permiten el acceso para realizar el CURD de la misma, configuraciones de archivos "Dockerfile" que definen la imagen y el codigo a implementar en el contenedor, utilizacion de archivos "requirements.txt" para la resolucion de dependencias y finalmente el uso de pruebas unitarias que verifican las funcionalidades codificadas.

>Adicionalmente cuenta con una capa visual que hace uso del backend anterior, renderizando templates de html para dar una interaccion del proyecto mucho mas amigable con el usuario, sin dejar de lado en ningun momento las premisas de que el proyecto debia exponer a travez de docker y la configuracion de un archivo "nginx.conf" los servicios requeridos para hacer el CRUD de la tienda online.

### **Las siguentes acciones se pueden realizar en la tienda online:**
1. Crear
    - Clientes
    - Productos
    - Añadir al carro de compras
2. Consultar
    - Clientes
    - Productos
    - Carro de compras
    - Compras
3. Modificar
    - Clientes
    - Productos
    - Carro de compras
    - Compras
4. Eliminar
    - Clientes
    - Productos
    - Carro de compras

### **Tener en cuenta:**
- Se debe tener instalado Docker para la ejecucion de los contenedores necesarios.
- Se recomienda tener instalado Git Bash para realizar la ejecucion del instructivo.
- Ingresar al directorio raiz "tienda-online"
- Utilizar el siguente comando para verificar que los contenedores de docker esten levantados:
```
docker-compose ps
```
- ejecutar en un git bash (recomendado) el archivo bash "start-proyect.sh"
- para detener la ejecucion, ejecutar el archivo "stop-proyect.sh"

### **Instrucciones para utilizar la tienda online**

1. Utilizar git bash para ejecutar el archivo "start-proyect.sh"
2. Abrir en el navegador una nueva ventana e ingresar "http://localhost:8080"
3. En la pantalla que se vizualiza se tiene un menu en la parte superior de la pantalla que contiene las funcionalidades a utilizar.
4. Para crear clientes se debe dar click en "Crear / Añadir" y seleccionar Clientes del menu desplegable
5. Ingresar el nombre y documento para luego guardar el cliente.
6. Si se desea crear mas clientes el formulario se limpia luego de la creacion exitosa.
7. Si se quiere seguir realizando creaciones pero de productos o de carros de compra, estan las opciones en el menu de la parte superior. Si se desea volver al menu principal se debe dar click en "TIENDA"
8. Cuanto se tengan los clientes, productos y carro de compras creado se puede proceder a consultar usando el menu de la barra superior.
9. En la seccion de consulta se puede ver la lista de clientes, lista de productos, consultar los productos en el carro de compras de un cliente o el historial de compras de un cliente.
10. Volviendo al menu principal usando el boton "TIENDA", se puede encontrar la seccion de modificar que muestra un menu desplegable con las ociones de modificacion disponibles.
11. Se puede modificar los datos de un cliente, los datos de un producto, los datos de un carro de compras o finalizar la compra de los productos que se encuentran en un carro de compras de un determinado cliente.
12. Volviendo al menu principal usando el boton "TIENDA", se puede encontrar la seccion de eliminar que muestra un menu desplegable con las ociones de modificacion disponibles.
13. Se pueden eliminar clientes, productos o carros de compra segun el id correspondiente.