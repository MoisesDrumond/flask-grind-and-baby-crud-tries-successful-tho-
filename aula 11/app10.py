from flask import Flask, render_template, request, make_response


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    resp = make_response(render_template('setcookie.html'))
    if request.method == 'POST':
        dados = request.form['c']
        resp.set_cookie('testeCookie', dados)

    return resp;


@app.route('/getcookie')
def getcookie():
    cookieName = request.cookies.get('testeCookie')
    return f'<h1>Valor cookie é: {cookieName}</h1>'


if __name__ == '__main__':
    app.run(debug=True)