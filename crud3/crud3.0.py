from flask import Flask, request, redirect, url_for, render_template
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

@app.route('/delete/<int:id>')
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return redirect(url_for('index'))#ser render_template('index.html') é a mesma coisa

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    if request.method == 'POST':
        estudante.nome = request.form['nome']
        estudante.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', estudante=estudante)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
