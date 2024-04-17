from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/date')
def show_date():
    now = datetime.datetime.now()
    return f'Current date and time: {now}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
