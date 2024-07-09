# Game Figures Hub

Game Figures Hub es una tienda en línea para los entusiastas de las figuras de acción de videojuegos, anime y cómics. Este proyecto está diseñado con Django y Bootstrap para proporcionar una experiencia de usuario fluida y atractiva.

## Características

- **Autenticación de Usuarios**: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión.
- **Roles de Usuario**: Existen roles de administrador y usuario normal.
- **Administrador**: Puede gestionar productos y usuarios.
- **Usuario Normal**: Puede ver productos, agregar productos al carrito y realizar compras.
- **Gestión de Productos**: Los administradores pueden crear, leer, actualizar y eliminar productos.
- **Carrito de Compras**: Los usuarios pueden agregar productos al carrito y proceder a la compra.
- **Búsqueda de Productos**: Incluye una barra de búsqueda para facilitar la localización de productos.
- **Música de Fondo**: Se reproduce música de fondo mientras los usuarios navegan por la tienda.

## Tecnologías Utilizadas

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Base de Datos**: SQLite (por defecto con Django, pero puede ser cambiado a cualquier otra base de datos soportada por Django)

## Instalación

Sigue estos pasos para configurar el proyecto localmente:

1. Clona este repositorio:
    ```bash
    git clone https://github.com/CvmiloM/ProyectoET.git
    ```

2. Crea un entorno virtual:
    ```bash
    python -m venv env
    ```

3. Activa el entorno virtual:

    - En Windows:
        ```bash
        .\env\Scripts\activate
        ```

    - En macOS y Linux:
        ```bash
        source env/bin/activate
        ```

4. Instala las dependencias:
    ```bash
    pip install pillow
    ```

6. Realiza las migraciones:
    ```bash
    python manage.py migrate
    ```

7. Carga los archivos estáticos:
    ```bash
    python manage.py collectstatic
    ```

8. Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

9. Abre tu navegador y navega a `http://127.0.0.1:8000/` para ver la aplicación en acción.

## Archivos Importantes

- `templates/`: Contiene las plantillas HTML.
- `static/`: Contiene archivos estáticos como CSS, JavaScript e imágenes.
- `media/`: Contiene archivos subidos, como imágenes de productos.
- `README.md`: Este archivo con la documentación del proyecto.

## Personalización

### Música de Fondo

Para cambiar la música de fondo, reemplaza el archivo `intro.mp3` en el directorio `static/audio/`.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes una idea o mejora, por favor abre un "issue" o envía un "pull request".

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.


---

¡Gracias por visitar Game Figures Hub! Esperamos que disfrutes de tu experiencia de compra.
