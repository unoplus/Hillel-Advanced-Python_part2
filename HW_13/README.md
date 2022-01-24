# LESSON TWENTY ONE

## Starting Django

## description of folders and files

**FOLDERS**

1. **config** - _base configuration files for django._
2. **core** - _base configuration files for user project._
3. **migrations** - _Project migration files._

**FILES**

1. **config/init.py** - _An empty file that tells Python that this directory should be considered a Python package._
2. **config/asgi.py** - _An entry-point for ASGI-compatible web servers to serve the project._
3. **config/settings.py** - _Settings/configuration for Django project._
4. **config/urls.py** - _The URL declarations for Django project; a “table of contents” of Django-powered site._
5. **config/wsgi.py** - _An entry-point for WSGI-compatible web servers to serve the project._

6. **core/migrations/init.py** - _An empty file that tells Python that this directory should be considered a Python package._

7. **core/init.py** - _An empty file that tells Python that this directory should be considered a Python package._
8. **core/admin.py** - _Used to display your models in the admin panel_
9. **core/apps.py** - _Django contains a registry of installed applications that store configuration and provides introspection. It also maintains a list of available models._
10. **core/models.py** - _A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table._
11. **core/tests.py** - _A conventional place for tests an application’s. You can write your own tests here._
12. **core/views.py** - _This is where we will place the "logic" of our application._

13. **manage.py** - _A command-line utility that lets you interact with Django project in various ways._
14. **Pipfile** - _Virtual environment requirements._
15. **Pipfile.lock** - _The lock file is created on the basis of the Pipfile file itself._
16. **README.md** - _Project description._

## Update 01 at 01.01.2022

Created Post and Like in admin panel

## Update 02 at 15.01.2022

**Create new app 'user'.**
**Create page 'posts'.**
**Create templates, styles, etc.**
**Adding some features like: view all posts, authors, how many posts created by author, likes/dislikes, etc.**

## Update 03 at 20.01.2022

**Adding debug toolbar for dev.**
**Change engine to mySQL for dev.**
**Create page 'post detail view'.**
**Create page 'post delete'.**
**Create templates, styles, etc.**
**Adding new fonts, backgrounds, etc.**
**Some SQL-requests tuning.**

## Update 04 at 24.01.2022

**Change engine to postgreSQL for dev.**
**Create pages 'update posts' and 'create post'.**
**Adding 'forms.py' with some stuff for forms.**
**Create templates, styles, etc.**
**Some code review for optimization**
**Some SQL-requests tuning.**
**Adding lib 'pillow'.**
