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

The server will now be running and you can access it at http://localhost:8000  (replace localhost with your public IP if accessing from a different computer and make sure your firewall allows it).

If you wish to create fake users to test the functionality of the game without needing a large number of real users connected, you can navigate to http://localhost:8000/home/fakeUserGen/ and it will generate 10 fake users named user1 through user10.  Then you can use the "Add Fake Users" button when hosting a game to be able to test in-game functionality without real users present.
