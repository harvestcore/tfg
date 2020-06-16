# Descripción de los módulos implementados

En este documento se definen los diferentes módulos que se han desarrollado. Además se contextualizan los diferentes conceptos relacionados a cada uno de ellos. Los módulos son los siguientes:



## Almacenamiento

### MongoEngine

Esta clase es la que nos permite conectarnos al servidor de MongoDB y realizar todas aquellas operaciones que deseemos. Se ha desarrollado como un singleton para que solo haya una instancia activa al mismo tiempo.

Cada instancia de MongoClient que se crea tiene una *pool* de conexiones, que abre y cierra sockets bajo demanda para manejar todas las operaciones que se realicen de forma simultánea. Por este motivo es contraproducente crear una instancia de MongoClient cada vez que se quiera realizar una operación. Por defecto el tamaño de esta *pool* es de 100, pero podría incrementarse si fuera necesario.

Los métodos implementados son los siguientes:

- Creación del cliente.

- Borrado de bases de datos y de colecciones. Usados principalmente en los tests unitarios.

- Asignación de base de datos y colección actual. Usados para seleccionar la base de datos necesaria para cada cliente, y la colección donde realizar operaciones.

- Datos estadísticos. Se extrae del cliente de MongoDB y se devuelve en un diccionario con la siguiente forma:

  ```python
  {
      "is_up": bool,
      "data_usage": list,
  	"info": dict || str
  }
  ```

  - is_up: Indica el estado del servicio, true si se encuentra funcionando correctamente, false en caso contrario.
  - data: Información de uso de datos de las bases de datos almacenadas.
  - info: Información adicional del cliente.



### Item

Clase base de la que heredan todas las clases que necesitan algún tipo de almacenamiento de datos. Sus datos miembro son:

- *table_name*: Nombre de la tabla (o colección) donde se van a almacenar los datos.

- *table_schema*: Esquema de la tabla equivalente a la proyección de MongoDB. Es un diccionario compuesto por claves (nombres de los datos que va a almacenar la tabla) y por un valor 1 ó 0. Todas las claves que aparezcan en este diccionario serán claves válidas para almacenar en la tabla. Los valores indican lo siguiente:

  - 1: El dato se devuelve al hacer una consulta.
  - 0: El dato no se devuelve al hacer una consulta.

  Un ejemplo de uso sería:

  ```python
  table_schema = {
      'domain': 1,
      'db_name': 1
  }
  ```

  Al realizar consultas  se puede sobreescribir este esquema, para obtener únicamente los datos deseados.

- *data*: Diccionario donde se almacenan los datos de los objetos que se creen de este tipo o que se obtengan al hacer una consulta.



Para el diseño y desarrollo de esta clase se ha intentado abstraer y simplificar al máximo las funcionalidades de esta, para que se pueda adaptar a cualquier tipo de uso. No se han hecho uso de todas las funciones que ofrece PyMongo en cuanto a manejo de datos en colecciones. Aún así los métodos son los mínimos para que se pueda cualquier tipo de operación básica. Los métodos implementados en la clase *Item* son los siguientes:

- *cursor*: Hace uso del nombre de la tabla para obtener el cursor a ella y poder realizar todas las operaciones necesarias.
- *find(criteria, projection)*: Devuelve todos los elementos (sólo los parámetros indicados en la proyección) que cumplan los criterios de búsqueda.
- *insert(data)*: Inserta un elemento o lista de elementos en la colección. También agrega dos claves adicionales a éste que son:
  - *enabled*: Por defecto a true. Indica si el elemento está activo o no.
  - *deleted*: Por defecto a false. Indica si el elemento ha sido borrado o no.
- *update(criteria, data)*: Actualiza todos los elementos que cumplan con el criterio. *Data* es un diccionario con las claves y valores a actualizar.
- *remove(criteria, force)*: Elimina los elementos que cumplan con el criterio. Por defecto el parámetro *force* tiene valor *true*, lo que elimina completamente los elementos. En el caso de asignarle un valor *false* en lugar de eliminar los elementos los modifica, cambiando sus propiedades *enabled* a *false* y *deleted* a *true*.



Con esta implementación cualquier clase que se quiera que tenga la capacidad de almacenar datos solo tendrá que heredar de esta clase. Podrá sobreescribir aquellos métodos a los que quiera agregar más funcionalidad y podrá también implementar nuevos métodos, ya que tiene acceso al cursor de MongoClient para realizar cualquier tipo de operación permitida.





## Servicios

En cuanto a los servicios que se han desarrollado a partir de clases que heredan de *Item*, la estructura general de todos es la siguiente:

> Suponemos que el servicio *service* permite hacer operaciones con objetos de tipo Service.

- *GET /api/service/<name>*: Devuelve los datos asociados a un objeto Service.
- *POST /api/service*: Crea un objeto de tipo Service.
- *PUT /api/service*: Modifica un objeto de tipo Service.
- *DELETE /api/service*: Elimina un objeto de tipo Service.
- *POST /api/service/query*: Permite hacer consultas más elaboradas haciendo uso del criterio de búsqueda y de la proyección de MongoDB. Los objetos obtenidos se devuelven en forma de diccionario (en el caso de un sólo resultado) o de lista de diccionarios (más de un resultado).



Para simplificar el código en los servicios he creado algunas funciones auxiliares:

- *response_by_success*: Devuelve un mensaje predeterminado y un código en función del resultado de la operación que se haya procesado.
- *response_with_message*: Devuelve un mensaje y código personalizados.
- *validate_or_abort*: Valida los datos de entrada del endpoint en función del esquema que se quiera validar.
- *parse_data*: Devuelve los datos que se le pasan con la forma del esquema que se quiera. Tiene en cuenta si es un solo dato o un conjunto.



Por otro lado, se han creado diferentes esquemas con *Marshmallow* para validar todos los datos que se manejan en los servicios. De este modo se tiene control absoluto del tipo de dato que se esté manejando en cada momento. En el momento de recibir una petición los datos se cotejan con el esquema que se use en el endpoint y se asegura que los datos son los esperados, en caso contrario se rechaza la petición, para ello se hace uso de la función anterior *validate_or_abort*. En cuanto a la salida de datos se usa *parse_data* para asegurar que los datos devueltos tenga la estructura esperada.



## Autenticación

Utilizado para sólo permitir el uso de la API a los usuarios registrados. Esta autenticación se hace mediante JWT (JSON Web Token).

Para la creación de esta clase se ha partido de la clase *Item*, definiendo una nueva clase *Login* con los siguientes datos miembro:

- *table_name*: login
- *table_schema*: (Por defecto todos los valores a 1).
  - *token*: JWT del usuario que tenga acceso actualmente al backend.
  - *username*: Nombre de usuario.
  - *exp*: Fecha y hora a la que expira el acceso.
  - *login_time*: Fecha y hora a la que el usuario realizó el acceso.
  - *public_id*: UUID que identifica al usuario.



Para controlar los accesos que puedan quedar obsoletos o en los que no se haya realizado un *logout* correcto, cada vez que se instancia la clase se comprueba si hay tokens con estas características y se eliminan, evitando así una acumulación innecesaria de tokens sin usar.

Los métodos que se han desarrollado han sido los siguientes:

- *login(auth)*: En este método se realiza todo el proceso del login. Se parte de los datos de autenticación, compuestos por un usuario y una contraseña y se comprueba si tal usuario existe. Se verifica que la contraseña sea la correcta y en caso correcto se procede a la creación del token. Tanto como si el usuario no estaba logueado previamente como si ya lo estaba, se generan todos los datos asociados nuevamente, y se insertan o actualizan. En el token JWT se codifica el *public_id* y la fecha y hora de expiración, *exp*. Si el proceso ha sido correcto se devolverá el token creado.
- *logout(username)*: Desloguea al usuario denotado por *username*. Verifica que existe el usuario y borra cualquier tipo de información asociada de eśte en la colección actual.
- *token_access(token)*: Decodifica el token y devuelve al usuario logueado que tenga tal *public_id*.
- *get_username(token)*: Devuelve el nombre del usuario asociado al token.



Una vez desarrollada la clase que permite accesos de usuarios se ha desarrollado el servicio. Todas las rutas del backend, salvo *GET /api/login* y *GET /api/heartbeat* están protegidas con esta autenticación. Para ello se ha creado un decorador que comprueba el token de acceso cada vez que se quiere acceder a un endpoint. Es el siguiente:

- *token_required*: Obtiene el token de la cabecera *x-access-token*, comprueba si es válido y permite el acceso o no al endpoint. En caso de no ser válido se devuelve un mensaje de error y un código de error 401.



El servicio de login cuenta con dos endpoints, los cuales son:

- *GET /api/login*: Loguea al usuario, para ello toma los datos de acceso de la cabecera *Basic auth* y devuelve o no el token asociado al usuario.
- *GET /api/logout*: Desloguea al usuario que previamente debe estar logueado.





## Clientes

Clase que se encarga del manejo de los *customers* o clientes del backend. Todas las operaciones relacionadas con clientes así como los datos asociados a ellos se almacenan en la base de datos que se define en la variable de entorno *BASE_DATABASE*.

Los datos miembro de esta clase son:

- *table_name*: customers
- *table_schema*: (Por defecto todos los valores a 1).
  - *domain*: Subdominio al que hace referencia este cliente.
  - *db_name*: Nombre de la base de datos donde se almacenarán todos sus datos.



Los métodos que implementa esta clase son:

- *is_customer(customer)*: Comprueba si el customer existe. En caso de existir se devuelve si está activo o no.
- *set_customer(customer)*: Asigna el customer al que se le van a hacer consultas de base de datos. Esto es: se consulta el cliente en *BASE_DATABASE* y se obtiene su *db_name*, a continuación se asigna este nombre de colección como la base de datos a utilizar, haciendo uso del método *set_collection_name* de *MongoEngine*.
- *insert*: Se ha sobreescrito este método de *Item* para realizar comprobaciones previa inserción de nuevos clientes.
- *find*: Se ha sobreescrito para asegurar que las operaciones se hacen sobre *BASE_DATABASE*.
- *update*: Se ha sobreescrito para asegurar que las operaciones se hacen sobre *BASE_DATABASE*.
- *remove*: Se ha sobreescrito para asegurar que las operaciones se hacen sobre *BASE_DATABASE*.



Los endpoints desarrollados tienen la forma que se indica [aquí](#servicios), pero no se han implementado todos ellos, sólo los siguientes:

- *POST /api/customer*
- *PUT /api/customer*
- *DELETE /api/customer*
- *POST /api/customer/query*



Por otro lado, para controlar el cliente que se debe utilizar en cada petición se ha creado una función para este cometido. Obtiene el subdominio del host de la petición y comprueba si se trata de un cliente válido; en caso afirmativo se asigna como cliente para esa petición y en caso negativo se aborta la petición con un código 404.





## Usuarios

Esta es la clase encargada del manejo de los usuarios y hereda de *Item*. Trabaja junto con la clase *Login* para permitir el acceso a la API. Los datos miembro de esta clase son:

- *table_name*: users
- *table_schema*: (Por defecto todos los valores a 1).
  - *type*: Tipo del usuario, puede ser *admin* o *regular*.
  - *first_name*: Nombre del usuario.
  - *last_name*: Apellido/s del usuario.
  - *username*: Nickname del usuario.
  - *email*: Email del usuario.
  - *password*: Contraseña del usuario.
  - *public_id*: UUID del usuario.



Se han sobreescrito los métodos de inserción y actualización de datos para tener en cuenta las restricciones de tipo de usuario, para la generación del UUID y para el cifrado de la contraseña. Este cifrado se hace con Fernet, el cual es de tipo simétrico.

En cuanto al servicio, este tiene está estructurado de la misma forma que se especifica [aquí](#servicios), siendo los endpoints:

- *GET /api/user/<username>*
- *POST /api/user*
- *PUT /api/user*
- *DELETE /api/user*
- *POST /api/user/query*





## Despliegues

Este módulo es el encargado de realizar los despliegues de los servicios mediante contenedores Docker. Para llevar a cabo esto se conecta a un servidor de Docker y contiene los métodos necesarios para ejecutar contenedores, imágenes y operaciones en ambos.

Actualmente no permite realizar algunas funciones, como son el manejo de redes, nodos, o volúmenes. Una futura mejora o ampliación del módulo podría incluir estas u otras nuevas funcionalidades. Por el momento no eran necesarias y se han priorizado los contenedores y las imágenes.

Por otro lado también permite obtener información del estado del cliente, del uso de almacenamiento e información general.

- En este módulo se entiende por **cliente** al conector que se crea en el sistema para comunicarnos con el daemon de Docker.

- Un **objeto** puede ser una imagen o un contenedor.

- Por **operación** se entiende toda aquella tarea que se puede ejecutar en un contenedor o en una imagen.

  Las operaciones constan de nombre, datos y, en ocasiones, de un objeto concreto:

  - *operation*: Nombre de la operación.
  - *data*: Datos necesarios para ejecutar la operación.
  - *object*: Objeto al que se dirige la operación.



Para manejar esto se ha creado la clase *DockerEngine*, la cual se conecta al daemon de Docker e implementa los métodos necesarios para realizar las funciones anterior mencionadas. Concretamente estas son:

- *run_container_operation(operation, data)*: Ejecuta una operación en todos los contenedor.
- *run_image_operation(operation, data)*: Ejecuta una operación en todas las imágenes.
- *run_operation_in_object(object, operation, data)*: Ejecuta una operación en todos los contenedor.
- *get_container_by_id(name)*: Ejecuta una operación en todos los contenedor.
- *get_image_by_name(container_id)*: Ejecuta una operación en todos los contenedor.



Los endpoints desarrollados son los siguientes:

- *POST /api/deploy/container*: Operaciones en todos los contenedores.
- *POST /api/deploy/container/single*: Operaciones en un único contenedor.
- *POST /api/deploy/image*: Operaciones en todas las imágenes.
- *POST /api/deploy/image/single*: Operaciones en una única imagen.

La información sobre el estado de este módulo se devuelve con la misma estructura que se utiliza en [MongoEngine](#mongoengine):

```python
{
    "is_up": boolean,
    "data_usage": list,
	"info": dict || string
}
```



Puede ocurrir que el backend se esté ejecutando en un contenedor Docker, por lo que intentar conectarse al daemon no sería posible en ese caso. Cuando se ejecuta el backend éste comprueba internamente en qué entorno se esta ejecutando y la variable que almacena la localización del daemon o servidor. Estas comprobaciones determinarán si éste módulo se encontrará activo o no.





## Aprovisionamiento

Es el encargado de aprovisionar sistemas mediante el uso de Ansible y se centra exclusivamente en la ejecución de playbooks y en la gestión y almacenamiento de grupos de hosts y playbooks.

- Un **grupo de hosts** es aquella máquina o grupo de máquinas que se quiere aprovisionar.
- Un **playbook** es el conjunto de ordenes, comandos y tareas que se quiere que se ejecuten en un grupo de hosts.

Tanto los hosts como los playbooks se pueden almacenar en base de datos si se desea y por tanto se han desarrollado las clases *Hosts* y *Playbook*.



#### Hosts

Clase que hereda de *Item* cuyos datos miembro son:

- *table_name*: hosts
- *table_schema*: (Por defecto todos los valores a 1).
  - *name*: Nombre del grupo de hosts.
  - *ips*: Lista de direcciones IP que componen el grupo de hosts.

Comparte los mismos endpoints que se indican [aquí](#servicios), siendo estos:

- *GET /api/provision/hosts/<name>*
- *POST /api/provision/hosts*
- *PUT /api/provision/hosts*
- *DELETE /api/provision/hosts*
- *POST /api/provision/hosts/query*



#### Playbook

Clase que hereda de *Item* cuyos datos miembro son:

- *table_name*: playbooks
- *table_schema*: (Por defecto todos los valores a 1).
  - *name*: Nombre del playbook.
  - *playbook*: Contenido del playbook codificado como JSON.

Comparte los mismos endpoints que se indican [aquí](#servicios), siendo estos:

- *GET /api/provision/playbooks/<name>*
- *POST /api/provision/playbooks*
- *PUT /api/provision/playbooks*
- *DELETE /api/provision/playbooks*
- *POST /api/provision/playbooks/query



Para la ejecución de los playbooks se ha desarrollado la clase *AnsibleEngine*, la cual implementa un método para este cometido, es:

- *run_playbook(hosts, playbook, passwords)*

Este método toma como entrada el grupo de hosts a los que se le va a ejecutar el playbook, el playbook en cuestión y un diccionario con las contraseñas para acceder a las máquinas. La librería de Ansible usada requiere que los hosts se pasen como un archivo de texto plano, por lo que se ha desarrollado una función auxiliar que crea un fichero cuando se ejecuta un playbook. El directorio donde se guardan estos archivos puede configurarse mediante una variable de entorno.



El endpoint creado es el siguiente:

- *POST /api/provision*





## Máquinas

Para el almacenamiento y gestión de máquinas se ha creado la clase *Machine*, la cual también hereda de *Item*. Sus datos miembro son:

- *table_name*: machines
- *table_schema*: (Por defecto todos los valores a 1).
  - *name*: Nombre de la máquina.
  - *description*: Descripción breve de la máquina.
  - *type*: Tipo de máquina, puede ser *local* o *remote*.
  - *ipv4*: Dirección IPv4 de la máquina.
  - *ipv6*: Dirección IPv6 de la máquina.
  - *mac*: MAC del adaptador de red que conecta la máquina a la red.
  - *broadcast*: Dirección broadcast de la red a la que está conectada la máquina.
  - *netmask*: Máscara de red.
  - *network*: Red a la que está conectada la máquina.



En el caso de las máquinas todas las direcciones IP que se manejan deben ser validadas, por lo que se ha creado un método auxiliar para realizar esta función. Además se han sobreescrito los métodos de inserción y actualización para realizar esta validación.

El servicio tiene la misma estructura que la explicada [aquí](#servicios) y sus endpoints son:

- *GET /api/machine/<name>*
- *POST /api/machine*
- *PUT /api/machine*
- *DELETE /api/machine*
- *POST /api/machine/query*





## Estado del backend y *heartbeat*

Para consultar el estado del backend se han creado dos endpoints. El primero ofrece una información más detallada de los dos servicios más importantes y el segundo ofrece sólo el estado general del backend. Son:

- *GET /api/status*: Endpoint autenticado que devuelve un diccionario con los estados de MongoDB y Docker, con la forma indicada anteriormente. Los usuarios administradores obtienen más información en el caso de Mongo. La estructura devuelta es:

  ```python
  {
      'mongo': {
          'is_up': bool,
          'data_usage': list,
          'info': dict || str
      },
      'docker': {
          'is_up': bool,
          'data_usage': list,
          'info': dict || str
      }
  }
  ```

  En el caso que Docker no se encuentre funcionando correctamente o se encuentre desactivado el estado devuelto es:

  ```python
  {
      'status': bool,
      'disabled': bool,
      'msg': str
  }
  ```

- *GET /api/heartbeat*: Endpoint no autenticado que devuelve el estado simplificado. Este endpoint puede ser usado para comprobar que el backend se encuentra activo de forma manual o por ejemplo por la funcionalidad *Heartbeat* que incorpora Docker para conocer el estado de salud de los contenedores.

  ```python
  {
      'ok': bool
  }
  ```

  



## CLI e inicialización de la BD

Se ha desarrollado un CLI interactivo que permite realizar operaciones básicas con los clientes y usuarios mediante una terminal de comandos. Para ello hace uso de las clases y métodos anterior explicados. Estas operaciones son:

- Crear, activar y desactivar clientes.
- Agregar usuarios a un cliente.



Además se ha creado un pequeño script que permite inicializar la base de datos, insertando un usuario administrador por defecto.





## Frontend

