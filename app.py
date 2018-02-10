from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    timeNow = str(datetime.utcnow())
    return "Hello from a container it's time"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
