# 🎬 Proyecto: Rediseño y Gestión de Cinemark Perú (Backend Django)

## 🌟 Visión General

Este proyecto es una aplicación web full-stack desarrollada con Python y Django, creada para demostrar la capacidad de construir una **arquitectura modular de backend** y un sistema completo de **gestión de contenido (CMS)** para un sitio de cine.

A diferencia del sitio original, este proyecto permite la gestión total de inventario y usuarios a través de un panel de administración personalizado.

---

## ✨ Logros y Funcionalidades Demostradas

Este proyecto demuestra el dominio de la **Arquitectura MVT (Modelo-Vista-Template)** y las mejores prácticas de Django:

### ⚙️ Backend y Arquitectura

* **Arquitectura Modular:** El proyecto está dividido en aplicaciones cohesivas: `core` (autenticación), `administration` (panel de gestión), `peliculas` (catálogo y salas), y `productos` (confitería). *(Esto demuestra escalabilidad y buena organización).*
* **CRUD Completo:** Implementación de la lógica **Crear, Leer, Actualizar, y Eliminar (CRUD)** para **Productos**, **Anuncios**,**Peliculas**, **Géneros** y **Salas**.
* **Autenticación y Permisos:** Sistema de **Login/Logout** y **Registro** de usuarios. Vistas protegidas que restringen el acceso al panel de administración solo a usuarios con rol `is_staff`.
* **Manejo de Relaciones Complejas:** Implementación de relaciones **Muchos-a-Muchos (`ManyToManyField`)** para asignar múltiples géneros y salas a una sola película (gestionado en `views.py` con `getlist` y `set`).
* **Base de Datos Segura:** Uso de `UUIDField` para IDs robustos y `ImageField` para la gestión de archivos multimedia.

### 🎨 Frontend (Plantillas y Estilos)

* **Panel de Administración Personalizado:** Interfaz propia diseñada en HTML/CSS, conectada a las vistas de Django para la gestión de datos.
* **Herencia de Plantillas:** Uso de `base.html` y bloques (`{% extends %}`) para mantener la consistencia visual y evitar código repetido.
* **Servicio de Archivos:** Configuración correcta para servir archivos estáticos (CSS/JS) y archivos media (imágenes subidas por el admin).

---

## 🛠️ Tecnologías Utilizadas

* **Framework Principal:** Python 3.10.0 , Django 5.2.7 , pillow 12.0.0
* **Base de Datos:** SQLite3 (Desarrollo)
* **Manejo de Datos:** Django ORM, `Decimal`, `UUIDField`.
* **Front-end:** HTML5, CSS3.
* **Control de Versiones:** Git & GitHub.

---

## 🚀 Cómo Ejecutar el Proyecto (Instrucciones)

Sigue estos pasos en tu sistema operativo (Windows, macOS o Linux):

1.  **Clonar el Repositorio:**
    ```bash
    git clone https://github.com/MackDaorta/django-Cine.git
    cd django-cine
    ```

2.  **Crear y Activar el Entorno Virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # macOS/Linux
    .\venv\Scripts\activate   # Windows
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configurar Base de Datos y Superusuario:**
    ```bash
    # 1. Crear tablas
    python manage.py migrate
    # 2. Crear administrador
    python manage.py createsuperuser
    ```

5.  **Ejecutar el Servidor:**
    ```bash
    python manage.py runserver
    ```

Ahora puedes acceder a:
* **Página Pública:** `http://127.0.0.1:8000/`
* **Panel de Administración:** `http://127.0.0.1:8000/administrator/`

---

## Próximo Paso: Integración de API

El siguiente paso es exponer los datos del catálogo a través de un API REST utilizando Django REST Framework (DRF) para un futuro frontend en React/Vue.