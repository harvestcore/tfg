# Playbooks

### Playbook

| Parámetro | Tipo   | Opcional | E/S  | Descripción                                  |
| --------- | ------ | :------: | :--: | -------------------------------------------- |
| name      | string |   :x:    | E/S  | Nombre del playbook.                         |
| playbook  | dict   |   :x:    | E/S  | Contenido del playbook codificado como JSON. |



---



## GET /provision/playbook/{name}

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

| Parámetro | Tipo                  | Descripción                                                  |
| --------- | --------------------- | ------------------------------------------------------------ |
| data      | [Playbook](#playbook) | Diccionario con toda la información del playbook consultado. |



## POST /provision/playbook/query

Devuelve los playbooks que cumplen los criterios de búsqueda.

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

| Parámetro | Tipo                  | Descripción        |
| --------- | --------------------- | ------------------ |
| data      | [Playbook](#playbook) | Playbook obtenido. |

Respuesta (más de una máquina):

| Parámetro | Tipo                        | Descripción                                              |
| --------- | --------------------------- | -------------------------------------------------------- |
| total     | int                         | Número de playbooks que cumplen el criterio de búsqueda. |
| items     | list[[Playbook](#playbook)] | Playbooks que cumplen el criterio de búsqueda.           |





## POST /provision/playbook

Crea un nuevo playbook.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

- [Playbook](#playbook)

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## PUT /provision/playbook

Modifica los datos de un playbook.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Tipo                  | Opcional | Descripción                                  |
| --------- | --------------------- | :------: | -------------------------------------------- |
| name      | string                |   :x:    | Nombre del playbook que se quiere modificar. |
| data      | [Playbook](#playbook) |   :x:    | Nuevos datos del playbook.                   |

Respuesta:

| Parámetro | Tipo   | Descripción                                         |
| --------- | ------ | --------------------------------------------------- |
| ok        | bool   | Si la operación se ha ejecutado correctamente o no. |
| message   | string | Mensaje complementario al estado de la operación.   |



## DELETE /provision/playbook

Elimina un playbook.

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

