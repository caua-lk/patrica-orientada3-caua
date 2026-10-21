from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

engine = create_engine("sqlite:///biblioteca.db", echo=False)
Base.metadata.create_all(engine)

sessao = Session(bind=engine)