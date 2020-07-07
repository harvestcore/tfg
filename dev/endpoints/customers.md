# Clientes

### Cliente

| Parámetro | Tipo   | Opcional | E/S  | Descripción                |
| --------- | ------ | :------: | :--: | -------------------------- |
| domain    | string |   :x:    | E/S  | Subdominio del cliente.    |
| db_name   | string |   :x:    | E/S  | Base de datos del cliente. |



---



## POST /customer/query

Devuelve los clientes que cumplen los criterios de búsqueda.

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
| data      | [Cliente](#cliente) | Cliente que cumple el criterio de búsqueda. |

Respuesta (más de un usuario):

| Parámetro | Tipo                      | Descripción                                             |
| --------- | ------------------------- | ------------------------------------------------------- |
| total     | int                       | Número de clientes que cumplen el criterio de búsqueda. |
| items     | list[[Cliente](#cliente)] | Clientes que cumplen el criterio de búsqueda.           |



## POST /customer

Crea un nuevo cliente.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

- [Cliente](#cliente)

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## PUT /customer

Modifica los datos de un cliente.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo                | Opcional | Descripción                                    |
| --------- | ------------------- | :------: | ---------------------------------------------- |
| domain    | string              |   :x:    | Subominio del cliente que se quiere modificar. |
| data      | [Cliente](#cliente) |   :x:    | Nuevos datos del cliente.                      |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## DELETE /customer

Elimina un cliente.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo   | Opcional | Descripción                                    |
| --------- | ------ | :------: | ---------------------------------------------- |
| domain    | string |   :x:    | Subdominio del cliente que se quiere eliminar. |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |