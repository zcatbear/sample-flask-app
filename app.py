from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    #print(request.headers)
    return str(request.headers)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
