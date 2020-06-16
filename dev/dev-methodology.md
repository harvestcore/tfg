# Metodología de desarrollo

Como bien se indicaba [aquí](doc.md) existen diferentes metodologías de desarrollo de software y como también se mencionaba se pueden diferenciar dos grandes tipos: ágiles y tradicionales. En este documento se defininen las principales metodologías existentes, sus pros y contras y finalmente se justifica la metodología elegida a la hora de desarrollar este proyecto.



[TOC]

## Metodologías tradicionales

Estas metodologías surgieron cuando aparecieron los primeros sistemas software y están caracterizadas por tener una fuerte planificación al comienzo del desarrollo. Por lo general se centran además en la documentación exhaustiva del proyecto y suelen ser llevadas a cabo por equipos compuestos por multitud de desarrolladores.

Sus etapas o ciclo de vida generalizado sería el siguiente, aunque siempre abierto a pequeños cambios:

1. **Inicio**

   Se establecen los objetivos y resultados esperados del proyecto. Se intenta encontrar las posibles dificultades u obstáculos.

2. **Planificación**

   Se planifica, estima y presupuesta el desarrollo del sistema.

3. **Desarrollo**

   En esta etapa se produce todo el desarrollo del producto y se lleva una evaluación cada cierto tiempo del mismo. Por otro lado se realiza la extensa documentación del software.

4. **Control de calidad**

   Se realizan controles de calidad del software, del entorno y se revisa toda la funcionalidad del producto previa entrega al cliente.

5. **Finalización**

   Se finaliza el proyecto entregando el software resultante al cliente y se redacta un informe final.



Como se observa, este tipo de metodologías tiene una estructura lineal, en la que al principio se acuerdan las características que debe tener el software y no se modifican durante el desarrollo del sistema, y finalmente se entrega el producto sin dar lugar a cambios. Esto crea una gran dependencia y presión inicial en el cliente, ya que tiene que tener gran dominio del problema y debe tener en cuenta multitud de aspectos. Por otro lado, durante el desarrollo, no se tiene una especial comunicación con el cliente.



### Ventajas

- Objetivos claros y concisos.
- Sencillo, al seguir unas pautas intuitivas.
- Seguimiento en cada una de sus fases.

### Inconvenientes

- Costes elevados.
- No se permiten cambios durante el desarrollo.
- El producto solo se entrega al final, por lo que suele resultar un proceso más lento.



### Ejemplos

#### Microsoft Solution Framework (MSF)

MSF agrupa una serie de buenas prácticas en cuanto al desarrollo de software que se adaptan a los diferentes proyectos. Este framework separa el proyecto en 5 procesos muy similares a los mencionados anteriormente, y son: visión, planificación, desarrollo, estabilización y despliegue.



#### Rational Unified Process (RUP)

RUP aglutina una serie de metodologías adaptables al proyecto a desarrollar y se basa en seis principios clave:

- Adaptar el completo desarrollo del software a las necesidades del cliente.
- Priorización y equilibrio de las tareas.
- Comunicación y colaboración entre equipos de desarrollo.
- Entregas paulatinas tras la finalización de etapas de desarrollo.
- Abstracción del problema.
- Calidad del producto.

Muchas de estas claves coinciden con las de las metodologías ágiles (las cuales se explican más adelante), pero este tipo de procedimientos pierde fuerza al cerrarse no permitiendo cambios. 

Por otro lado, su ciclo de vida es similar al de MSF, pero con una fase menos. Éstas son:

- Iniciación.
- Elaboración.
- Construcción.
- Transición.





## Metodologías ágiles

Las metodologías ágiles responden al cambio y producen y entregan el software cada cierto tiempo. Además potencian la relación directa con el cliente como clave para el éxito del desarrollo. Éstas han triunfado por su velocidad, flexibilidad y capacidad de colaboración, retroalimentación y entregas paulatinas al finalizar un periodo de tiempo preestablecido. Por otro lado dan mas importancia al resultado final del producto que a su documentación, aunque no es algo mandatorio.

Con esto se consigue ahorrar tiempo y costes, trabajando de forma más rápida y eficiente, lo que permite cumplir los contratos establecidos en el desarrollo de un proyecto software.

Se podrían enunciar unos principios básicos de este tipo de metodologías, son los siguientes:

- Entregas del software funcional con frecuencia.
- Satisfacción del cliente.
- Motivación de los equipos implicados.
- Simplicidad y orden de las tareas a desarrollar.
- Buena comunicación entre cliente y equipos de desarrollo.



### Ventajas

- Permiten cambios durante el desarrollo.
- Flexibles.
- Resultados funcionales con frecuencia.
- Clientes satisfechos.

### Inconvenientes

- Una comunicación no acertada puede inducir a errores y retardos en el tiempo de entrega.
- Costos de desarrollo variables, al depender de los cambios realizados.



### Ejemplos

Por lo general todas las metodologías ágiles siguen los mismos principios, aunque tienen ligeras variaciones para potenciar unos aspectos frente a otros. Algunos ejemplos son los siguientes.

#### Extreme Programming (XP)

XP se centra principalmente en la relaciones entre los integrantes implicados en el desarrollo del producto, en la retroalimentación entre desarrolladores y cliente y en la afrontación de los cambios propuestos de una forma certera. Por otro lado evita el desarrollo de aquellas funcionalidades que realmente no son necesarias en un momento preciso, evitando pérdidas de tiempo, aunque también se centra en el aprendizaje de los desarrolladores. Además la planificación y las pruebas del software son continuas.

Tiene cuatro fases en el desarrollo de un producto software. Son las siguientes:

- Planificación con el cliente.
- Diseño.
- Desarrollo del software.
- Pruebas del software.



#### Scrum

Scrum tiene características similares a XP, pero la diferencia más significativa es que la principal estrategia es el desarrollo incremental, en lugar de una planificación completa del software al inicio del proyecto. En esta metodología existen tres roles: Product Owner (PO), Scrum Master (SM) y los desarrolladores. En el caso de un proyecto pequeño como es el que engloba este TFG, la misma persona tiene los tres roles a la vez.

Lo interesante de Scrum es la forma de dividir el proceso de desarrollo del software. Para ello se usan *sprints*, los cuales son un periodo de tiempo (variables) en el que se planifican tareas, se desarrollan y luego se entregan de forma funcional. Esto permite entregas paulatinas del software, un feedback contínuo y un desarrollo más dinámico por parte de todos los implicados en el mismo.

Al comienzo de los *sprints* se planifican las tareas que se van a realizar en el mismo. Estas tareas se extraen del *backlog*, que es el listado total de tareas que se tienen que realizar para completar el software. Una vez extraídas las tareas se compone el sprint, ordenando dichas tareas por prioridad. Por otro lado se pone una meta que se debe alcanzar al finalizar el sprint. Además se tienen reuniones diarias con todos los integrantes del desarrollo para comentar lo que se ha hecho el día anterior, lo que se va a hacer hoy y los posibles problemas que hayan surgido. Una vez finalizado el sprint se produce otra reunión para valorar el transcurso y resultados.



#### Kanban

Es una metodología que utiliza tarjetas para simbolizar las tareas que se tienen que realizar en el desarrollo de un software. Estas tarjetas se utilizan en un tablero dividido por columnas, las cuales simbolizan tareas que no se han empezado aún, tareas que estan en progreso, ya terminadas, etc.

De esta manera se ve de manera rápida y visual lo que se esta haciendo en un proyecto en un momento dado. También evita distracciones y problemas, ya que cada persona se centra sólo en las tareas que tenga asignadas, dejando saber al resto a lo que dedida su tiempo.

Por otro lado también fomenta el feedback y las reuniones entre integrantes, lo que facilita también el proceso de desarrollo del software.



## Conclusión

Por los diferentes motivos expuestos anteriormente, en este proyecto voy a utilizar una mezcla de dos metodologías ágiles: Scrum y Kanban.

En primer lugar porque Scrum agrupa todas las buenas prácticas de las metodologías ágiles, y si bien en mi caso estoy algo más limitado al ser Product Owner, Scrum Master y desarrollador al mismo tiempo, la organización es muy atractiva en este tipo de proyectos. La división por sprints hace que cada dos semanas (tiempo que estimo mínimo y suficiente para un sprint completo) se tenga un conjunto de funcionalidades nuevas. Por otro lado, las reuniones diarias son conmigo mismo (y en ocasiones con el tutor, las cuales pueden solucionar problemas que surjan), lo que permite que me organice mejor y sepa qué hacer cada día.

En cuanto a Kanban, pienso que la organización visual de las tareas es bastante provechosa, pues dicha visualización permite saber las tareas que son más urgentes o el estado en el que se encuentran. GitHub cuenta con una herramienta llamada *Proyectos* que ofrece un tablero Kanban para la organización de tareas y además integración con las *issues* y *pull requests* que se van creando en el proyecto, algo que pienso que es beneficioso para el desarrollo del proyecto y que voy a usar durante el desarrollo del mismo.





## Referencias

https://www.ecured.cu/Metodologias_de_desarrollo_de_Software

https://obsbusiness.school/es/blog-project-management/metodologia-agile/que-son-las-metodologias-de-desarrollo-de-software

https://blog.workep.com/es/metodologias-de-gestion-de-proyectos-tradicional-vs-agil

https://www.cleanpng.com/png-microsoft-solutions-framework-information-technolo-5829507/preview.html

https://es.wikipedia.org/wiki/Proceso_Unificado_de_Rational

[https://es.wikipedia.org/wiki/Metodolog%C3%ADa_de_desarrollo_de_software](https://es.wikipedia.org/wiki/Metodología_de_desarrollo_de_software)

https://www.iebschool.com/blog/que-son-metodologias-agiles-agile-scrum/

https://en.wikipedia.org/wiki/Extreme_programming

https://www.wearemarketing.com/es/blog/metodologia-scrum-que-es-y-como-funciona.html

https://kanbanize.com/es/recursos-de-kanban/primeros-pasos/que-es-kanban

https://es.wikipedia.org/wiki/Kanban_(desarrollo)

