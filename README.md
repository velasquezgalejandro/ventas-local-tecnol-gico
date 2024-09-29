# ventas-local-tecnol-gico
Sistema de Ventas para Local de Tecnología

## Funcionalidades

Aquí encontras las principales funciones que se han implementado en el proyecto:

- **Funcionalidad 1**: Se crea vista de inicio con enlaces a demas vistas (categorias, clientes, productos y ventas)
- **Funcionalidad 2**: Se crea vista para seleccionar el servicio que se desea gestionar
- **Funcionalidad 3**: Se crean vistas para la creación, el detalle, la edicción y la eliminación
- **Funcionalidad 3**: Se crea formulario de creacion y actualizacion
- **Funcionalidad 5**: Se implementan filtros para la busqueda

## Instalación

Pasos para instalar el proyecto localmente:

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/velasquezgalejandro/ventas-local-tecnol-gico.git
    ```

2. **Accede al directorio del proyecto:**

    ```bash
    cd sistema_ventas
    ```

3. **Ejecuta las migraciones de la base de datos e inicia el servidor en local:**
    ```bash
    python manage.py migrate
    python manage.py makemigration
    python manage.py migrate
    python manage.py runserver
    ```

    o

    ```bash
    py manage.py migrate
    py manage.py makemigration
    py manage.py migrate
    py manage.py runserver
    ```
