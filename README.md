# Tutorial de Flask

Este tutorial tiene como objetivo desarrollar un mini blog usando el framework web Flask, el cuál está basado en Python.

Durante las diferentes lecciones se verá todo aquello que, personalmente, considero que hay que tener en cuenta a la
hora de desarrollar una aplicación web (cualquier aplicación web, no solo en Flask). Por tanto, se repasarán aspectos
esenciales como gestión de usuarios, control de errores, trazas de log, seguridad, test o arquitectura.

## Funcionalidades del miniblog

El miniblog a desarrollar tendrá las siguientes características:

* Existirán dos tipos de usuario: administradores e invitados.
* Un usuario administrador puede añadir, modificar y eliminar entradas del blog.
* Los usuarios invitados pueden registrarse en el blog para comentar las diferentes entradas.
* Un usuario administrador puede crear, modificar, eliminar y listar usuarios, además de poder asignarles el rol de administrador.

## Lecciones del tutorial

* Lección 1: La primera aplicación Flask
* Lección 2: Uso de plantillas para las páginas HTML
* Lección 3: Uso de formularios en Flask
* Lección 4: Gestión de usuarios: Registro y Login
* Lección 5: Añadiendo una base de datos: SQLAlchemy
* Lección 6: Estructura de un proyecto con Flask: blueprints
* Lección 7: Parámetros de configuración de un proyecto Flask
* Lección 8: Gestión de errores
* Lección 9: Flask y trazas de log
* Lección 10: Securizando los endpoints
* Lección 11: Actualizando la base de datos
* Lección 12: Test con Flask
* Lección 13: Paginando las consultas de base de datos
* Lección 14: Envío de emails
* Lección 15: Trabajando con Fechas
* Lección 16: Trabajando con ficheros
* Lección 17: Flask y PyCharm
* Lección 18: Despliegue de una aplicación Flask en un entorno de producción

## Lecciones extra

* Lección 19: Recordar contraseña
* Lección 20: Ejecución de trabajos en background
* Lección 21: Añadiendo peticiones AJAX
* Lección 22: Internacionalización de la web
* Lección 23: Crear un API con Flask: Flask-RESTful
* Lección 24: Securizando el API
* Lección 25: Gestión de errores del API
* Lección 26: Documentando el API: flask-swagger-ui
* Lección 27: Integrando mongodb
  
## Descarga e instalación del proyecto

Para descargar el proyecto puedes clonar el repositorio:

    git clone https://github.com/j2logo/tutorial-flask.git
    
> Cada una de las lecciones se corresponde con una hoja del repositorio.
> El nombre de las hojas es "leccionXX".

Si quieres descargar una lección en concreto, ejecuta el siguiente comando git:

    git checkout tags/<leccionXX> -b <nombre-de-tu-rama>

Por ejemplo:

    git checkout tags/leccion1 -b leccion1

### Variables de entorno

Para que el miniblog funcione debes crear las siguientes variables de entorno:

#### Linux/Mac

    export FLASK_APP="run.py"
    export FLASK_ENV="development"

#### Windows

    set "FLASK_APP=run.py"
    set "FLASK_ENV=development"
    
> Mi recomendación para las pruebas es que añadas esas variables en el fichero "activate" o "activate.bat"
> si estás usando virtualenv
 
### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

    pip install -r requirements.txt

## Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno y descargado las dependencias,
puedes arrancar el proyecto ejecutando:

    flask run
