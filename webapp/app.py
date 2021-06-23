from flask import Flask, render_template, request
import subprocess
from os.path import exists, join
import config
import os


if exists(join(config.WORKSPACE, 'mount', 'healthy')):
    os._exit(0)

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if exists(join(config.WORKSPACE, 'mount', 'healthy')):
        os._exit(0)
    elif request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        password = request.form.get('password')
        proc = subprocess.run([join(config.WORKSPACE, 'decrypt'), '--name', config.NAME, '--workspace', config.WORKSPACE, '--password', password],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode == 0 and exists(join(config.WORKSPACE, 'mount', 'healthy')):
            print(proc.stdout.decode("utf8"))
            os._exit(0)
        else:
            return f'Error:\n {proc.stderr.decode("utf8")}'


app.run(host='0.0.0.0', port=8000)
