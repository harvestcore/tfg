# Juju

- ¿Qué hace?
Herramienta de gestión de orquestación de servicios que permite desplegar, configurar, escalar y operar con infraestructuras cloud.

  - Modela de forma sencilla despliegues software que pueden ser bastante complejos. (Se centra bastante en este aspecto).
  - Encapsula en componentes reutilizables.
  - Existen "Charms", que describe como se instala, configura y opera un sistema.
  - Estos "Charms" simplifican la "típica" configuración que se podría hacer con Fabric, Ansible o Chef.
  - Los modelos se describen en un archivo YAML, el cual puede contener tambien detalles concretos del despliegue de cada servicio (instancias, config, etc).
  - Tiene CLI/UI.
  - Fácil actualización de la configuración.
  - Buena integración de actualizaciones de software.
  - Buena integración con sistemas cloud (AWS, Microsoft Azure, Google Cloud, OpenStack, Oracle Cloud, Joyent).
  - Soporta contenedores (LXD, Kubernetes)
  - Soporta bare metal (MAAS)
  - Soporta máquinas virtuales.
  - Automatización de tareas (despliegue, escalado, etc).
  - Es Open Source.

- ¿Lenguaje de programación?

Juju tiene clientes para diferentes lenguajes de programación (como Go), pero está orientado a usarse con su CLI.

- ¿Es útil para el proyecto?

En parte podría ser útil pues soluciona los problemas que propone el proyecto, pero para el cometido que se requiere no se puede usar para desarrollar una infraestructura como código.

- Pros:
  - Gran integración con multitud de sistemas.
  - OpenSource
  - Fácil configuración.

- Cons:
  - Por ahora ninguno

- Links:

[https://jaas.ai/how-it-works](https://jaas.ai/how-it-works)
