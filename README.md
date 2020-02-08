# werewolf
Online Werewolf (game) managing app for our Python Project Week
Made by Jake Sklarew, Sonia Benothmane, and Kaelo Bang


Required dependencies for running the django server:
  
  -Create a virtual environment, and run the following pip installation commands:
    
    - pip3 install django==2.2
    - pip3 install bcrypt
    - pip3 install plotly

  -To be safe, in the werewolf_project directory where manage.py is located, run the following commands:
  
    - python3 manage.py makemigrations
    - python3 manage.py migrate
    
  (those two are only necessary the first time you setup the server to get the database setup)
  
  -Then to run the server at the local address so that anyone can connect at port 8000 to your IP, run:
  
    - python3 manage.py runserver 0.0.0.0:8000
