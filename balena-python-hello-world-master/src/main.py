from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'TKXCHR001 and SWNNIS001'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
