# Starting A Django Project

First thing to do is to install the latest version of [python](https://www.python.org/downloads/ "python.org") and then use the python package manager `pip` to install django globally.

```bash
python -m pip install Django
```

<br/>

With that you have it set up globally and you can check that with the following command:

```bash
# You may have to use python3 if you have older versions of python on your system.
# Check by using > python --version
python -m django --version
```
<br/>

After you get Django installed, it is time to create a project. Create a project folder and open it in your IDE (VSCode for me). When in this folder, select open folder and navigate to your newly created folder. Once open, open up the integrated terminal in the IDE or simply navigate to the project folder in your systems main terminal application. In there you will create a Django project with this command:


```bash
# The project name "mysite" can be whatever you want to name your project.
# The optional period at the end will stop the setup from creating two folders of the same name.
django-admin startproject mysite .
```
<br/>

You should now see that you have a project folder with the name you chose and a `manage.py` file. The `manage.py` file is a command utility file to interact with your project. In the project folder you will have a files related to configuring your project for development and for serving your project on the web. One of the files, `__init__` is there solely to mark to python that this folder should be considered a package. The main two that we need to interact with at the moment is the `settings.py` and the `urls.py`. 

<br/>

To run your server and see the development only page, type this command in your terminal at the root of the project where your `manage.py` lives:

```bash
# You can specify ports and/or IPs like so: 0.0.0.0:3000 or just 3000 for the port.
# Default IP: http://127.0.0.1:8000/
python manage.py runserver
```
## Creating Apps For The Project

In order to get functionality from a Django project, we need to create apps (modules) for our project to connect with and utilize. In Django, apps are sections or parts of our project, dealing with specific functionality or features. For example, in an e-commerce application you can have one app for the store front, one for customer accounts, one for the cart and one for checkout.