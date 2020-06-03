# Variables de entorno

IPManager necesita algunas variables de entorno para funcionar correctamente. Todas tienen un valor por defecto, aunque se recomienda que se revisen y se modifiquen antes de comenzar a usar tanto backend como frontend.

## Backend

Estas variables se pueden configurar como variables de entorno o se pueden configurar directamente en `config/server_environment.py`.

- `MONGO_HOSTNAME` Hostname donde se encuentra el host de MongoDB. Por defecto `127.0.0.1`
- `MONGO_PORT` Puerto del host de MongoDB. Por defecto `27017`.
- `TESTING_DATABASE` Nombre de la colección usada para ejecutar los tests unitarios. Por defecto `ipm_root_testing`.
- `BASE_DATABASE` Nombre de la colección base de IPManager. En esta colección se almacenan datos de los clientes del backend. Por defecto toma el valor que tenga la variable `TESTING_COLLECTION`.
- `ENC_KEY` Clave usada para encriptar las contraseñas. Puedes generar una clave ejecutando el archifo `generate_key.py` que se encuentra en `utils`. Por defecto se usa una aleatoria.
- `JWT_ENC_KEY` Clave usada para encriptar los JWT usados en el login. Puedes generar una clave ejecutando el archifo `generate_key.py` que se encuentra en `utils`. Por defecto se usa una aleatoria.
- `DOCKER_BASE_URL` URL o path donde se encuentra el socket de Docker. Por defecto `unix://var/run/docker.sock`.
- `DOCKER_ENABLED` Activa o desactiva los endpoints para gestión de servicios. Por defecto comprueba si el backend se está ejecutando en un Docker para desactivarlos en caso afirmativo.
- `ANSIBLE_PATH` Path relativo o absoluto donde se van a almacenar los diferentes archivos generados por el backend necesarios para el aprovisionamiento. Por defecto `./`.



## Frontend

El frontend cuenta con dos variables de entorno que se tienen que configurar previamente, son:

- `backendUrl` URL del backend sin protocolo.
- `httpsEnabled` True si el backend cuenta con HTTPS, false en caso contrario.

La configuración de estas variables se puede hacer de dos maneras:

- En los archivos environment.*.ts que se encuentran en `fronend/src/environments`. Estos archivos una vez configurados son inmutables una vez se ha construido el frontend.

  - `environment.on-premise.ts` Entorno utilizado para construir la imagen de Docker. Por defecto se utilizan los valores usados en el docker-compose.
  - `environment.prod.ts` Entorno utilizado para construir una versión de producción.

- En el archivo `env.js`. Este archivo se encuentra en `fronend/src/` y se puede modificar sin tener que reconstruir el frontend. En caso de no necesitar esta característica se recomienda utilizar el environment anterior. El archivo tiene la siguiente forma:

  ```javascript
  (function (window) {
    // window.__env = {
    //   backendUrl: '172.20.0.3:5000',
    //   httpsEnabled: false
    // };
  }(this));
  ```