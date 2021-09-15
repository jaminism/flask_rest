"""
Flask Server for calling api by version
"""
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def post_data():
    return 'Create app.py file'

if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    serve(app, host="0.0.0.0", port=80)