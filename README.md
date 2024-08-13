**-- This README is being constructed as I progress through the project. Information may not yet be accurate. --**

<br/>

# Starting A Django Project

If you haven't done so, make sure you already have python installed. To install the latest version of python, go to the official site [python.org](https://www.python.org/downloads/ "python.org") and download the latest version for your operating system. I will be using Linux and the bash terminal.

Before starting any python project, it is best to create a virtual environment. Virtual environments create a project level separation of modules and libraries so that every project gets a version of the modules they need without effecting anything globally. 

To start, we need to create the setup files for the virtual environment. We do this with the command:

```bash
python -m venv env
```

<br/>

Then we need to activate the virtual environment. Run the command bellow:

```bash
# start the virtual environment
source env/bin/activate

# if you need to deactivate from a virtual environment, use command:
deactivate
```
<br/>

We have our virtual environment up and running. Let's get django added to our environment using pip, python's package manager:  

```bash
# Assuming you already have python installed, use pip to install packages
pip install django

# Or if you need a specific version
pip install django==3.6
```

<br/>

You can check that it was downloaded successfully by using following command:

```bash
# You may have to use python3 if you have older versions of python on your system.
# Check by using > python --version
python -m django --version
```
<br/>

After you get Django installed, it is time to create a project. 

Create a project folder and open it in your IDE (VSCode for me). When in this folder, Once open, use the integrated terminal in the IDE or simply navigate to the project folder in your systems main terminal application. In there you will create a Django project with this command:


```bash
# The project folder name "config" can be whatever you want to name your project settings folder.
# The optional period at the end will stop the setup from creating two folders of the same name.
django-admin startproject config .
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