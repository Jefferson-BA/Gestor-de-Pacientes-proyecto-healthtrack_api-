# 🧑‍⚕️ HealthTrack API: Gestor de Pacientes y Doctores

## 📝 Descripción del Proyecto

**HealthTrack API** es una API RESTful desarrollada con **Django** y **Django REST Framework (DRF)** que permite la gestión centralizada de pacientes y la asignación de doctores. El objetivo principal es ofrecer un sistema robusto y modular para el control de registros médicos mediante el uso de endpoints HTTP.

---

## ⚙️ Funcionalidades Implementadas (16/16 Puntos)

La aplicación gestiona dos entidades principales, **Paciente** (Entidad 1) y **Doctor** (Entidad 2), y cumple con la totalidad de los requisitos de CRUD, filtrado y relaciones.

| Funcionalidad | Descripción | Endpoint | Método | Puntos |
| :--- | :--- | :--- | :--- | :--- |
| **Listado General (Pacientes)** | Devuelve todos los registros de pacientes. | `/api/v1/pacientes/` | `GET` | 2 pts |
| **Creación (Pacientes)** | Permite crear un nuevo paciente. | `/api/v1/pacientes/` | `POST` | 2 pts |
| **Edición (Pacientes)** | Permite actualizar un paciente existente. | `/api/v1/pacientes/{id}/` | `PUT/PATCH` | 2 pts |
| **Eliminación (Pacientes)** | Elimina un paciente existente. | `/api/v1/pacientes/{id}/` | `DELETE` | 2 pts |
| **🔍 Búsqueda y Filtros** | Búsqueda por `nombre` o `diagnóstico`. | `/api/v1/pacientes/search/?q=` | `GET` | 2 pts |
| **🔗 Relación Entidad 1 y 2** | Muestra el nombre y la especialidad del Doctor asociado en cada Paciente. | `/api/v1/pacientes/` | `GET` | 3 pts |
| **📚 CRUD Doctores** | Endpoints funcionales de CRUD para Doctores (Entidad 2). | `/api/v1/doctores/` | `GET, POST, PUT, DELETE` | 3 pts |
| **Total Funcionalidades** | | | | **16 pts** |

---

## ✨ Puntos Extras y Personalización

Se ha implementado la personalización de la respuesta de los *endpoints* para obtener el punto extra opcional:

| Característica | Implementación | Puntos |
| :--- | :--- | :--- |
| **Personalización de Respuesta** | En el **PacienteSerializer** (Entidad 1), se ha anidado la información del doctor asignado (`nombre` y `especialidad`) bajo el campo `doctor_info`. | **+1 pt** |

---

## 💻 Configuración y Ejecución Local

### Prerrequisitos

* Python 3.x
* pip (Administrador de paquetes de Python)

### Pasos

1.  **Clonar el Repositorio:**
    ```bash
    git clone [LINK_DEL_REPOSITORIO]
    cd healthtrack_api
    ```

2.  **Crear y Activar Entorno Virtual (Recomendado):**
    ```bash
    # En Windows (CMD/PowerShell)
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install -r requirements.txt 
    # (Si no tienes requirements.txt, usa: pip install django djangorestframework)
    ```

4.  **Aplicar Migraciones:**
    ```bash
    python manage.py makemigrations records_app
    python manage.py migrate
    ```

5.  **Ejecutar el Servidor:**
    ```bash
    python manage.py runserver
    ```

La API estará accesible en `http://127.0.0.1:8000/api/v1/`.

---

## 🔗 Endpoints Principales

Todos los *endpoints* utilizan el prefijo `/api/v1/`.

| Entidad | Descripción | Endpoint Base |
| :--- | :--- | :--- |
| **Pacientes** (Entidad 1) | CRUD completo y Listado | `/api/v1/pacientes/` |
| **Doctores** (Entidad 2) | CRUD completo y Listado | `/api/v1/doctores/` |
| **Búsqueda** (Pacientes) | Filtro por nombre o diagnóstico | `/api/v1/pacientes/search/?q={término}` |

---

## 🐙 Historial de Commits

El historial de commits sigue una metodología progresiva y descriptiva, tal como se solicitó, para evidenciar el desarrollo incremental del proyecto.

---

## 🎥 Video de Demostración (Obligatorio)

* **Link de YouTube:** [https://youtu.be/psODygFDBFQ]