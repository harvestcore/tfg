# Máquinas

### Máquina

| Parámetro   | Tipo   | Opcional | E/S  | Descripción                                         |
| ----------- | ------ | :------: | :--: | --------------------------------------------------- |
| name        | string |    ❌     | E/S  | Tipo de usuario.                                    |
| description | string |    ✔️     | E/S  | Descripción de la máquina.                          |
| type        | string |    ❌     | E/S  | Tipo de la máquina.                                 |
| ipv4        | string |    ✔️     | E/S  | Dirección IPv4 de la máquina.                       |
| ipv6        | string |    ✔️     | E/S  | Dirección IPv6 de la máquina.                       |
| mac         | string |    ✔️     | E/S  | Dirección MAC de la máquina.                        |
| broadcast   | string |    ✔️     | E/S  | Broadcast de la red a la que se conecta la máquina. |
| gateway     | string |    ✔️     | E/S  | Gateway de la red a la que se conecta la máquina.   |
| netmask     | string |    ✔️     | E/S  | Netmask de la red a la que se conecta la máquina.   |
| network     | string |    ✔️     | E/S  | Network de la red a la que se conecta la máquina.   |



---



## GET /machine/{name}

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

| Parámetro | Tipo                | Descripción                                                  |
| --------- | ------------------- | ------------------------------------------------------------ |
| data      | [Machine](#machine) | Diccionario con toda la información de la máquina consultada. |





## POST /machine/query

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

Respuesta (una sola máquina):

| Parámetro | Tipo                | Descripción                                 |
| --------- | ------------------- | ------------------------------------------- |
| data      | [Machine](#machine) | Máquina que cumple el criterio de búsqueda. |

ReRespuesta (más de una máquina):

| Parámetro | Tipo                      | Descripción                                             |
| --------- | ------------------------- | ------------------------------------------------------- |
| total     | int                       | Número de máquinas que cumplen el criterio de búsqueda. |
| items     | list[[Machine](#machine)] | Máquinas que cumplen el criterio de búsqueda.           |



## POST /machine

Crea una nueva máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

- [Machine](#machine)

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## PUT /machine

Modifica los datos de una máquina.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo                | Opcional | Descripción                                   |
| --------- | ------------------- | :------: | --------------------------------------------- |
| name      | string              |   :x:    | Nombre de la máquina que se quiere modificar. |
| data      | [Machine](#machine) |   :x:    | Nuevos datos de la máquina.                   |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## DELETE /machine

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