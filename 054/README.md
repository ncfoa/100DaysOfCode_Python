# 100 Days of Code Python

### Creating a webserver with [Flask](https://pypi.org/project/Flask/)
This application is just a simple Flask server providing a `Hello World!`
page from your local machine. After you create your server, create a `.env` 
file in your directory where you will be running `flask run` from by simply 
pasting the following into your command line(on mac and linux windows may require something else.)
`echo FLASK_APP=hello_world.py >> .env` now any time you type `flask run` in the
directory with the .env file it will pull the environment variable from the `.env`
file and run with it. 
