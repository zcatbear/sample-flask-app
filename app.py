from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from a container"
if __name__ == '__main__':
    app.run()