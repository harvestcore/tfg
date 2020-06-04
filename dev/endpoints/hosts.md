# Grupos de Hosts

### Hosts

| Parámetro | Tipo         | Opcional | E/S  | Descripción                |
| --------- | ------------ | :------: | :--: | -------------------------- |
| name      | string       |   :x:    | E/S  | Nombre del grupo de hosts. |
| ips       | list[string] |   :x:    | E/S  | Direcciones IPv4.          |



## GET /api/provision/hosts/{name}

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

| Parámetro | Tipo            | Descripción                                                  |
| --------- | --------------- | ------------------------------------------------------------ |
| data      | [Hosts](#hosts) | Diccionario con toda la información del grupo de hosts consultado. |



## POST /api/provision/hosts/query

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

| Parámetro | Tipo            | Descripción                                        |
| --------- | --------------- | -------------------------------------------------- |
| data      | [Hosts](#hosts) | Grupo de hosts que cumple el criterio de búsqueda. |

Respuesta (más de un grupo de hosts):

| Parámetro | Tipo                  | Descripción                                                  |
| --------- | --------------------- | ------------------------------------------------------------ |
| total     | int                   | Número de grupos de hosts que cumplen el criterio de búsqueda. |
| items     | list[[Hosts](#hosts)] | Grupos de hosts que cumplen el criterio de búsqueda.         |



## POST /api/provision/hosts

Crea un nuevo grupo de hosts.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

- [Hosts](#hosts)

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## PUT /api/provision/hosts

Modifica los datos de un grupo de hosts.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo            | Opcional | Descripción                                        |
| --------- | --------------- | :------: | -------------------------------------------------- |
| name      | string          |   :x:    | Nombre del grupo de hosts que se quiere modificar. |
| data      | [Hosts](#hosts) |   :x:    | Nuevos datos del grupo de hosts.                   |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## DELETE /api/provision/hosts

Elimina un grupo de hosts.

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