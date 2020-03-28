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
 docker run -e MONGO_HOSTNAME=172.17.0.3 harvestcore/ipm-backend:<tag>
```

