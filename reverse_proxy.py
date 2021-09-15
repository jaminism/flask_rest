import flask import Flask, request, Response
from waitress import serve

app = Flask(__name__)

SITE = 'http://localhost:80'

@app.route('/<path:path>',methods=['GET', 'POST'])
def proxy(path):
    """ 80 포트 리다이렉트
        Post는 Kafka 로 데이터 전달
    """
    if request.method=='POST':
        resp = requests.post(f'{SITE}/{path}')
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
        return response
    else:
        return f'Not Support Method : {request.method}'

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=443)
