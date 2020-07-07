# Status

## GET /status

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