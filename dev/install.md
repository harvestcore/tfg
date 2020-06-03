## Instalación

Una vez clonado el repositorio puedes instalar y ejecutar tanto backend como frontend siguiendo los pasos que se describen a continuación.

### Backend

El backend de IPManager tiene algunas dependencias que tienes que instalar para que funcione correctamente, son las siguientes:

```bash
apt install sshpass
apt instal openssl
apt install libffi6

pip3 install -r requirements.txt
```

Asegúrate que la versión instalada del paquete `werkzeug` coincide con `0.16.1`.

Para ejecutarlo puedes hacerlo mediante Flask o con Gunicorn.

- Flask (no recomendado):

  ```bash
  export FLASK_APP=wsgi.py
  flask run
  ```

- Gunicorn:

  ```bash
  gunicorn -b 0.0.0.0:5000 wsgi:app
  ```



#### Docker

El backend también está disponible en Docker, puedes descargarte la imagen de la siguiente manera:

```bash
docker pull harvestcore/ipm-backend:<tag>
```

Se recomienda siempre utilizar la última versión disponible de la imagen, la cual puede consultarse [aquí](https://github.com/harvestcore/tfg/releases) o [aquí](https://hub.docker.com/r/harvestcore/ipm-backend/tags). Revisa también las [variables de entorno](./env-vars.md) necesarias para ejecutar el backend.

Ejemplo de ejecución:

```bash
 docker run -e MONGO_HOSTNAME=172.20.0.2 harvestcore/ipm-backend:<tag>
```

Si por el contrario quieres construir tú mismo la imagen, ejectuta:

```bash
cd backend

docker build .
```





### Frontend

Para instalar el frontend primero revisa y configura las [variables de entorno](./env-vars.md), tras eso solo tienes que ejecutar lo siguiente:

```bash
cd frontend

// Construir el frontend
npm build --prod
```

Para ejecutarlo se recomienda utilizar Nginx u otro tipo de servidor web. En la raíz del frontend se adjunta el archivo de configuración (`nginx.conf`) usado para construir la imagen de Docker, y puede ser usado.



#### Docker

Puedes ejecutar el frontend con Docker, para ello puedes bajarte la imagen del repositorio disponible o puedes construir y ejecutar tu mismo la imagen.

```bash
docker pull harvestcore/ipm-frontend:<tag>
```

El tag o versión lo puedes consultar [aquí](https://github.com/harvestcore/tfg/releases) o [aquí](https://hub.docker.com/r/harvestcore/ipm-backend/tags). Se recomienda usar siempre la última versión estable, las versiones *latest* pueden contener bugs.

```bash
cd frontend

// Construir imagen
docker build . -t ipm-frontend:<tag>

docker run ipm-frontend:<tag>
```



### Docker-compose

En el caso de utilizar el docker-compose que se encuentra en la raíz del repositorio solo es necesario ejecutar lo siguiente:

```bash
// Construir imágenes
docker-compose build

// Ejecutar imágenes
docker-compose up
```

Por supuesto se pueden agregar variables de entorno para configurar el backend. Un ejemplo sería:

```bash
docker-compose up -e BASE_DATABASE=ipm_root
```

El docker-compose tiene configurada una red bridge con la siguiente subnet:

- `172.20.0.0/16`

Por otro lado las máquinas cuentan con las siguientes direcciones IP estáticas asignadas:

- mongo: `172.20.0.2`
- ipmanager-backend: `172.20.0.3`
- ipmanager-frontend: `172.20.0.4`

También se fija la variable de entorno `BASE_DATABASE` con valor `ipm_root`.