# Generador de Syllabus y Gestión Programática de Cursos

Esta aplicación que proporciona una API para la gestión de syllabus de cursos y la generación de documentos relacionados. Tiene dos implementaciones para la gestión de datos, una que utiliza una base de datos SQLite para almacenar la información del curso y otra con archivos CSV.  Ofrece funcionalidades para exportar syllabus en formato LaTeX y generar calificaciones en formato CSV.

Originalmente esta serie de scripts estaban diseñados para propositos personales en la gestión de cursos en la Universidad Autónoma de Metropolitana Unidad Iztapalapa (UAM-I), en la UEA que he impartido. Cada trimestre he ido mejorando y adaptando los scripts para automatizar la generación de syllabus y la gestión de calificaciones. Aprovechando lo que recién aprendí al desarrollar una API para un proyecto de *Machine Learning en Aplicaciones Médicas*, decidí migrar el sistema de gestión de syllabus a una arquitectura arquitectura hexagonal con *entry points* en CLI gestionados con Hydra, permitiendo una mayor modularidad y escalabilidad.

Actualmente la App genera los archivos de LaTeX hard-coded, y usando *Jinja2* para generar partes complejas como cuadros y listas de temas. Creo que la nueva arquitectura permitirá implementarlo de forma más óptima en el futuro.

Espero que les sea de utilidad y sus comentarios/retroalimentación. Saludos

Omar Piña Ramírez
delozath@gmail.com
2026.01.18

## Features
**Implementados**
- Crear y gestionar syllabus de cursos
- Endpoints API para la recuperación y actualización de syllabus
- Cargar datos desde una base de datos SQLite
- Cargar datos desde archivos CSV
- Exportar syllabus en formato LaTeX

**En migración**
- Generar calificaciones en formato CSV. 


## Instalación
1. Requisitos previos:
   - Python 3.8 o superior
   - Git
1. Configura un entorno virtual (opcional) e instala dependencias:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`

   pip install hydra-core pylatex jinja2 python-dotenv
   ```
1. Clona el repositorio:
   ```bash
   git clone https://github.com/delozath/core.learning.public.git
   
    ```
1. Instalación local usando pip. Navega al directorio `apps/syllabus` e instala la aplicación en modo editable:
   ```bash
   cd apps
   pip install -e syllabus
   cd syllabus
   ```
1. Configura las variables de entorno. Crea un archivo `.env` en el directorio `apps/syllabus/` con las siguientes variables:
   ```env
   DB_PATH=/ruta/a/tu/carpeta/de/datos/
   TEX_FILES_PATH=/ruta/a/tu/carpeta/de/archivos/tex/
   ```

## Estructura del Proyecto
<details>
<summary>Árbol del proyecto</summary>

```bash
└── apps
    └── syllabus
        ├── files
        │   ├── common.sty
        │   ├── cursos.db
        │   ├── lini-v1.png
        │   ├── notas.csv
        │   ├── temario.csv
        │   ├── uam-izt-v6.png
        │   └── uea_planeacion.sty
        ├── pyproject.toml
        ├── README.md
        └── src
            ├── syllabus
            │   ├── conf
            │   │   ├── config.yaml
            │   │   ├── curso
            │   │   │   └── symp.yaml
            │   │   └── institution
            │   │       └── uam.yaml
            │   ├── core.py
            │   ├── data
            │   │   ├── _csv_driver.py
            │   │   ├── loader.py
            │   │   └── _sqlite_driver.py
            │   ├── main.py
            │   ├── outputs
            │   ├── ports
            │   │   ├── dbs.py
            │   │   └── tasks.py
            │   ├── tasks
            │   │   └── uam
            │   │       ├── __init__.py
            │   │       ├── jinja_driver.py
            │   │       ├── _syllabus.py
            │   │       ├── templates
            │   │       │   ├── uami_eventos.tex.j2
            │   │       │   ├── uami_sesiones.tex.j2
            │   │       │   └── uami_temario.tex.j2
            │   │       └── trimestre.py
            │   └── utils.py
            └── 
```
</details>

## Uso
Ejecuta la aplicación desde CLI:
   ```bash
   >> apps/syllabus$ python -m syllabus.main institution=uam curso=symp task=syllabus +db_type='csv'
   ```
Las opciones institucion y curso hacen los mapeos correspondientes a los archivos de configuración YAML en `src/syllabus/conf/institution/` y `src/syllabus/conf/curso/`. El parámetro `db_type` selecciona la fuente de datos, ya sea `sqlite` o `csv`.

En la carpeta files/ se encuentran los archivos de datos y estilos necesarios para la generación de los syllabus UAM-I de la UEA Secuenciadores y Microprocesadores.