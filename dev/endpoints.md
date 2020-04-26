# Endpoints

## Autenticación
- POST /api/login
- POST /api/logout



## Usuarios
- GET /api/user/`username`
- POST /api/user
- POST /api/user/query
- PUT /api/user
- DELETE /api/user



## Aprovisionamiento

- GET /api/provision
- GET /api/provision/hosts/`name`
- POST /api/provision/hosts/query
- PUT /api/provision/hosts
- POST /api/provision/hosts
- DELETE /api/provision/hosts
- GET /api/provision/playbook/`name`
- POST /api/provision/playbook/query
- PUT /api/provision/playbook
- POST /api/provision/playbook
- DELETE /api/provision/playbook



## Despliegue
- POST /api/deploy/container
- POST /api/deploy/container/single
- POST /api/deploy/image
- POST /api/deploy/image/single



## Status

- GET /api/status



## Máquinas

- GET /api/machine/`name`
- POST /api/machine
- POST /api/machine/query
- PUT /api/machine
- DELETE /api/user