from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudantes.sqlite3'

db = SQLAlchemy(app)

class Estudante(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

@app.route('/')
def index():
    estudantes = Estudante.query.all()
    return render_template('index.html', estudantes=estudantes)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        estudante = Estudante(request.form['nome'], request.form['idade'])
        db.session.add(estudante)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    if request.method == 'POST':
        estudante.nome = request.form['nome']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', estudante=estudante)

@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():  # Usar o contexto do aplicativo
        db.create_all()  # Cria as tabelas do banco de dados
    app.run(debug=True)
