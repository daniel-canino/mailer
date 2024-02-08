# Mailer

## ¿Que hace?

1. Permite enviar correos 
2. Muestra los correos que se han enviado en la app 
3. Tiene un buscador, en el cual puedes buscar por el contenido del correo que se han enviado

Creada con FLASK, POSTGRESQL, HTML Y CSS

## Como usarla o configurla

1. Clona el repositorio o descargalo como zip.

```git clone https://github.com/daniel-canino/mailer.git```

2. Instala las dependencias/librerias en requirements.txt

```pip install -r requirements.txt```

3. Debe tener Postgresql instalado.

4. Crea un archivo .env y agrega las variables de entorno.

    - FLASK_DATABASE_HOST=tu_host_bd
    - FLASK_DATABASE_USER=tu_usuario_bd
    - FLASK_DATABASE_PASSWORD=tu_password_bd
    - FLASK_DATABASE=nombre_bd
    - PASSWORD_KEY=tu_key_email

5. Configurar tu correo y obtener la clave de acceso.
    Para realizar este paso puedes seguir ver video https://youtu.be/DDVpKvJXRz8?si=PAa-kHrDnKU13UZ8

6. Inicializa la base de datos.

```flask init-db```

7. Corre el servidor.

```flask run```
