# Pasos para levantar servidor

- Crear entorno virtual (ojo donde lo crean)

        python3 virtualenv <mi_entorno>
- Activar entorno virtual

        - \path\to\env\Scripts\activate (Windows)
        - source /path/to/env/bin/activate (Linux)

        source /opt/carpeta1/carpeta2/nuetro_proyecto
- Nos movemos hasta la raiz de nuestro proyecto
- Instalar las dependencias

        pip install -r requirements.txt

- Ejecutar servidor Flask

        python3 app.py

## Para desactivar entorno

        deactivate