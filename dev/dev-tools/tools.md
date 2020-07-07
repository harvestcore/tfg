# Herramientas



## Arquitectura

Tradicionalmente el software ha tenido una arquitectura monolítica en la que todos los servicios y funcionalidades están integrados y programados en un mismo sistema. Estas por lo general tienen una modularidad reducida y presentan serios problemas a la hora de ampliar sus características. Un gran punto en contra de este tipo de arquitecturas es que a la hora de desplegar el software se tiene que hacer de forma completa, desplegando todo el sistema de nuevo.

Frente a esta arquitectura monolítica han surgido los microservicios, una arquitectura que intenta dividir todas aquellas partes de un sistema monolítico en pequeños subsistemas independientes y autónomos. La principal ventaja es que cada microservicio es la independencia, por lo que cada uno puede estar desarrollado en un lenguaje diferente del resto y el desarrollo y evolución es constante, ya que no se depende del despliegue de un gran sistema completo. La comunicación entre ellos se hace a través de APIs a través de protocolos como HTTP o HTTPS, por lo que aunque sean muy diferentes entre sí, el medio de comunicación es el mismo para todos.

Sus principales ventajas sobre la arquitectura monolítica son:

- Agilidad. No es necesario desarrollar todas las funcionalidades completas, por lo que se pueden reutilizar otros microservicios ya desarrollados para suplir las necesidades actuales.
- Modularidad. Cada microservicio es independiente del resto, lo que facilita el desarrollo y el despliegue de estos.
- Escalabilidad. Debido a la modularidad de estos la escalabilidad horizontal es asequible y muy beneficiosa.
- Seguridad y aislamiento. Cada uno de estos servicios encapsula toda su funcionalidad, quedando aislados del resto. Cualquier tipo de vulnerabilidad de la seguridad queda reducido a una parte del sistema general, evitando así pérdidas de información y posibles fallos a otros microservicios.

En cambio, también tiene desventajas. Tener multitud de servicios en ejecución conlleva una configuración y un coste de implantación más alto de lo habitual, además de que no hay una uniformidad a la hora de desempeñar un despliegue. Esto conlleva una complejidad añadida ya que aunque los servicios son mas ligeros y sencillos el sistema que conforman es mucho más complejo. La administración también es más compleja, ya que se requieren conocimientos específicos de cada microservicio para este cometido.



### Elección

En este caso la elección está bastante clara y opto por la arquitectura de microservicios. En el software que se desarrolla no tiene sentido un sistema monolítico en el que frontend y backend se encuentren juntos. En este caso las funcionalidades a desarrollar se centran en aspectos muy concretos y los beneficios de este tipo de arquitectura superan a los inconvenientes.

En primer lugar la modularidad, ya que el backend sería totalmente independiente del frontend, lo que permite que se puedan desarrollar infinitas interfaces de usuario, cada una adecuada al uso que se vaya a dar del sistema. Por otro lado la escalabilidad, en el caso de necesitar más instancias se pueden desplegar de forma rápida y sencilla; y finalmente la seguridad y aislamiento, ya que cada instancia del sistema no interviene con las demás, aislando en este caso los datos de cada caso de uso.



## Integración continua

La integración continua es una práctica que consiste en el control de versiones del código que se desarrolla y en la ejecución de pruebas automáticas del mismo de forma periódica con el fin de detectar errores o un mal funcionamiento de una forma rápida. Actualmente es un requisito necesario e indispensable en cualquier tipo de software y debe abordar todos los aspectos del mismo.

Estas pruebas deben ejecutarse cada vez que se haga una modificación del código para asegurar que el funcionamiento de este es correcto, por lo que la automatización de estas tareas es esencial. Esto mejora la calidad del software y nos permite controlar mejor lo que ocurre en este.

Existen multitud de servicios para este tipo de pruebas:

- Jenkins
- Travis CI
- Bamboo
- GitHub Actions
- GitLab CI
- Circle CI

Todos ellos comparten características y son realmente similares. Algunos como Jenkins permiten la integración de multitud de plugins y otros permiten además despliegues continuos. En el caso de este software la característica que más nos interesa es que sea gratuito y la mayoria de ellos lo son para proyectos de software libre. Esta es otra de las características que hacen que estos sistemas gratuitos tengan tanta popularidad.



### Elección

GitHub Actions es el sistema elegido para la integración continua. Esto se debe a dos motivos, el primero es que el proyecto se encuentra alojado en GitHub y por otro lado GitHub Actions permite el despliegue de contenedores Docker. Este último aspecto es muy importante en el software que se desarrolla, ya que debido a que el backend trabaja con este tipo de tecnología los tests unitarios deben probar todas estas funcionalidades. Además para las pruebas del resto de funcionalidades el poder ejecutar un contenedor con una base de datos facilita mucho el proceso de integración continua. Así mismo son sistemas que se encuentran perfectamente integrados el uno con el otro.



## Despliegue del software en contenedores

En este ámbito se va a utilizar Docker para desplegar tanto frontend como el backend. Este sistema provee una capa adicional de abstracción y de virtualización de las aplicaciones, lo que nos permite ejecutar un software de manera aislada sin tener que depender de complejas configuraciones de máquinas virtuales o hipervisores. Por otro lado, los recursos pueden ser también aislados.

Para la creación de estos contenedores se utilizan los denominados *Dockerfile*, que son archivos de texto plano con las diferentes instrucciones que crearán a voluntad el entorno de ejecución de nuestro software. En el caso de este proyecto se van a crear dos de estos archivos, para el frontend y otro para el backend y la creación y despliegue de las imágenes generadas se va a realizar mediante DockerHub.

Como se indica, este proceso también se puede automatizar, ya sea con scripts creados a mano o con el uso los hooks de DockerHub, que construyen las imágenes especificadas cada vez que se haga un cambio en el código o cada vez que se produzca un evento concreto.

Docker Compose es otra herramienta que facilita aún más este proceso, ya que a partir de un archivo YAML permite crear estos contenedores, configurarlos y conectarlos de una forma muy sencilla. En este proyecto también se incluye uno de estos archivos.

Finalmente, existen otras herramientas muy interesantes, como son Kubernetes, OpenShift o Mesos, que nos permiten orquestar y escalar los contenedores según los criterios que se configuren. En este proyecto no se hace uso de ellas, pero en el caso de que se quisiera dar un paso más en el despliegue del software podrían ser muy interesantes.



## Aprovisionamiento

Existen muchas herramientas que permiten el aprovisionamiento de sistemas, algunas más centradas en el ámbito Cloud y otras de uso local. Algunas de las más utilizadas son:

- Chef. Basado en Ruby y orientado a desarrolladores. La configuración de las máquinas se hace de forma procedural y se depende de un servidor central que almacene las configuraciones o *recetas*. Además ofrece análisis e informes de las máquinas aprovisionadas.
- Ansible. Escrito en Python y con SDK en este lenguaje. La principal ventaja de Ansible sobre el resto es que no necesita de un servidor maestro para funcionar ni tampoco que se instale algún tipo de software en las máquinas finales. Hace uso de *Playbooks*, los cuales son archivos en formato YAML que se ejecutan en orden. La conexión con los hosts los hace mediante SSH.
- Puppet. Es un conjunto de herramientas que permiten orquestar y administrar grandes conjuntos de máquinas. Al igual que Chef depende de un servidor central y permite ampliar su funcionalidad a través de módulos.



### Elección

En el ámbito de este software la opción que mejor encaja es Ansible. Debido a su sencillez de uso y de no requerir un servidor central lo hace ideal para el uso en el backend. Además, ya que se encuentra desarrollado en Python y a que existe un SDK, la integración es inmediata, solo teniendo que desarrollar las funcionalidades que se quieran.

Por otro lado la sencillez de los Playbooks lo hace más atractivo aún, ya que la sintaxis de los archivos YAML  es muy sencilla. En cuanto a la conexión mediante SSH solo se requiere que el backend tenga conexión a internet, por lo que no es necesario ningún protocolo o configuración adicional para que funcione.



## Backend

### Lenguaje de programación y framework

Actualmente existen multitud de lenguajes de programación que podrían usarse sin problema alguno para desarrollar una API de las características que se requieren. Una rápida investigación revela que los más usados para este cometido son los siguientes:

- Java
- JavaScript
- PHP
- Python
- Ruby
- C#
- Go

Aunque en este caso se usan para lo mismo existen bastantes diferencias entre todos ellos. Por un lado Java, C# y Go son lenguajes compilados, mientras que el resto son interpretados. Los primeros son más rápidos que los segundos, pero como principal inconveniente se encuentra el paso intermedio de compilado que hay que realizar previa ejecución del código. En cambio los lenguajes interpretados, por lo general, son más fáciles de comprender y están más orientados a facilitarle la vida al desarrollador.

La elección de un lenguaje u otro también depende de los recursos que nos ofrezca, esto es librerías, frameworks y todas aquellas características que hagan destacar un lenguaje sobre otro. También influye la experiencia que se tenga, ya que afrontar un gran proyecto con un lenguaje que nunca has usado puede dar un poco de miedo.

Los frameworks más usados en los lenguajes anteriores son:

**Java**. Destacan frameworks como Spring, el cual es muy ligero, se basa en una arquitectura MVC y es muy modular, lo que quiere decir que se puede usar para cualquier aspecto de un proyecto. También destaca Struts, muy similar al anterior basándose en MVC.

**JavaScript**. Express es el más utilizado y se ejecuta sobre Node.js. Es muy sencillo de utilizar, ya que la sintaxis que utiliza está muy simplificada. En cuanto a rendimiento, debido a lo ligero que es, no tiene casi impacto sobre el rendimiento de Node. Otros ejemplos son Sails o Meteor, incluyendo estos una curva de aprendizaje mayor y un rendimiento inferior.

**PHP**. Los más popular son Slim y Lumen. Ambos son microservicios bastante sencillos con muchas funcionalidades incorporadas, como autenticación, encriptado de datos, eventos y colas.

**Python**. En cuanto a microframeworks Flask es el más popular. Tiene una sintaxis muy sencilla y no intrusiva en el resto del código. También es muy customizable, existiendo gran cantidad de módulos para la definición de esquemas o mejora de sus funcionalidades básicas (como por ejemplo Flask-RESTplus, con el que se definen endpoints de forma muy sencilla haciendo uso de clases). Otro ejemplo es Django, similar a Spring u otros frameworks con arquitectura MVC.

**Ruby**. Roda y Sinatra son los más utilizados en Ruby. Estos, al igual que Flask en Python o Express en JS, tienen una sintaxis muy sencilla y que permiten crear una API en poco tiempo con pocas líneas de código.

**C#**. El más usado es .NET Core, de Microsoft y aunque la curva de aprendizaje es mayor que en los demás frameworks el rendimiento y las funcionalidades que ofrece son muy interesantes. Otro punto a tener en cuenta es la documentación tan extensa que tiene, ya que la sintaxis y la estructura que tiene es algo compleja.

**Go**. Tanto Revel como Gin son los más usados. Proveen de un marco de trabajo sencillo en el que el desarrollo de APIs es bastante minimalista. Por contra, carecen de algunas funcionalidades básicas, lo que implica que el desarrollador tiene que emplear tiempo extra en crearlas. Además no están pensados para entornos extremadamente grandes.



### Decisión

Las características deseadas que deberían ofrecernos estos lenguajes y frameworks en el caso de este software son sencillas aunque a la par difíciles de encontrar en ocasiones.

- Para el manejo de datos se requiere que se pueda conectar a MongoDB y esto lo cumplen los lenguajes mencionados, por lo que todos son buenos candidatos en este caso.
- En cuanto al aprovisionamiento se requiere algún tipo de SDK de Ansible. Los lenguajes que soportan esto son Go, Python, Ruby, PHP y JavaScript, mientras que el resto tienen un soporte limitado.
- Se debe poder administrar Docker y en este caso, al igual que con MongoDB, todos los lenguajes tienen SDKs disponibles.

Por otro lado, debido a la arquitectura del proyecto, no es necesario que el framework elegido tenga la arquitectura MVC, ya que de la vista se encarga el frontend. Por este motivo todos aquellos frameworks que siguen este modelo quedan descartados. Podrían utilizarse sin problema alguno, pero no tendría mucho sentido ya que no le estaríamos sacando todo el jugo a los mismos.

Anteriormente se mencionaba como aspecto importante los recursos que tienen estos lenguajes y cierto es que algunos pueden ofrecer más que otros, bien sea porque son más antiguos o bien porque son más usados y la comunidad es mayor. En esto destaca Python, también motivado por opinión personal, ya que existen una infinidad de librerías y recursos para este lenguaje y se puede desarrollar cualquier aplicación de forma sencilla e intuitiva. Además, en el caso del aprovisionamiento, Ansible está programado en Python, por lo que la integración con su SDK sería directa, sin problema alguno.

La ausencia de tipado en Python da una mayor flexibilidad y libertad a la hora de desarrollar, pero puede inducir a errores, por lo que es necesario tener un especial cuidado. Otro aspecto es que se trata de un lenguaje interpretado, algo que agiliza el desarrollo ya que no hay que emplear tiempo extra en el compilado. También tiene una sintaxis muy sencilla que facilita la comprensión del código.

En cuanto al framework, como se indicaba antes no es necesario que disponga de arquitectura MVC, por lo que Django queda descartado. En su defecto se usará Flask junto a otros módulos como Flask-RESTPlus o Marshmallow (usado para la definición de esquemas y validación de datos en los servicios).

Los tests unitarios se harán con Pytest, un framework para este tipo de pruebas muy ligero y potente, que además de permitir testear toda la funcionalidad de forma unitaria permite desplegar el backend para realizar pruebas a los servicios desarrollados.





## Frontend

En la actualidad la cantidad de frameworks y librerías para desarrollar un frontend es muy extensa y está en constante avance. Tradicionalmente este tipo de desarrollo estaba compuesto por el *stack* HTML/CSS/JS, en el que el desarrollador se encarga de todos los aspectos y, aunque no va a desaparecer, esta siendo en parte desplazado por la aparición de nuevos frameworks y librerías.

Estos facilitan mucho el trabajo del programador, ya que incorporan funcionalidades que de ser creadas de cero implicarían una cantidad de tiempo y trabajo considerable.

Los que mas destacan en cada ámbito son los siguientes:

#### Librerías

**React**. Tiene un enfoque reactivo y trabaja con un DOM virtual en varias capas, lo que permite que sólo se actualicen aquellas partes de la página que deban actualizarse. También permite la creación y reutilización de componentes personalizados, lo que dota a esta librería de mucha flexibilidad a la hora del desarrollo. Por contra sólo se trata de una librería centrada en la parte visual del frontend, por lo que el manejo de datos entre componentes o cualquier tipo de comunicación externa, como HTTP, quedan a cargo del desarrollador.

**Vue**. En este caso Vue comparte conceptos de React y de Angular, por lo que sería el punto intermedio entre ambos. Destaca por ser mas liviano que estos y por su simplicidad a la hora del desarrollo, lo que hace que la curva de aprendizaje sea bastante menor. Por el contrario, al igual que con React, las comunicaciones corren a cargo del programador, lo que es un punto en su contra.



#### Frameworks

**Angular**. Es un framework que aborda todos los aspectos del desarrollo frontend, desde la parte visual hasta las comunicaciones. Su arquitectura se basa en componentes que se pueden crear y personalizar a voluntad y el lenguaje usado para su desarrollo es TypeScript, lo cual permite un mayor control de los datos que se manejan. Integra además multitud de librerías, como RxJS, para aprovechar sus virtudes. Entre sus principales características destacan el enlace de datos bidireccional (*2-way data-binding*) entre el modelo y la vista, la inyección de servicios y dependencias, que facilita el desarrollo y la comprensión del código, y la validación de datos y mecanismos de seguridad integrados. Por contra la curva de aprendizaje es mas grande, ya que integra multitud de conceptos diferentes que no se contemplan en las demás soluciones.



### Elección

En el caso de este software la primera elección que se toma es la de abandonar el *stack* HTML/CSS/JS ya que realmente no ofrece nada novedoso sobre las demás soluciones. Por otro lado queda decidir si tomar un rumbo más abierto, eligiendo alguna librería, o uno más cerrado, eligiendo Angular como framework.

En cuanto a React y Vue, aunque es muy interesante el enfoque que tienen, se quedan cortas a la hora de la comunicación con el backend. El desarrollador es el que debe proveer de los métodos de comunicación, lo que requiere más tiempo. En cambio con Angular esos aspectos ya se encuentran integrados, lo que simplifica mucho el proceso. Por otro lado aspectos como el *2-way data-binding* y la validación de datos son también interesantes, ya que aportan flexibilidad y agilizan el desarrollo.

Por estos motivos Angular es la mejor solución en el caso de este software y, en caso de quedarse corta en algunos aspectos, permite la integración de otras librerías. Además Angular incluye librerías y mecanismos para tests unitarios e integración continua, algo muy necesario en el desarrollo de un software.

Finalmente, para los test unitarios y end-to-end (e2e) se van a utilizar herramientas que se integran perfectamente con Angular. Para los primeros se utiliza Karma, que viene incluido por defecto en el framework y permite comprobar el funcionamiento unitario de cada uno de los componentes. Para los tests e2e se utilizará Cypress, una herramienta gratuita muy potente que permite realizar tests al frontend como si de un usuario se tratara, haciendo uso de datos sobre las diferentes funcionalidades del sistema.



## Base de datos

Elegir un sistema de gestión de base de datos es una de las decisiones más importantes a la hora de diseñar y desarrollar un software. Existe una gran variedad de tipos de bases de datos y hay que tener en cuenta una serie de cuestiones que serán determinantes a la hora de elegir un tipo u otro. Algunos de estos son:

**SQL**. Este tipo de bases de datos se basan en las relaciones entre los datos. Estos se introducen en registros y luego se organizan por tablas, columnas y tuplas, permitiendo relacionarlos de manera sencilla. El principal lenguaje de consultas es el *Standard Query Language* (SQL), el cual esta compuesto por una serie de comandos de diferentes tipos, que se usan para unos cometidos u otros. Estos son *Data Definition Language*, *Data Query Language*, *Data Manipulation Language*, *Data Control Language* y *Transaction Control Language*. Sus principales características son el esquema rígido que se define previo al uso que garantiza el esquema ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad).

Algunos ejemplos son:

- Bases de datos relacionales. Como MySQL, Oracle o Access de Microsoft.
- Bases de datos multidimensionales. Se asemejan mucho a las anteriores, la diferencia se encuentra en que los atributos de las tablas pueden tener dos tipos.



**NoSQL**. La principal característica de estos sistemas es que no usan SQL como lenguaje para realizar consultas. Los datos no se almacenan ni organizan en tablas ni se garantiza el esquema ACID pero sí destacan por su gran escalabilidad horizontal, pueden manejar cantidades enormes de datos y no generan cuellos de botella. Algunos ejemplos son:

- Bases de datos clave-valor. Utiliza un modelo muy similar a una tabla hash, pero con la característica de que cada elemento tiene una serie de atributos asociados. Como Cassandra, BigTable o Redis.
- Bases de datos orientadas a objetos. La información es representada mediante objetos, como si de objetos en programación se tratasen. La principal ventaja es que los datos de este tipo de sistemas aparece directamente como objetos en el lenguaje de programación, por lo que la integración es alta. Ejemplos son ObjectDB o ZooDB.
- Bases de datos en grafos. En este caso la información se almacena en grafos, los cuales están compuestos por nodos (entidades), aristas (relaciones entre nodos) y la información como tal. Este tipo de base de datos es indicada en el caso de que las consultas requiran tomar datos de diferentes nodos. Ejemplos: Neo4j, InfoGrid o AllegroGraph.
- Bases de datos documentales. Se caracterizan por su semiestructura, en la que no se define de forma previa un esquema robusto, sino que el modelado es flexible. Almacenan toda la información en documentos de texto plano, XML o JSON. Algunos ejemplos son MongoDB, CouchDB o RavenDB.



#### SQL vs NoSQL

Cada tipo de base de datos tiene unas ventajas e invenientes que destacan sobre el otro. El siguiente cuadro resume sus principales características:

| SQL                                             | NoSQL                           |
| :---------------------------------------------- | :------------------------------ |
| Esquema rígido predefinido                      | Esquema dinámico                |
| Adecuadas para consultas o relaciones complejas | Muy rápida en consultas simples |
| Escalabilidad vertical                          | Escalabilidad horizontal        |
| Garantiza ACID                                  | Flexibiliza el esquema ACID     |
| Uso de lenguaje de consultas SQL                | Búsqueda clave-valor            |



### Elección

Una vez contemplados y comprendidos los diferentes tipos de bases de datos que existen se debe de decidir cual elegir. Por las características del software a desarrollar queda excluído el tipo SQL, ya que el tipo de datos que se va a manejar no requiere de grandes relaciones entre ellos y además el esquema puede ser cambiante. Podría ocurrir que ciertos valores no se encontraran almacenados, bien porque no son necesarios o bien porque el usuario decide no insertarlos, por lo que sería mantener una estructura que no se está cumpliendo.

Por otro lado el tipo de consultas que se van a realizar no son extremadamente complejas. Los datos manejados no tienen relaciones entre sí y las consultas serían realmente básicas. Otro punto a favor en este aspecto para las bases de datos NoSQL es la velocidad a la hora de realizar las consultas.

En el caso de la integración con el software, en las bases de datos SQL se utilizan los llamados ORM (Object Relation Mapper). Estos permiten realizar consultas a estas bases de datos de una forma más amigable en el lenguaje que se esté usando, lo que implica que se tenga que volver a redefinir el esquema para poder manejar estos datos. En cambio con NoSQL esta integración suele ser mas sencilla, al utilizarse directamente objetos como diccionarios.

Dentro de las bases de datos NoSQL existen diferentes tipos, como se menciona anteriormente. En el caso de este software el modelo que mas encaja es el documental, en la que una semiestructura flexible almacenada en forma de documentos es ideal. MongoDB es una gran elección, ya que los datos se almacenan en BSON (Binary JSON), lo que ofrece aún más flexibilidad a la hora de almacenar objetos. También permite crear índices en cualquier clave y el balanceo de carga en el caso de realizar grandes cantidades de consultas simultáneas.

Actualmente también están destacando las bases de datos en la nube o DBaaS (DataBase as a Service), las cuales estan optimizadas para operaciones en entornos virtualizados. La principal característica de estos servicios es que se suele pagar por el uso de almacenamiento y además conceptos como la escalabilidad o la alta disponibilidad estan asegurados. En el caso de MongoDB existe **Atlas**, que incluso ofrece planes gratuitos. Otro ejemplo de DBaaS sería **mLab**, muy similar al anterior pero con una configuración más sencilla. Para el desarrollo de este software este aspecto es muy interesante, ya que al tratarse de un microservicio el no estar atado a una base de datos local permite que se pueda desplegar tambien en cloud.
