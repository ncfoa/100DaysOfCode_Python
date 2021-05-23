from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World! <br> Welcome to my Flask App... <br> -Dave'


if __name__ == "__main__":
    app.run()
