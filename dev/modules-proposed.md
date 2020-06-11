# Descripción de los módulos propuestos

En este documento se definen los diferentes módulos que se proponen:



## Almacenamiento

Para facilitar el desarrollo de los diferentes módulos se propone desarrollar una base común que sirva como puente para realizar operaciones en las diferentes colecciones de la base de datos.

Esta podría llamarse *Item* e implementaría las cuatro operaciones básicas necesarias para manejar cualquier tipo de dato: crear, modificar, obtener y eliminar. Una vez implementados esos métodos básicos el resto de módulos que se desarrollen sólo tienen que sobreescribir las operaciones necesarias, para adecuarlas a cada uso concreto.

Por otro lado, para manejar el cliente de MongoDB se propone crear una clase, llamada MongoEngine, que permita realizar diferentes operationes en las coleciones y bases de datos. Además, podría obtenerse también algún tipo de estadisticos de este servicio.

Ambos módulos funcionarían conjuntamente para ofrecer un conector a la base de datos sencillo y capaz de adaptarse a cualquier tipo de uso.

Para la configuración de cada clase que pueda heredar de *Item*, se debería definir un nombre de la colección a usar por esa clase y además el esquema de la colección. Este esquema sería el conjunto de datos que se pueden almacenar en la colección.

En conclusión, se propone:

- Clase Item
- Clase MongoEngine



Finalmente, el *developer journey* a la hora de implementar cada clase sería el siguiente:

1. Creación de nueva clase, que herede de *Item*.
2. Definición del nombre de la colección y del esquema.
3. Redefinición de aquellos métodos de *Item* que requieran alguna modificación especial.
4. Creación de todos aquellos métodos que sean necesarios.





## Autenticación

Se propone un módulo que permita la autenticación de usuarios en el sistema. Este haría uso de JWT (JSON Web Token) para encriptar la información y se debería incluir en las cabeceras de las peticiones que se realicen al backend. La cabecera a usar podría ser: *x-access-token*.

En cada petición este token deberá ser decodificado, se comprobará al usuario al que pertenece y finalmente se permitirá el acceso o no.

Todos los endpoints del backend estarían protegidos por esta autenticación, salvo:

- *GET /api/login*
- *GET /api/heartbeat*



El servicio de autenticación a implementar debería implementar:

- *GET /api/login*
- *GET /api/logout*



*Developer journey*:

1. Creación de la clase *Login* del mismo modo que se especifica en el *developer journey* [aquí](#almacenamiento).
2. Creación del servicio *Login*.
3. Implementación del decorador usado para comprobar el token *x-access-token* que se encuentra en las cabeceras de la petición.





## Clientes

Se propone este módulo para diferenciar y manejar los diferentes clientes que podrían acceder al backend. Cada uno de estos clientes contaría con su propia base de datos, por lo que se debería administrar y controlar esos datos.

La clase *Customer* es la propuesta en este caso. Heredaría las funcionalidades de *Item* y las complementaría con la gestión de estos clientes. Para diferenciar un cliente de otro se propone que se acceda al backend por medio de un subdominio.



*Developer journey*:

1. Creación de la clase *Customer* del mismo modo que se especifica [aquí](#almacenamiento).
2. Implementación de los métodos necesarios para clasificar las peticiones por subdominio.





## Usuarios

Este módulo es el encargado de la gestión de los usuarios y sus funcionalidades serían las siguientes:

- Crear usuarios.
- Modificar usuarios.
- Obtener información de los usuarios.
- Eliminar usuarios.



Para satisfacer los requisitos del software se propone lo siguiente:

- Los datos a almacenar por usuario son: Identificador único, Tipo de usuario, Nombre, Apellidos, Email, Nombre de usuario, Contraseña.
- La contraseña se encriptaría con encriptado simétrico Fernet.
- Los tipos de usuario aceptados serían "admin" y "regular".
- El email será único.



Debido a que partimos del módulo Item, para desarrollar el módulo de usuarios solo es necesario heredar de éste y hacer algunas modificaciones. En cuanto al borrado y obtención de usuarios no sería necesario hacer ningún tipo de modificación. Por otro lado, en las operaciones de inserción y modificación sólo habría que añadir el código necesario para el encriptado de la contraseña y para la comprobación del tipo de usuario y del email único.



Este módulo contaría con los siguientes endpoints:

- *GET /api/user/:user* - Obtener la información de un usuario.
- *POST /api/user* - Crear un usuario.
- *PUT /api/user* - Modificar un usuario.
- *DELETE /api/user* - Eliminar un usuario.
- *POST /api/user/query* - Listar usuarios.



*Developer journey*:

1. Creación de la clase *User* del mismo modo que se especifica en el *developer journey* [aquí](#almacenamiento), siguiendo las restricciones anterior mencionadas.
2. Creación del servicio *User*.
3. Implementación de los endpoints especificados anteriormente.





## Despliegues

Éste módulo sería el encargado de realizar los despliegues de los servicios mediante contenedores Docker. Para llevar a cabo esto el módulo se conectaría a un servidor de Docker y contendría los métodos necesarios para ejecutar contenedores, imágenes y operaciones en ambos.

En el caso de los despliegues no es necesario el almacenamiento de datos de ningún tipo, por lo que tampoco sería necesario crear clases que hereden de *Item*. En cambio, se propone la creación de una clase, llamada *DockerEngine*, que permita conectarse al cliente de Docker e implemente los métodos necesarios para hacer las operaciones deseadas.

Estas serían:

- Ejecutar operaciones a todos los contenedores.
- Ejecutar operaciones en un contenedor en concreto.
- Ejecutar operaciones a todas las imágenes.
- Ejecutar operaciones en una imagen en concreto.



Las anteriores operaciones corresponderían con los siguientes endpoints:

- *POST /api/deploy/container*
- *POST /api/deploy/container/single*
- *POST /api/deploy/image*
- *POST /api/deploy/image/single*



Por otro lado, del mismo modo que se propone en el módulo de almacenamiento, podrían sacarse una serie de estadísticos de este servicio.



*Developer journey*:

1. Creación de la clase *DockerEngine*.
2. Implementación de los métodos anterior mencionados, haciendo uso del cliente de Docker.
3. Creación del servicio *Deploy*.
4. Implementación de los endpoints especificados anteriormente.



## Aprovisionamiento

Sería el encargado de aprovisionar sistemas mediante el uso de Ansible y se centraría exclusivamente en la ejecución de playbooks. Por el funcionamiento de Ansible, debería establecer una conexión SSH con los hosts indicados y ejecutaría las órdenes que se encuentran en el playbook.

En el caso de este módulo son necesarias dos clases extra, una para almacenar los playbooks y otra para almacenar los grupos de hosts donde se van a ejecutar esos playbooks. Las clases serían:

- *Hosts*
- *Playbooks*



Los endpoints que se proponen para manejar ambas clases son:

- *GET /api/provision/hosts/:name* - Obtener la información de un grupo de hosts.
- *POST /api/provision/hosts* - Crear un grupo de hosts.
- *PUT /api/provision/hosts* - Modificar un grupo de hosts.
- *DELETE /api/provision/hosts* - Eliminar un grupo de hosts.
- *POST /api/provision/hosts/query* - Listar grupos de hosts.



- *GET /api/provision/playbook/:name* - Obtener la información de un playbook.
- *POST /api/provision/playbook* - Crear un playbook.
- *PUT /api/provision/playbook* - Modificar un playbook.
- *DELETE /api/provision/playbook* - Eliminar un playbook.
- *POST /api/provision/playbook/query* - Listar playbooks.



Siguiendo los requisitos del software, las restricciones son:

- Se almacenará para cada playbook un identificador único, un nombre y el playbook en sí.
- Se almacenará para cada grupo de playbooks un identificador único, un nombre y el conjunto de direcciones IP asociadas.



*Developer journey* para estas clases:

- Creación de la clase *Hosts* y *Playbooks* del mismo modo que se especifica en el *developer journey* [aquí](#almacenamiento), siguiendo las restricciones anterior mencionadas.
- Creación del servicio *Provision* e implementación de los endpoints anteriores.



Por otro lado para ejecutar los playbooks se propone la creación de una clase *AnsibleEngine*, que sería la encargada de implementar aquellos métodos necesarios para ejecutar los playbooks. También se propone el siguiente endpoint:

- *POST /api/provision*



*Developer journey*:

- Creación de la clase *AnsibleEngine* e implementación de los métodos necesarios para ejecutar playbooks.
- Completar el servicio *Provision* con el anterior endpoint.





## Máquinas

Módulo encargado del almacenamiento y gestión de máquinas y dispositivos. Tendría estructura similar a las clases *Host* o *Playbook*, ya que heredaría las funcionalidades que ofrece la clase base *Item*.

Los endpoints propuestos para este módulo son:

- *GET /api/machine/:user* - Obtener la información de una máquina.
- *POST /api/machine* - Crear una máquina.
- *PUT /api/machine* - Modificar una máquina.
- *DELETE /api/machine* - Eliminar una máquina.
- *POST /api/machine/query* - Listar máquinas.



Requisitos del software:

- El sistema almacenará para cada máquina un identificador único, un nombre, una descripción, un tipo de máquina, dirección IPv4 e IPv4, dirección MAC, máscara de red, dirección broadcast y dirección de red.



*Developer journey*:

1. Creación de la clase *Machine* del mismo modo que se especifica en el *developer journey* [aquí](#almacenamiento), siguiendo las restricciones anterior mencionadas.
2. Creación del servicio *Machine*.
3. Implementación de los endpoints especificados anteriormente.





## Estado del backend y *heartbeat*

Para comprobar el estado del backend se propone la creación de un servicio que devuelva información asociada al modulo de despliegues y al de almacenamiento. Para ello se propone agregar métodos a las clases *MongoEngine* y *DockerEngine* que devuelvan esta información asociada.

El endpoint sería el siguiente:

- *GET /api/status*

Debido a que este endpoint devolvería información relevante éste deberia estar también protegido por la autenticación comentada en secciones anteriores.

Anexo a este estado se propone el siguiente endpoint:

- *GET /api/heartbeat*

En este caso solo devolvería si los diferentes módulos del backend se encuentran funcionando correctamente o no, y no sería necesario que estuviera autenticado. Este endpoint podría ser usado por Docker, en el caso de que el backend se ejecute en un contenedor de este tipo.



*Developer journey*:

- Ampliar las clases *MongoEngine* y *DockerEngine* con métodos para obtener estadísticos del funcionamiento de estos servicios.
- Crear el servicio *Status* e implementar los módulos anteriores.





## Variables de entorno

Para el funcionamiento del backend y el frontend sería necesaria la definición de variables de entorno que permitan configurar ciertos aspectos de estos. Serían:

- Hostname y puerto de MongoDB.
- Nombre de la base de datos a utilizar.
- Claves de encriptado para las contraseñas y los token de autenticación.
- Hostname de Docker.
- URL y puerto del backend.



*Developer journey*:

- Identificar todas las variables de entorno necesarias, definirlas y asignarles un valor por defecto.