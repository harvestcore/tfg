# Primeros pasos

## Inicialización de BD

Una vez instalado el backend puedes ejecutar un script llamado `init_database.py`, el cual creará un usuario en el cliente base. Este usuario es administrador y sus credenciales deben ser cambiadas una vez haya sido creado.

El cliente base viene denominado por el nombre de la base de datos principal, el cual se toma de la variable de entorno `BASE_DATABASE` (toma valor `ipm_root` en caso de no encontrarse configurada).

Tras crear este primer usuario administrador, este puede comenzar a crear otros usuarios o clientes usando la API o el CLI.



## CLI

El CLI que se incluye en el directorio raíz del backend permite realizar algunas operaciones con clientes (o *customers*) y usuarios. Se puede ejecutar con:

```bash
cd backend

python3 cli.py
```

Es interactivo y permite:

- Crear un cliente (o *customer*).
- Activar un cliente (o *customer*).
- Desactivar un cliente (o *customer*).
- Agregar un usuario a un cliente (o *customer*).

Internamente utiliza la configuración de las [variables de entorno](env-vars.md) que se encuentre establecida en el momento de utilizar el CLI.



### Rationale

Existen multitud de librerias y frameworks 