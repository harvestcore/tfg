# Herramientas



## Arquitectura

Microservicio



## Integración Contínua



## Backend

### Lenguaje de programación

Actualmente existen multitud de lenguajes de programación que podrían usarse sin problema alguno para desarrollar una API de las características que se requieren. Una rápida investigación revela que los más usados para este cometido son los siguientes:

- Java
- JavaScript
- PHP
- Python
- Ruby
- C#
- Go



Aunque en este caso se usan para lo mismo existen bastantes diferencias entre todos ellos. Por un lado Java, C# y Go son lenguajes compilados, mientras que el resto son interpretados. Los primeros son más rápidos que los segundos, pero como principal inconveniente se encuentra el paso intermedio de compilado que hay que realizar previa ejecución del código. En cambio los lenguajes interpretados, por lo general, son más fáciles de comprender y están más orientados a facilitarle la vida al desarrollador.

La elección de un lenguaje u otro tambien depende de los recursos que nos ofrezca, esto es librerías, frameworks y todas aquellas características que hagan destacar un lenguaje sobre otro.

En el caso 





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

Por estos motivos Angular es la mejor solución en el caso de este software y, en caso de quedarse corta en algunos aspectos, permite la integración de otras librerías. Además Angular incluye librerías y mecanismos para tests unitarios e integración contínua, algo muy necesario en el desarrollo de un software.



## Base de datos

Elegir un sistema de gestión de base de datos es una de las decisiones más importantes a la hora de diseñar y desarrollar un software. Existe una gran variedad de tipos de bases de datos y hay que tener en cuenta una serie de cuestiones que serán determinates a la hora de elegir un tipo u otro. Algunos de estos son:

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

