from sqlalchemy import ForeignKey, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from database import Base

class User(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True)
    senha: Mapped[str] = mapped_column(String(120), nullable=False)
    livros: Mapped[List['Book']] = relationship("Book", back_populates="usuario") # Referencia ao model de livros


class Book(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    usuario_id: Mapped[int] = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False) # Chave estrangeira para o banco de dados
    usuario: Mapped['User'] = relationship("User", back_populates="livros") # Referencia ao model de usuarios para a orientação a objetos
