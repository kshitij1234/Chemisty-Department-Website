# Chemisty-Department-Website
The official website of chemistry department of IIT Patna

### Steps for setting up the Project - 
1. Install python 3.6.0 .
1. Clone this repository
1. cd into the local repo and run the following commands:
   1. python -m venv chemvenv   (Sets up a virtual environment - makes it easier to manage projects with different versions of modules.)
   1. chemvenv\Scripts\activate (Starts the virtual environment . Make sure to run this command every time before starting work on the project. Also makes it easier to maintain the website in future.)
   1. pip install --upgrade pip
   1. pip install Django==1.11.2
   1. pip install Pillow
   
### How to run the project on localhost

Go to the local repository and run the following commands:
   1. cd Chemisty-Department-Website-master
   1. python manage.py runserver

Now you can access the project on browser at 127.0.0.1:8000
