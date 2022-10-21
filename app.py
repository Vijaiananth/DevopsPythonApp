from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Vijai Ananth Flask application version 2'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)