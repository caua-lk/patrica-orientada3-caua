from database import sessao, Base, engine
from models import User, Book
from werkzeug.security import generate_password_hash
Base.metadata.create_all(engine)
session = sessao
senha = generate_password_hash('robertinho')
maria = User(nome="Maria", email='maria@gmail.com', senha=senha)

session.add(maria)
session.commit()

livro = Book(titulo="Dom Casmurro", usuario=maria)
session.add(livro)
session.commit()
session.close()