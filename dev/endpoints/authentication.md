# Autenticación

## GET /api/login

Loguea al usuario en el cliente.

Cabeceras necesarias:

| Nombre     | Opcional | Descripción                                   |
| ---------- | :------: | --------------------------------------------- |
| Basic Auth |   :x:    | Basic Auth compuesto por usuario y contraseña |

Respuesta:

| Parámetro | Tipo   | Descripción                                      |
| --------- | ------ | ------------------------------------------------ |
| token     | string | Token JWT utilizado para identificar al usuario. |



## POST /api/logout

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

