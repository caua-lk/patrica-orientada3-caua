from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import select
from werkzeug.security import check_password_hash
from database import sessao
from models import User, Book

app = Flask(__name__)
app.secret_key = 'roberto'
@app.route("/", methods=['POST', 'GET'])
def index():
    session = sessao
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        senha = check_password_hash(password=senha)
        usuario = session.scalars(select(User).where(email=email,senha=senha))
        if usuario:
            return redirect(url_for(listar_usuarios))
    return render_template("login.html")

@app.route("/usuario/novo", methods=["POST","GET"])
def new_user():
    if request.method == "POST":
        nome = request.form.get("nome", None)
        email = request.form.get("email", None)

        if nome and email:
            session = sessao
            usuario = session.scalars(select(User).where(User.email==email))

            if not usuario:
                usuario_novo = User(nome=nome, email=email)
                session.add(usuario_novo)
                session.commit()

            else:
                return redirect(url_for('login'))

@app.route("/livros/novo", methods=["POST","GET"])
def new_book():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        user_id = request.form.get("user_id")

        if titulo and user_id:
            session = sessao
            livro = session.scalars(select(Book).where(Book.titulo == titulo)).first()

            if not livro:
                livro_novo = Book(titulo=titulo, user_id=int(user_id))
                session.add(livro_novo)
                session.commit()
                return redirect(url_for("listar_livro"))

    return render_template("book_form.html")

@app.route("/livros/listar")
def listar_livro():
    session = sessao
    livros = session.scalars(select(Book).order_by(Book.titulo)).all()
    return render_template("index.html", livros=livros)


@app.route("/usuarios/listar")
def listar_usuarios():
    session = sessao
    usuarios = session.scalars(select(User).order_by(User.nome)).all()
    return render_template("index.html", usuarios=usuarios)