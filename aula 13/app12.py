import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__, template_folder='templates')
upload_folder = os.path.join(os.getcwd(), 'upload')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['imagem']
    savepath = os.path.join(upload_folder, secure_filename(file.filename))
    file.save(savepath)
    return 'Upload feito com sucesso'


@app.route('/get-file/<filename>')
def getfile(filename):
    file = os.path.join(upload_folder, filename + '.bmp')
    return send_file(file, mimetype='image/bmp')


if __name__ == '__main__':
    app.run(debug=True)
