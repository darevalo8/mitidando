### Mitidando

# Instalacion

cree un entorno virtual despues de activarlo
ubicquese en la carpeta del proyectos y ejecute el siguiente comando

`pip install -r requirements.txt`

Luego este comando para instalar las migraciones de la bases de datos

`python manage.py migrate`

para usar el administrador de django creamos un super usuario con el siguiente comando:

`python manage.py createsuperuser`

seguimos los pasos que la consola nos pida.

por ultimo ejecutamos el servidor local con el siguiente comando:

`python manage.py runserver`

luego vamos al localhost:8000/admin e ingresamos el usuario y contraseña que creamos a la hora de crea el administrador.