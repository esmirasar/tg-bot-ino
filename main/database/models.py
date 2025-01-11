from typing import List, Optional

from sqlalchemy import Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.orm import mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger(), unique=True)
    telegram_name: Mapped[str] = mapped_column(String(70))
    telegram_username: Mapped[str] = mapped_column(String(32), unique=True)

    categories: Mapped[List["Category"]] = relationship("Category", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, telegram_id={self.telegram_id!r}, telegram_name={self.telegram_name!r}, telegram_username={self.telegram_username!r})"


class Category(Base):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    language: Mapped[str] = mapped_column(String(15))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship("User", back_populates="categories")
    words: Mapped[List["Words"]] = relationship("Words", back_populates="category", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Category(id={self.id}, language={self.language}, user_id={self.user_id})"


class Words(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[Optional[str]] = mapped_column(String())
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    collocation: Mapped[Optional[str]] = mapped_column(String())
    translation: Mapped[str] = mapped_column(String())

    category: Mapped["Category"] = relationship("Category", back_populates="words")

    def __repr__(self):
        return f"Words(id={self.id}, word={self.word}, category_id={self.category_id}, collocation={self.collocation}, translation={self.translation})"
