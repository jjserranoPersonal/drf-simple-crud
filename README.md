# DRF Simple CRUD

Este es un proyecto de ejemplo que implementa una API REST simple para gestionar "Proyectos" utilizando Django y Django Rest Framework.

## Características

- CRUD completo para el modelo `Project`.
- Documentación automática de la API con CoreAPI.
- Soporte para bases de datos SQLite y PostgreSQL.
- Preparado para despliegue en plataformas como Render.

## Requisitos

- Python 3.10+
- Django 4.2
- Django Rest Framework 3.14.0

## Instalación

1. Clonar el repositorio.
2. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
   *Nota: Si encuentras problemas con `coreapi` en versiones recientes de Python, asegúrate de tener una versión de `setuptools` compatible (ej. `pip install "setuptools<70"`).*

3. Realizar las migraciones:
   ```bash
   python manage.py migrate
   ```

4. Ejecutar el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

La API está disponible en los siguientes endpoints:

- `GET /api/projects/`: Lista todos los proyectos.
- `POST /api/projects/`: Crea un nuevo proyecto.
- `GET /api/projects/{id}/`: Detalle de un proyecto específico.
- `PUT /api/projects/{id}/`: Actualiza un proyecto.
- `DELETE /api/projects/{id}/`: Elimina un proyecto.

### Otros Endpoints

- `GET /docs/`: Documentación interactiva de la API.
- `GET /admin/`: Panel de administración de Django.

## Modelo de Datos (Project)

- `title`: Título del proyecto (String).
- `description`: Descripción detallada (Text).
- `technology`: Tecnología utilizada (String).
- `created_at`: Fecha de creación (Automática, lectura).
