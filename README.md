# Django

Python based web application development

# Features

MVT Framework
Hot loading on browser
ORM

# REQUIREMENTS

PYTHON 3.x
DJANGO 2.x

# INSTALLATION ON WINDOWS

-> PYTHON
    --> Download python 3.x from https://www.python.org/downloads/
    --> Set python library path to PATH environmental variable

-> DJANGO
    --> Create a virtual environment for Django project (better way for isolating projects)
        Create a project folder
        python -m venv Virtual_Environment_Name
    --> To install Django
        python -m pip install django

# Project Structure

# WSGI :

(API) Interface for server and web application communication

# URLS :

Hold links among templates within project (*URL resolver)

# SETTINGS :

Project settings/ Site configuration

# MANAGE :

Site management

# Application Structure

# ADMIN :

Administrative interface

# APPS :

Application configuration

# MODELS :

Data objects maintenance

# TESTS :

Unit Testing

# VIEWS :

Define pages in application

# MIGRATIONS :

Administrative utility for managing database versions

# COMMANDS :

-> TO START DJANGO PROJECT
    django-admin startproject [ProjectName]

cd ProjectName

-> TO RUN DJANGO SERVER
    python manage.py runserver [PORT]

-> TO CREATE APPLICATION
    python manage.py startapp [ApplicationName]