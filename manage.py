#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#importa el sistema operativo y los argumentos de la terminal 


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sitioweb.settings')
    #nos dice que busquemos el archivo settings.py dentro de la carpeta sitioweb 
    #dice donde encontrar la configuración del proyecto Django
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)   #ejecuta el comando 


if __name__ == '__main__':
    main()
