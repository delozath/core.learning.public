# Generador de Syllabus y Gestión Programática API-Application Basada en Python

Esta aplicación proporciona una API para la gestión de syllabus de cursos y la generación de documentos relacionados. Utiliza una base de datos SQLite para almacenar la información del curso y ofrece funcionalidades para exportar syllabus en formato LaTeX y generar calificaciones en formato CSV.

## Features
- Crear y gestionar syllabus de cursos
- Endpoints API para la recuperación y actualización de syllabus
- Cargar datos desde una base de datos SQLite
- Exportar syllabus en formato LaTeX
- Generar calificaciones en formato CSV. Inicialmente pensada para mis cursos de la Universidad Autónoma Metropolitana (UAM)


syllabus.egg-info

## Instalación
1. Clona el repositorio:
   ```bash
   git clone
   python -m pip install hydra-core
    ```
2. Navega al directorio del proyecto:
   ```bash
   cd apps
   pip install -e syllabus
   cd syllabus
   ```

3. Navega al directorio del proyecto:
   ```bash
   >> apps/syllabus$ python -m syllabus.main
   ```

> python -m syllabus.main institution=uam curso=symp