# Sprint 1

Cada integrante desarrollará un microservicio utilizando el lenguaje que sea de mejor utilidad para cada uno, al igual que cada uno desarrollará su base datos Relacional, esa característica de la BD será utilizada en todos los microservicios, a futuro agregaremos más microservicios, la lista de los que desarrollaremos es la siguiente:

- **Microservicio de Estado Físico Miguel Mora**
1. Base de Datos Relacional: Ideal para almacenar datos estructurados como el historial de peso, altura, y signos vitales, donde las relaciones entre las tablas (como bebé -> registros de mediciones) son importantes.

2. Entrada Manual: Una aplicación móvil o web que permite a los padres registrar manualmente el estado del bebé (por ejemplo, dormido, despierto, comiendo, etc.). Estos datos pueden ser enviados a un API para almacenamiento y análisis.

3. Backend: Utilizar un framework como Flask o FastAPI en Python para crear el backend del microservicio. Este servicio puede recibir datos de dispositivos o entradas manuales y almacenarlos en una base de datos.

4. Desarrollar una aplicación móvil/web para que los padres ingresen el estado del bebé.

------------

- **Microservicio de Alimentación Alejandro Esparza**
1. Base de Datos Relacional:
Utiliza una base de datos relacional para gestionar información estructurada relacionada con la alimentación del bebé, como registros de ingesta, horarios de comida, y preferencias alimenticias. Las tablas deben reflejar las conexiones entre distintos tipos de datos, como las comidas consumidas y los horarios de las tomas.

2. Registro Manual:
Implementa una aplicación móvil o web que permita a los padres ingresar manualmente detalles sobre la alimentación y el estado del bebé, como si ha comido, si está despierto o dormido. Estos registros pueden ser enviados a una API para su almacenamiento y análisis posterior.

3. Desarrollo del Backend:
Desarrolla el backend del microservicio utilizando frameworks en Python. Este backend debe ser capaz de recibir datos desde dispositivos de seguimiento o entradas manuales, procesarlos y almacenarlos en la base de datos relacional para su gestión y análisis.

4. Aplicación para Padres:
Crear una aplicación móvil o web que facilite a los padres la entrada de datos sobre la alimentación y el estado del bebé. La aplicación debe permitir una interfaz intuitiva para registrar la información y sincronizarla con el backend del microservicio.


------------

- **Microservicio de Sueño Uriel Beltrán**
1. Base de Datos Relacional: Útil para llevar un registro detallado y estructurado de los patrones de sueño, con relaciones claras entre las entradas de sueño y el bebé correspondiente.


2. Modelado de la Base de Datos

Bebé (baby)
ID (Primary Key)
Nombre
Fecha de nacimiento
Datos adicionales (padres, grupo sanguíneo, etc.)
Patrón de Sueño (sleep_pattern)
ID (Primary Key)
ID del Bebé (Foreign Key)
Fecha
Hora de inicio del sueño
Hora de fin del sueño
Observaciones (e.g., inquieto, tranquilo, etc.)
Esto permite establecer relaciones claras entre cada entrada de sueño y el bebé correspondiente.

3. Endpoints del Microservicio
Crear Bebé: Endpoint para registrar un nuevo bebé en la base de datos.
Registrar Patrón de Sueño: Endpoint para registrar una nueva entrada de sueño asociada a un bebé específico.
Obtener Patrones de Sueño por Bebé: Endpoint para obtener todos los patrones de sueño de un bebé en particular.
Actualizar o Eliminar Entradas: Endpoints para modificar o eliminar registros existentes.

4. Tecnologías y Herramientas
Base de Datos Relacional: MySQL.
ORM: Puede usarse un ORM como SQLAlchemy (para Python) o Hibernate (para Java) para manejar las operaciones de la base de datos.
API REST: Framework como Flask, Django (Python), o Spring Boot (Java) para desarrollar la API que exponga los endpoints.

5. Consideraciones de Seguridad
Autenticación y Autorización: Asegurarse de que solo el personal autorizado pueda acceder o modificar los registros.
Backup y Recuperación: Implementar un sistema de backups regulares para proteger los datos.
Encriptación de Datos: Encriptar datos sensibles como información personal de los bebés.

7. Escalabilidad
Sharding: Dividir la base de datos en fragmentos más pequeños para manejar grandes volúmenes de datos si es necesario.
Replicación: Implementar replicación de bases de datos para alta disponibilidad.
------------

- **Microservicio de Salud y Bienestar Lizbeth Cortés**

1-Registro de Información de Salud:
Historia Médica: Registro de enfermedades previas, alergias, y condiciones médicas de cada niño.
Vacunas: Seguimiento de vacunas administradas, fechas y próximas dosis necesarias.
Medicamentos: Información sobre medicamentos que los niños deben tomar, horarios y dosis.

2-Monitoreo de Salud Diaria:
Temperatura y Síntomas: Registro de la temperatura corporal y síntomas como tos, dolor de estómago, etc.
Observaciones de Bienestar: Notas sobre el estado general del niño, como cambios en el apetito o el estado de ánimo.

3-Alertas y Notificaciones:
Recordatorios de Medicación: Envío de notificaciones a los cuidadores y personal sobre los horarios de medicación alertas de Salud: Notificaciones en caso de fiebre alta, reacciones alérgicas, o si un niño muestra síntomas preocupantes.

4- Informes para Padres: 
Generación de informes y actualizaciones regulares sobre la salud de los niños.
Acceso para Médicos: Permitir a los médicos consultar la información relevante con el consentimiento de los padres.

------------


Todos estos microservicios serán implementados en el lenguaje de programación Python y se tendrán que realizar de manera eficiente, eficaz, en tiempo y forma.

**Gracias.**:smile:

------------
###### SoftGarden

