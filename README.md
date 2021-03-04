# mastermindplayer webpage using Flask and AJAX
This Flask application is a small personal project to learn a bit of Flask and the use of AJAX. It provides a web interface to play the mastermind game. The webpage will use AJAX requests to create a new game, play a round or retrieve the solution and update the webpage. The application itself will forward the requests from the webpage to the docker container which runs the Mastermind API (see the corresponding Repo).

To run the game, start the application with the terminal command: python3 app.py
(Please note that the Mastermind API docker container must be running prior to launching the application)

The webpage itself can then be retrieved in the browser on: http://127.0.0.1:5000/

![Screenshot of webpage](https://github.com/KennethEmerson/mastermindplayer/blob/main/Screenshot.png)
