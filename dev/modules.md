# Descripción de los módulos

En este documento se definen los diferentes módulos que se han propuesto y desarrollado. Además se contextualizan los diferentes conceptos relacionados a cada uno de ellos. Los módulos son los siguientes:

## Backend

### 1. Despliegues

Éste módulo es el encargado de realizar los despliegues de los servicios mediante contenedores Docker. Para llevar a cabo esto se conecta a un servidor de Docker y contiene los métodos necesarios para ejecutar contenedores, imágenes y operaciones en ambos.

Actualmente no permite realizar algunas funciones, como son el manejo de redes, nodos, o volúmenes. Una futura mejora o ampliación del módulo podría incluir estas u otras nuevas funcionalidades. Por el momento no eran necesarias y se han priorizado los contenedores y las imágenes.

Por otro lado también permite obtener información del estado del cliente, del uso de almacenamiento e información general.

Contextualización:

- En este módulo se entiende por **cliente** al conector que se crea en el sistema para comunicarnos con el daemon de Docker.

- Un **objeto** puede ser una imagen o un contenedor.

- Por **operación** se entiende toda aquella tarea que se puede ejecutar en un contenedor o en una imagen.

  Las operaciones constan de nombre, datos y, en ocasiones, de un objeto concreto:

  - *operation*: Nombre de la operación.
  - *data*: Datos necesarios para ejecutar la operación.
  - *object*: Objeto al que se dirige la operación.

  

### 2. Aprovisionamiento

Es el encargado de aprovisionar sistemas mediante el uso de Ansible y se centra exclusivamente en la ejecución de playbooks. Para ello establece una conexión ssh con los hosts indicados y ejecuta las órdenes que se encuentran en el playbook.

Contextualización:

- Un **host** es aquel equipo o máquina que se quiere aprovisionar.
- Un **playbook** es el conjunto de ordenes, comandos y tareas que se quiere que se ejecuten en el host.

Tanto los hosts como los playbooks se pueden almacenar en base de datos si se desea.



### 3. Almacén de datos

Este módulo está compuesto por una serie de submódulos para almacenar todos los datos necesarios en el sistema. Se ha desarrollado una base común a todos ellos, que permite que el desarrollo de submódulos se simplifique considerablemente, sólo teniendo que implementar las necesidades concretas de cada uno.

Los submódulos son:

- [*Customer*](modules/customer.md)
- [*Host*](modules/host.md)
- [*Login*](modules/login.md)
- [*Machine*](modules/machine.md)
- [*Playbook*](modules/playbook.md)
- [*User*](modules/user.md)

Y la base es:

- [*Item*](modules/item.md)



### 4. Autenticación

Utilizado para sólo permitir el uso de la API a los usuarios registrados. Esta autenticación se hace mediante JWT (JSON Web Token).



[Completar]