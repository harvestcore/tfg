# Usuarios

### Usuario

| Parámetro  | Tipo   | Opcional | E/S  | Descripción             |
| ---------- | ------ | :------: | :--: | ----------------------- |
| type       | string |   :x:    | E/S  | Tipo de usuario.        |
| public_id  | string |    -     |  S   | UUID del usuario.       |
| first_name | string |   :x:    | E/S  | Nombre del usuario.     |
| last_name  | string |   :x:    | E/S  | Apellido del usuario.   |
| username   | string |   :x:    | E/S  | Nickname del usuario.   |
| email      | string |   :x:    | E/S  | Email del usuario.      |
| password   | string |   :x:    |  E   | Contraseña del usuario. |



---



## GET /user/{username}

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

| Parámetro | Tipo                | Descripción                                                 |
| --------- | ------------------- | ----------------------------------------------------------- |
| data      | [Usuario](#usuario) | Diccionario con toda la información del usuario consultado. |



## POST /user/query

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

| Parámetro | Tipo                | Descripción                                 |
| --------- | ------------------- | ------------------------------------------- |
| data      | [Usuario](#usuario) | Usuario que cumple el criterio de búsqueda. |

Respuesta (más de un usuario):

| Parámetro | Tipo                      | Descripción                                             |
| --------- | ------------------------- | ------------------------------------------------------- |
| total     | int                       | Número de usuarios que cumplen el criterio de búsqueda. |
| items     | list[[Usuario](#usuario)] | Usuarios que cumplen el criterio de búsqueda.           |



## POST /user

Crea un nuevo usuario.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

- [Usuario](#usuario)

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## PUT /user

Modifica los datos de un usuario.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo                | Opcional | Descripción                                |
| --------- | ------------------- | :------: | ------------------------------------------ |
| email     | string              |   :x:    | Email del usuario que se quiere modificar. |
| data      | [Usuario](#usuario) |   :x:    | Nuevos datos del usuario.                  |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## DELETE /user

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