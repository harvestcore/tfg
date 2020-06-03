# Endpoints

## Status

#### GET /api/status

Devuelve el estado actual de los dos servicios principales del backend, MongoDB y Docker.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Respuesta:

| Parámetro | Key        | Tipo       | Descripción                                        |
| --------- | ---------- | ---------- | -------------------------------------------------- |
| mongo     |            | dict       |                                                    |
|           | is_up      | bool       | Si el servicio se encuentra activo o no.           |
|           | data_usage | list[dict] | Información de uso de datos de cada base de datos. |
|           | info       | string     | Información adicional del cliente de MongoDB.      |
| docker    |            | dict       |                                                    |
|           | is_up      | bool       | Si el servicio se encuentra activo o no.           |
|           | data_usage | dict       | Información de uso de las imágenes y contenedores. |
|           | info       | string     | Información adicional del cliente de Docker.       |

En caso de que el servicio de Docker no se encuentre activado o presenta errores, el estado de este en la respuesta anterior tiene la siguiente forma:

| Parámetro | Key      | Tipo   | Descripción                                   |
| --------- | -------- | ------ | --------------------------------------------- |
| docker    |          | dict   |                                               |
|           | status   | bool   | False. El servicio no funcina correctamente.  |
|           | disabled | bool   | Si el servicio se encuentra desactivado o no. |
|           | msg      | string | Información adicional.                        |





## Heartbeat

#### GET /api/heartbeat

Devuelve el estado actual de los dos servicios principales del backend de forma simplificada.

Respuesta:

| Parámetro | Tipo | Descripción                                                |
| --------- | ---- | ---------------------------------------------------------- |
| ok        | bool | Si los servicios del sistema funcionan correctamente o no. |





## Autenticación

#### GET /api/login

Loguea al usuario en el cliente.

Cabeceras necesarias:

| Nombre     | Opcional | Descripción                                   |
| ---------- | :------: | --------------------------------------------- |
| Basic Auth |   :x:    | Basic Auth compuesto por usuario y contraseña |

Respuesta:

| Parámetro | Tipo   | Descripción                                      |
| --------- | ------ | ------------------------------------------------ |
| token     | string | Token JWT utilizado para identificar al usuario. |



#### POST /api/logout

Desloguea al usuario del cliente.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |





## Usuarios

#### GET /api/user/{username}

Devuelve toda la información asociada a un usuario.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Parámetros de la URL:

| Nombre   | Opcional | Descripción                     |
| -------- | :------: | ------------------------------- |
| username |   :x:    | Nombre del usuario a consultar. |

Respuesta:

| Parámetro | Key        | Tipo   | Descripción                                                 |
| --------- | ---------- | ------ | ----------------------------------------------------------- |
| data      |            | dict   | Diccionario con toda la información del usuario consultado. |
|           | type       | string | Tipo de usuario.                                            |
|           | public_id  | string | UUID del usuario.                                           |
|           | first_name | string | Nombre del usuario.                                         |
|           | last_name  | string | Apellido del usuario.                                       |
|           | username   | string | Nickname del usuario.                                       |
|           | email      | string | Email del usuario.                                          |



#### POST /api/user/query

Devuelve los usuarios que cumplen los criterios de búsqueda.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo |      Opcional      | Descripción                                |
| --------- | ---- | :----------------: | ------------------------------------------ |
| query     | dict |        :x:         | Criterio de búsqueda.                      |
| filter    | dict | :heavy_check_mark: | Parámetros que se quieren en la respuesta. |

Respuesta (un solo usuario):

| Parámetro  | Tipo   | Descripción           |
| ---------- | ------ | --------------------- |
| type       | string | Tipo de usuario.      |
| public_id  | string | UUID del usuario.     |
| first_name | string | Nombre del usuario.   |
| last_name  | string | Apellido del usuario. |
| username   | string | Nickname del usuario. |
| email      | string | Email del usuario.    |

Respuesta (más de un usuario):

| Parámetro | Tipo          | Descripción                                             |
| --------- | ------------- | ------------------------------------------------------- |
| total     | int           | Número de usuarios que cumplen el criterio de búsqueda. |
| items     | list[Usuario] | Usuarios que cumplen el criterio de búsqueda.           |



#### POST /api/user

Crea un nuevo usuario.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro  | Tipo   | Opcional | Descripción             |
| ---------- | ------ | :------: | ----------------------- |
| type       | string |   :x:    | Tipo de usuario.        |
| password   | string |   :x:    | Contraseña del usuario. |
| first_name | string |   :x:    | Nombre del usuario.     |
| last_name  | string |   :x:    | Apellido del usuario.   |
| username   | string |   :x:    | Nickname del usuario.   |
| email      | string |   :x:    | Email del usuario.      |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### PUT /api/user

Modifica los datos de un usuario.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Key        | Tipo   | Opcional | Descripción                                |
| --------- | ---------- | ------ | :------: | ------------------------------------------ |
| email     |            | string |   :x:    | Email del usuario que se quiere modificar. |
| data      |            | dict   |   :x:    | Nuevos datos del usuario.                  |
|           | type       | string |   :x:    | Tipo de usuario.                           |
|           | password   | string |   :x:    | Contraseña del usuario.                    |
|           | first_name | string |   :x:    | Nombre del usuario.                        |
|           | last_name  | string |   :x:    | Apellido del usuario.                      |
|           | username   | string |   :x:    | Nickname del usuario.                      |
|           | email      | string |   :x:    | Email del usuario.                         |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### DELETE /api/user

Elimina un usuario.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                               |
| --------- | ------ | :------: | ----------------------------------------- |
| email     | string |   :x:    | Email del usuario que se quiere eliminar. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## Aprovisionamiento

#### POST /api/provision

Ejecuta un playbook.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Key         | Tipo         |      Opcional      | Descripción                                          |
| --------- | ----------- | ------------ | :----------------: | ---------------------------------------------------- |
| hosts     |             | list[string] |        :x:         | Grupo de hosts donde se quiere ejecutar el playbook. |
| playbook  |             | string       |        :x:         | Nombre del playbook a ejecutar.                      |
| passwords |             | dict         |        :x:         | Contraseñas necesarias para la conexión a los hosts. |
|           | conn_pass   | string       | :heavy_check_mark: | Contraseña de acceso.                                |
|           | become_pass | string       | :heavy_check_mark: | Contraseña para acceder al root.                     |

Respuesta:

| Parámetro | Tipo   | Descripción                             |
| --------- | ------ | --------------------------------------- |
| result    | string | Respuesta de la ejecución del playbook. |



### Hosts

#### GET /api/provision/hosts/{name}

Devuelve toda la información asociada a un grupo de hosts.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Parámetros de la URL:

| Nombre | Tipo   | Opcional | Descripción                            |
| ------ | ------ | :------: | -------------------------------------- |
| name   | string |   :x:    | Nombre del grupo de hosts a consultar. |

Respuesta:

| Parámetro | Tipo         | Descripción                |
| --------- | ------------ | -------------------------- |
| name      | string       | Nombre del grupo de hosts. |
| ips       | list[string] | Direcciones IPv4.          |



#### POST /api/provision/hosts/query

Devuelve los grupos de hosts que cumplen los criterios de búsqueda.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo | Opcional | Descripción                                |
| --------- | ---- | :------: | ------------------------------------------ |
| query     | dict |    ❌     | Criterio de búsqueda.                      |
| filter    | dict |    ✔️     | Parámetros que se quieren en la respuesta. |

Respuesta (un solo grupo de hosts):

| Parámetro | Tipo         | Descripción                |
| --------- | ------------ | -------------------------- |
| name      | string       | Nombre del grupo de hosts. |
| ips       | list[string] | Direcciones IPv4.          |

Respuesta (más de un grupo de hosts):

| Parámetro | Tipo        | Descripción                                                  |
| --------- | ----------- | ------------------------------------------------------------ |
| total     | int         | Número de grupos de hosts que cumplen el criterio de búsqueda. |
| items     | list[Hosts] | Grupos de hosts que cumplen el criterio de búsqueda.         |



#### POST /api/provision/hosts

Crea un nuevo grupo de hosts.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo         | Opcional | Descripción                |
| --------- | ------------ | :------: | -------------------------- |
| name      | string       |   :x:    | Nombre del grupo de hosts. |
| ips       | list[string] |   :x:    | Direcciones IPv4.          |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### PUT /api/provision/hosts

Modifica los datos de una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Key  | Tipo         | Opcional | Descripción                                        |
| --------- | ---- | ------------ | :------: | -------------------------------------------------- |
| name      |      | string       |   :x:    | Nombre del grupo de hosts que se quiere modificar. |
| data      |      | dict         |   :x:    | Nuevos datos del grupo de hosts.                   |
|           | name | string       |   :x:    | Nombre del grupo de hosts.                         |
|           | ips  | list[string] |   :x:    | Direcciones IPv4.                                  |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### DELETE /api/provision/hosts

Elimina una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                       |
| --------- | ------ | :------: | ------------------------------------------------- |
| name      | string |   :x:    | Nombre del grupo de hosts que se quiere eliminar. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



### Playbooks

#### GET /api/provision/playbook/{name}

Devuelve toda la información asociada a un playbook.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Parámetros de la URL:

| Nombre | Tipo   | Opcional | Descripción                      |
| ------ | ------ | :------: | -------------------------------- |
| name   | string |   :x:    | Nombre del playbook a consultar. |

Respuesta:

| Parámetro | Tipo   | Descripción                                  |
| --------- | ------ | -------------------------------------------- |
| name      | string | Nombre del playbook.                         |
| playbook  | dict   | Contenido del playbook codificado como JSON. |



#### POST /api/provision/playbook/query

Devuelve los grupos de hosts que cumplen los criterios de búsqueda.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo | Opcional | Descripción                                |
| --------- | ---- | :------: | ------------------------------------------ |
| query     | dict |    ❌     | Criterio de búsqueda.                      |
| filter    | dict |    ✔️     | Parámetros que se quieren en la respuesta. |

Respuesta (una sola máquina):

| Parámetro | Tipo   | Descripción                                  |
| --------- | ------ | -------------------------------------------- |
| name      | string | Nombre del playbook.                         |
| playbook  | dict   | Contenido del playbook codificado como JSON. |

Respuesta (más de una máquina):

| Parámetro | Tipo          | Descripción                                              |
| --------- | ------------- | -------------------------------------------------------- |
| total     | int           | Número de playbooks que cumplen el criterio de búsqueda. |
| items     | list[Machine] | Playbooks que cumplen el criterio de búsqueda.           |



#### POST /api/provision/playbook

Crea un nuevo playbook.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                  |
| --------- | ------ | :------: | -------------------------------------------- |
| name      | string |   :x:    | Nombre del playbook.                         |
| playbook  | dict   |   :x:    | Contenido del playbook codificado como JSON. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### PUT /api/provision/playbook

Modifica los datos de una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Key      | Tipo   | Opcional | Descripción                                  |
| --------- | -------- | ------ | :------: | -------------------------------------------- |
| name      |          | string |   :x:    | Nombre del playbook que se quiere modificar. |
| data      |          | dict   |   :x:    | Nuevos datos del playbook.                   |
|           | name     | string |   :x:    | Nombre del playbook.                         |
|           | playbook | dict   |   :x:    | Contenido del playbook codificado como JSON. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### DELETE /api/provision/playbook

Elimina una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                 |
| --------- | ------ | :------: | ------------------------------------------- |
| name      | string |   :x:    | Nombre del playbook que se quiere eliminar. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## Despliegue

#### POST /api/deploy/container

Permite ejecutar operaciones básicas en todos los contenedores.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                                  |
| --------- | ------ | :------: | ------------------------------------------------------------ |
| operation | string |   :x:    | Nombre de la operación que se quiere ejecutar. Valores posibles: *run*, *get*, *list*, *prune*. |
| data      | dict   |   :x:    | Argumentos de la operación.                                  |

Tipos de operaciones:

##### run

| Parámetro | Key         | Tipo         |      Opcional      | Descripción                                                  |
| --------- | ----------- | ------------ | :----------------: | ------------------------------------------------------------ |
| data      |             | dict         |         ❌          | Argumentos de la operación.                                  |
|           | image       | string       |        :x:         | Imagen a ejecutar.                                           |
|           | command     | list[string] | :heavy_check_mark: | Comando a ejecutar en el contenedor.                         |
|           | auto_remove | bool         | :heavy_check_mark: | Eliminar o no el contenedor al terminar la ejecución.        |
|           | detach      | bool         | :heavy_check_mark: | Ejecutar o no el contenedor en segundo plano. Por defecto *true*. |
|           | entrypoint  | list[string] | :heavy_check_mark: | Entrypoint del contenedor.                                   |
|           | environment | dict         | :heavy_check_mark: | Variables de entorno.                                        |
|           | hostname    | string       | :heavy_check_mark: | Hostname del contenedor.                                     |
|           | mounts      | list[string] | :heavy_check_mark: | Lista de volumenes que se montan en el contenedor.           |
|           | name        | string       | :heavy_check_mark: | Nombre del contenedor.                                       |
|           | network     | string       | :heavy_check_mark: | Nombre de la red a la que se conecta.                        |
|           | ports       | dict         | :heavy_check_mark: | Puertos a enlazar.                                           |
|           | user        | string       | :heavy_check_mark: | Usuario para ejecutar los posibles comandos dentro del contenedor. |
|           | volumes     | dict         | :heavy_check_mark: | Volumenes a montar.                                          |
|           | working_dir | string       | :heavy_check_mark: | Directorio de trabajo.                                       |
|           | remove      | bool         | :heavy_check_mark: | Eliminar el contenedor al terminar la ejecución.             |



##### get

| Parámetro | Key          | Tipo   | Opcional | Descripción                  |
| --------- | ------------ | ------ | :------: | ---------------------------- |
| data      |              | dict   |    ❌     | Argumentos de la operación.  |
|           | container_id | string |   :x:    | Identificador del contenedor |

Respuesta:

| Parámetro | Tipo   | Descripción                                            |
| --------- | ------ | ------------------------------------------------------ |
| id        | string | Identificador del contenedor                           |
| short_id  | string | Identificador del contenedor truncado a 10 carácteres. |
| name      | string | Nombre del contenedor.                                 |
| labels    | dict   | Etiquetas del contenedor.                              |
| status    | string | Estado del contenedor.                                 |
| image     | Image  | Imagen que se esta ejecutando en el contenedor.        |



##### list

| Parámetro | Key     | Tipo                | Opcional | Descripción                                                  |
| --------- | ------- | ------------------- | :------: | ------------------------------------------------------------ |
| data      |         | dict                |    ❌     | Argumentos de la operación.                                  |
|           | all     | bool                |   :x:    | Mostrar o no todos los contenedores (en ejecución y detenidos o finalizados). |
|           | since   | string              |   :x:    | Mostrar contenedores creados desde este identificador.       |
|           | before  | string              |   :x:    | Mostrar contenedores creados previos a este identificador.   |
|           | filters | [filters](#filters) |   :x:    | Filtros para afinar la búsqueda.                             |

Respuesta (un solo contenedor):

| Parámetro | Tipo   | Descripción                                            |
| --------- | ------ | ------------------------------------------------------ |
| id        | string | Identificador del contenedor                           |
| short_id  | string | Identificador del contenedor truncado a 10 carácteres. |
| name      | string | Nombre del contenedor.                                 |
| labels    | dict   | Etiquetas del contenedor.                              |
| status    | string | Estado del contenedor.                                 |
| image     | Image  | Imagen que se esta ejecutando en el contenedor.        |

Respuesta (más de un contenedor):

| Parámetro | Tipo             | Descripción                                                 |
| --------- | ---------------- | ----------------------------------------------------------- |
| total     | int              | Número de contenedores que cumplen el criterio de búsqueda. |
| items     | list[Contenedor] | Contenedores que cumplen el criterio de búsqueda.           |



##### prune

| Parámetro | Key     | Tipo                |      Opcional      | Descripción                 |
| --------- | ------- | ------------------- | :----------------: | --------------------------- |
| data      |         | dict                |         ❌          | Argumentos de la operación. |
|           | filters | [filters](#filters) | :heavy_check_mark: | Filtros.                    |



#### Filtros de Contenedores {#filters}

| Parámetro | Key    | Tipo    |      Opcional      | Descripción                                       |
| --------- | ------ | ------- | :----------------: | ------------------------------------------------- |
| filters   |        | dict    |         ❌          |                                                   |
|           | exited | boolean | :heavy_check_mark: | Si el contenedor ha finalizado su ejecución o no. |
|           | status | string  | :heavy_check_mark: | Estado del contenedor.                            |
|           | id     | string  | :heavy_check_mark: | Identificador del contenedor.                     |
|           | name   | string  | :heavy_check_mark: | Nombre del contenedor.                            |

---

#### POST /api/deploy/container/single

Permite ejecutar operaciones básicas en un contenedor en concreto.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro    | Tipo   | Opcional | Descripción                                                  |
| ------------ | ------ | :------: | ------------------------------------------------------------ |
| container_id | string |   :x:    | Identificador del contenedor.                                |
| operation    | string |   :x:    | Nombre de la operación que se quiere ejecutar. Valores posibles: *kill*, *logs*, *pause*, *reload*, *rename*, *restart*, *stop*, *unpause*. |
| data         | dict   |   :x:    | Argumentos de la operación.                                  |

Tipos de operaciones:

##### rename

| Parámetro | Key  | Tipo   | Opcional | Descripción                  |
| --------- | ---- | ------ | :------: | ---------------------------- |
| data      |      | dict   |    ❌     | Argumentos de la operación.  |
|           | name | string |   :x:    | Nuevo nombre del contenedor. |

##### logs

Respuesta:

| Parámetro | Tipo   | Descripción          |
| --------- | ------ | -------------------- |
| data      | string | Logs del contenedor. |



#### POST /api/deploy/image

Permite ejecutar operaciones básicas en todos las imágenes.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                                  |
| --------- | ------ | :------: | ------------------------------------------------------------ |
| operation | string |   :x:    | Nombre de la operación que se quiere ejecutar. Valores posibles: *list*, *get*, *prune*, *pull*, *remove*, *search*. |
| data      | dict   |   :x:    | Argumentos de la operación.                                  |

Tipos de operaciones:

##### list

| Parámetro | Key     | Tipo   |      Opcional      | Descripción                                                  |
| --------- | ------- | ------ | :----------------: | ------------------------------------------------------------ |
| data      |         | dict   |         ❌          | Argumentos de la operación.                                  |
|           | name    | string | :heavy_check_mark: | Mostrar sólo las imágenes pertenecientes a este repositorio. |
|           | all     | bool   | :heavy_check_mark: | Mostrar todas las imágenes o no (incluídas las imágenes de capas intermedias). |
|           | filters |        | :heavy_check_mark: | Filtros adicionales.                                         |

##### get

| Parámetro | Key  | Tipo   | Opcional | Descripción                 |
| --------- | ---- | ------ | :------: | --------------------------- |
| data      |      | dict   |    ❌     | Argumentos de la operación. |
|           | name | string |    ❌     | Nombre de la imagen.        |

##### prune

| Parámetro | Key     | Tipo |      Opcional      | Descripción                 |
| --------- | ------- | ---- | :----------------: | --------------------------- |
| data      |         | dict |         ❌          | Argumentos de la operación. |
|           | filters |      | :heavy_check_mark: | Filtros adicionales.        |

##### pull

| Parámetro | Key         | Tipo   |      Opcional      | Descripción                                |
| --------- | ----------- | ------ | :----------------: | ------------------------------------------ |
| data      |             | dict   |         ❌          | Argumentos de la operación.                |
|           | repository  | string | :heavy_check_mark: | Repositorio e imagen a descargar.          |
|           | tag         | string | :heavy_check_mark: | Tag de la imagen.                          |
|           | auth_config | dict   | :heavy_check_mark: | Sobreescribir las credenciales.            |
|           | platform    | string | :heavy_check_mark: | Plataforma en formato: os[/arch[/variant]] |

## Máquinas

#### GET /api/machine/{name}

Devuelve toda la información asociada a una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Parámetros de la URL:

| Nombre | Opcional | Descripción                       |
| ------ | :------: | --------------------------------- |
| name   |   :x:    | Nombre de la máquina a consultar. |

Respuesta:

| Parámetro | Key         | Tipo   | Descripción                                                  |
| --------- | ----------- | ------ | ------------------------------------------------------------ |
| data      |             | dict   | Diccionario con toda la información de la máquina consultada. |
|           | name        | string | Tipo de usuario.                                             |
|           | description | string | Descripción de la máquina.                                   |
|           | type        | string | Tipo de la máquina.                                          |
|           | ipv4        | string | Dirección IPv4 de la máquina.                                |
|           | ipv6        | string | Dirección IPv6 de la máquina.                                |
|           | mac         | string | Dirección MAC de la máquina.                                 |
|           | broadcast   | string | Broadcast de la red a la que se conecta la máquina.          |
|           | gateway     | string | Gateway de la red a la que se conecta la máquina.            |
|           | netmask     | string | Netmask de la red a la que se conecta la máquina.            |
|           | network     | string | Network de la red a la que se conecta la máquina.            |



#### POST /api/machine/query

Devuelve las máquinas que cumplen los criterios de búsqueda.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo | Opcional | Descripción                                |
| --------- | ---- | :------: | ------------------------------------------ |
| query     | dict |    ❌     | Criterio de búsqueda.                      |
| filter    | dict |    ✔️     | Parámetros que se quieren en la respuesta. |

Respuesta (una sola máquina):

| Parámetro   | Tipo   | Descripción                                         |
| ----------- | ------ | --------------------------------------------------- |
| name        | string | Tipo de usuario.                                    |
| description | string | Descripción de la máquina.                          |
| type        | string | Tipo de la máquina.                                 |
| ipv4        | string | Dirección IPv4 de la máquina.                       |
| ipv6        | string | Dirección IPv6 de la máquina.                       |
| mac         | string | Dirección MAC de la máquina.                        |
| broadcast   | string | Broadcast de la red a la que se conecta la máquina. |
| gateway     | string | Gateway de la red a la que se conecta la máquina.   |
| netmask     | string | Netmask de la red a la que se conecta la máquina.   |
| network     | string | Network de la red a la que se conecta la máquina.   |

Respuesta (más de una máquina):

| Parámetro | Key         | Tipo       | Descripción                                             |
| --------- | ----------- | ---------- | ------------------------------------------------------- |
| total     |             | int        | Número de máquinas que cumplen el criterio de búsqueda. |
| items     |             | list[dict] | Máquinas que cumplen el criterio de búsqueda.           |
|           | name        | string     | Tipo de usuario.                                        |
|           | description | string     | Descripción de la máquina.                              |
|           | type        | string     | Tipo de la máquina.                                     |
|           | ipv4        | string     | Dirección IPv4 de la máquina.                           |
|           | ipv6        | string     | Dirección IPv6 de la máquina.                           |
|           | mac         | string     | Dirección MAC de la máquina.                            |
|           | broadcast   | string     | Broadcast de la red a la que se conecta la máquina.     |
|           | gateway     | string     | Gateway de la red a la que se conecta la máquina.       |
|           | netmask     | string     | Netmask de la red a la que se conecta la máquina.       |
|           | network     | string     | Network de la red a la que se conecta la máquina.       |



#### POST /api/machine

Crea una nueva máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro   | Tipo   |      Opcional      | Descripción                                         |
| ----------- | ------ | :----------------: | --------------------------------------------------- |
| name        | string |        :x:         | Tipo de usuario.                                    |
| description | string | :heavy_check_mark: | Descripción de la máquina.                          |
| type        | string |        :x:         | Tipo de la máquina.                                 |
| ipv4        | string | :heavy_check_mark: | Dirección IPv4 de la máquina.                       |
| ipv6        | string | :heavy_check_mark: | Dirección IPv6 de la máquina.                       |
| mac         | string | :heavy_check_mark: | Dirección MAC de la máquina.                        |
| broadcast   | string | :heavy_check_mark: | Broadcast de la red a la que se conecta la máquina. |
| gateway     | string | :heavy_check_mark: | Gateway de la red a la que se conecta la máquina.   |
| netmask     | string | :heavy_check_mark: | Netmask de la red a la que se conecta la máquina.   |
| network     | string | :heavy_check_mark: | Network de la red a la que se conecta la máquina.   |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### PUT /api/machine

Modifica los datos de una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Key         | Tipo   |      Opcional      | Descripción                                         |
| --------- | ----------- | ------ | :----------------: | --------------------------------------------------- |
| name      |             | string |        :x:         | Nombre de la máquina que se quiere modificar.       |
| data      |             | dict   |        :x:         | Nuevos datos de la máquina.                         |
|           | name        | string |        :x:         | Tipo de usuario.                                    |
|           | description | string | :heavy_check_mark: | Descripción de la máquina.                          |
|           | type        | string |        :x:         | Tipo de la máquina.                                 |
|           | ipv4        | string | :heavy_check_mark: | Dirección IPv4 de la máquina.                       |
|           | ipv6        | string | :heavy_check_mark: | Dirección IPv6 de la máquina.                       |
|           | mac         | string | :heavy_check_mark: | Dirección MAC de la máquina.                        |
|           | broadcast   | string | :heavy_check_mark: | Broadcast de la red a la que se conecta la máquina. |
|           | gateway     | string | :heavy_check_mark: | Gateway de la red a la que se conecta la máquina.   |
|           | netmask     | string | :heavy_check_mark: | Netmask de la red a la que se conecta la máquina.   |
|           | network     | string | :heavy_check_mark: | Network de la red a la que se conecta la máquina.   |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



#### DELETE /api/machine

Elimina una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                  |
| --------- | ------ | :------: | -------------------------------------------- |
| name      | string |   :x:    | Nombre de la máquina que se quiere eliminar. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |