# Despliegue

### Contenedor

| Parámetro | Tipo   | E/S  | Descripción                                            |
| --------- | ------ | :--: | ------------------------------------------------------ |
| id        | string |  S   | Identificador del contenedor                           |
| short_id  | string |  S   | Identificador del contenedor truncado a 10 carácteres. |
| name      | string |  S   | Nombre del contenedor.                                 |
| labels    | dict   |  S   | Etiquetas del contenedor.                              |
| status    | string |  S   | Estado del contenedor.                                 |
| image     | Image  |  S   | Imagen que se esta ejecutando en el contenedor.        |



### Imagen

| Parámetro | Tipo         | E/S  | Descripción                                          |
| --------- | ------------ | :--: | ---------------------------------------------------- |
| id        | string       |  S   | Identificador de la imagen.                          |
| labels    | dict         |  S   | Etiquetas de la imagen.                              |
| short_id  | string       |  S   | Identificador de la imagen truncado a 10 carácteres. |
| tags      | list[string] |  S   | Tags de la imagen.                                   |



### Filtro de contenedores

| Parámetro | Key    | Tipo    | Opcional | Descripción                                       |
| --------- | ------ | ------- | :------: | ------------------------------------------------- |
| filters   |        | dict    |    ❌     |                                                   |
|           | exited | boolean |    ✔️     | Si el contenedor ha finalizado su ejecución o no. |
|           | status | string  |    ✔️     | Estado del contenedor.                            |
|           | id     | string  |    ✔️     | Identificador del contenedor.                     |
|           | name   | string  |    ✔️     | Nombre del contenedor.                            |



### Filtro de imágenes

| Parámetro | Key      | Tipo    |      Opcional      | Descripción                             |
| --------- | -------- | ------- | :----------------: | --------------------------------------- |
| filters   |          | dict    |         ❌          |                                         |
|           | dangling | boolean |         ✔️          | Si la imagen se encuentra colgada o no. |
|           | label    | string  | :heavy_check_mark: | Etiqueta de la imagen.                  |



---



## POST /deploy/container

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

| Parámetro | Key     | Tipo                              | Opcional | Descripción                                                  |
| --------- | ------- | --------------------------------- | :------: | ------------------------------------------------------------ |
| data      |         | dict                              |    ❌     | Argumentos de la operación.                                  |
|           | all     | bool                              |   :x:    | Mostrar o no todos los contenedores (en ejecución y detenidos o finalizados). |
|           | since   | string                            |   :x:    | Mostrar contenedores creados desde este identificador.       |
|           | before  | string                            |   :x:    | Mostrar contenedores creados previos a este identificador.   |
|           | filters | [Filtro](#filtro-de-contenedores) |   :x:    | Filtros para afinar la búsqueda.                             |

Respuesta (un solo contenedor):

| Parámetro | Tipo                            | Descripción                                    |
| --------- | ------------------------------- | ---------------------------------------------- |
| data      | list[[Contenedor](#contenedor)] | Contenedor que cumple el criterio de búsqueda. |

Respuesta (más de un contenedor):

| Parámetro | Tipo                            | Descripción                                                 |
| --------- | ------------------------------- | ----------------------------------------------------------- |
| total     | int                             | Número de contenedores que cumplen el criterio de búsqueda. |
| items     | list[[Contenedor](#contenedor)] | Contenedores que cumplen el criterio de búsqueda.           |



##### prune

| Parámetro | Key     | Tipo                              |      Opcional      | Descripción                 |
| --------- | ------- | --------------------------------- | :----------------: | --------------------------- |
| data      |         | dict                              |         ❌          | Argumentos de la operación. |
|           | filters | [Filtro](#filtro-de-contenedores) | :heavy_check_mark: | Filtros.                    |



## POST /deploy/container/single

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



## POST /deploy/image

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

| Parámetro | Key     | Tipo                          |      Opcional      | Descripción                                                  |
| --------- | ------- | ----------------------------- | :----------------: | ------------------------------------------------------------ |
| data      |         | dict                          |         ❌          | Argumentos de la operación.                                  |
|           | name    | string                        | :heavy_check_mark: | Mostrar sólo las imágenes pertenecientes a este repositorio. |
|           | all     | bool                          | :heavy_check_mark: | Mostrar todas las imágenes o no (incluídas las imágenes de capas intermedias). |
|           | filters | [Filtro](#filtro-de-imágenes) | :heavy_check_mark: | Filtros adicionales.                                         |

Respuesta (una sola imagen):

| Parámetro | Tipo              | Descripción                             |
| --------- | ----------------- | --------------------------------------- |
| data      | [Imagen](#imagen) | Diccionario con los datos de la imagen. |

Respuesta (más de una imagen):

| Parámetro | Tipo                    | Descripción                  |
| --------- | ----------------------- | ---------------------------- |
| total     | int                     | Número de imágenes listadas. |
| items     | list[[Imagen](#imagen)] | Imágenes listadas.           |

##### get

| Parámetro | Key  | Tipo   | Opcional | Descripción                 |
| --------- | ---- | ------ | :------: | --------------------------- |
| data      |      | dict   |    ❌     | Argumentos de la operación. |
|           | name | string |    ❌     | Nombre de la imagen.        |

Respuesta:

- [Imagen](#imagen)

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

Respuesta:

- [Imagen](#imagen) descargada.

##### remove

| Parámetro | Key     | Tipo   |      Opcional      | Descripción                         |
| --------- | ------- | ------ | :----------------: | ----------------------------------- |
| data      |         | dict   |         ❌          | Argumentos de la operación.         |
|           | image   | string |        :x:         | Imagen a eliminar.                  |
|           | force   | bool   | :heavy_check_mark: | Forzar borrado.                     |
|           | noprune | bool   | :heavy_check_mark: | Borrar o no imágenes padre sin tag. |

##### search

| Parámetro | Key  | Tipo   | Opcional | Descripción                 |
| --------- | ---- | ------ | :------: | --------------------------- |
| data      |      | dict   |    ❌     | Argumentos de la operación. |
|           | term | string |   :x:    | Término de búsqueda.        |

Respuesta:

| Parámetro | Key          | Tipo       | Descripción                       |
| --------- | ------------ | ---------- | --------------------------------- |
| total     |              | int        | Número de imágenes encontradas.   |
| items     |              | list[dict] | Imágenes encontradas.             |
|           | star_count   | int        | Número de estrellas en DockerHub. |
|           | is_official  | bool       | Si la imagen es oficial o no.     |
|           | name         | string     | Nombre de la imagen               |
|           | is_automated | bool       | Imagen automatizada.              |
|           | description  | string     | Descripción.                      |



## POST /deploy/image/single

Permite ejecutar operaciones básicas en una imagen en concreto.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                                  |
| --------- | ------ | :------: | ------------------------------------------------------------ |
| name      | string |   :x:    | Nombre de la imagen.                                         |
| operation | string |   :x:    | Nombre de la operación que se quiere ejecutar. Valores posibles: *history*, *reload*. |
| data      | dict   |   :x:    | Argumentos de la operación.                                  |

Tipos de operaciones:

##### history

Respuesta:

| Parámetro | Tipo   | Descripción            |
| --------- | ------ | ---------------------- |
| data      | string | Historia de la imagen. |

##### reload

Recarga la imagen y aplica los posibles cambios que tenga.

