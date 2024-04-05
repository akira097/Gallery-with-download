from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/galery', methods=['POST', 'GET'])
def login():
    global photo_list, FILE_COUNT
    if request.method == 'GET':
        return render_template('base.html', photo_list=photo_list)
    elif request.method == 'POST':
        FILE_COUNT += 1
        name = f'web{FILE_COUNT}.jpg'
        f = request.files['file']
        q = open(name, mode='wb')
        q.write(f.read())
        q.close()
        photo_list.append(name)
        return render_template('base.html', photo_list=photo_list)


if __name__ == '__main__':
    os.chdir('static/img')
    photo_list = os.listdir()
    FILE_COUNT = len(photo_list)
    app.run(port=8080, host='127.0.0.1')
