# HealthApp
Health App Using Django

1. Created a GitHub repo named HealthApp

2. Created a virtual environment:
    python -m venv Myenv

3. Activated the virtual environment:
    Myenv\Scripts\Activate

4. Installed Django inside the virtual environment:
    pip install django

5. Checked Django version to verify installation:
    django-admin --version

6. Created a Django project named Health:
    django-admin startproject Health .

7. Created a Django app named patients:
    python manage.py startapp patients

8. Applied initial database migrations:
    python manage.py migrate

10. Created view functions in patients/views.py

11. Created URL patterns in patients/urls.py

12. Included patients URLs in the main project’s urls.py

13. Created an Images folder and added image files

* Why use Django URLS
- To manage different paths
- If we are describing any python apps inside the django, then 
we have to use urls.py where we have to define the paths for different apps 
which is written in views.py

* manage.py
- manages overall project
- has main function
- makemigrations

* settings.py
- all configurations happen here

* wsgi.py
- to host project 




