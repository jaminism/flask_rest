"""
Flask Server for calling api by version
"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def post_log():
    return 'Create app.py file'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
