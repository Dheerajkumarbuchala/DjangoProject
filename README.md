# DjangoProject
This project is completed as a part of a training program

## Virtual Environment
    - python3 venv -m myvenv
    - source myvenv/bin/activate

## Install Django
    - python3 -m pip install Django

## Initializing a Django project
    - django-admin startproject LoginSystem

## Creating a new app
    - cd LoginSystem
    - python manage.py startapp Loginify
    - Register the new app in the INSTALLED_APPS in settings.py of LoginSystem

## Migration Errors
    - When ran the server for the first time, the following errors will occur
      as we need to migrate the configurations.
    - To remove the errors :
        - python manage.py makemigrations
        - python manage.py migrate

## URLS and Views
    - It is better to store the urls of the application in the application    
      folder itself rather than in the project folder.
    - Using include() we can direct the urls from project to app as we are 
      developing.
    - Usually the app we created will not be having a urls.py file, we should 
      create it and tell the base dir urls folder to look for the app specific urls in the folder we created in the app directory.
    - path("loginify/", include('Loginify.urls')) (This tells us where to   
      look for the urls)
    - path("hello_world/", views.hello_world) (This is the url which is in  
      our app folder)

## Templates
    - Usually Templates folder will be at the project level and each app   
      directory will be created and the template of the respective apps will be stored in their respective directories.
    - The path to the Templates should be registered in the settings.py
    - "DIRS": [BASE_DIR/'Templates']