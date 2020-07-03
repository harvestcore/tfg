# Aprovisionamiento

## POST /provision

Ejecuta un playbook.

Cabeceras necesarias:

| Nombre         | Opcional | Descripción      |
| -------------- | :------: | ---------------- |
| x-access-token |   :x:    | Token de acceso. |

Cuerpo de la petición (JSON):

| Parámetro | Key         | Tipo         |      Opcional      | Descripción                                                  |
| --------- | ----------- | ------------ | :----------------: | ------------------------------------------------------------ |
| hosts     |             | list[string] |        :x:         | Lista de grupo de hosts donde se quiere ejecutar el playbook. |
| playbook  |             | string       |        :x:         | Nombre del playbook a ejecutar.                              |
| passwords |             | dict         |        :x:         | Contraseñas necesarias para la conexión a los hosts.         |
|           | conn_pass   | string       | :heavy_check_mark: | Contraseña de acceso.                                        |
|           | become_pass | string       | :heavy_check_mark: | Contraseña para acceder al root.                             |

Respuesta:

| Parámetro | Tipo   | Descripción                             |
| --------- | ------ | --------------------------------------- |
| result    | string | Respuesta de la ejecución del playbook. |