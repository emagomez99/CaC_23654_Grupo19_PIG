# CaC_23654_Grupo19_PIG
Proyecto de Codo a Codo, comisión 23654, grupo 19 

## Descripción

Sistema de gestión de figuritas.

## Integrantes

- Emanuel Gomez
- Lucas Caracciolo

## Requisitos

- [Python 3.10.11 o superior](https://www.python.org/downloads/)

>```bash
>python -V
>```

- [Django 4.2.5](https://docs.djangoproject.com/en/4.2/releases/4.2.5/)

>```bash
>python -m django --version
>```

## Instalación

1. Clonar el repostorio desde git
>```bash
>git clone 'https://github.com/emagomez99/CaC_23654_Grupo19_PIG.git'
>```
2. Accedeter a la carpeta raíz del projecto
>```bash
>cd CaC_23654_Grupo19_PIG.git/
>```
3. Crear el enterno virtual
>```bash
>python -m venv 'venv'
>```
4. Activar el entorno virtual
  >*Windows*
  >
  >```bash
  >venv\Scripts\activate
  >```
  >
  >*Linux / macOS*
  >
  >```bash
  >source venv/bin/activate
  >```
5. Instalar las dependencias
>```bash
>
>```
6. Crear un archivo .env en la carpeta raíz
>```bash
>SECRET_KEY='secret_key'
>DB_PASS='db_password'
>```
7. Crear un usuario administrador
>```bash
>python manage.py createsuperuser
>````
8. Levantar el sitio en el servidor local
>```bash
>python manage.py runserver
>````
