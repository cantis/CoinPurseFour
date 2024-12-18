from datetime import datetime

from app import db
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    """Model for user accounts."""

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    characters = db.relationship('Character', backref='user', lazy=True)


class Character(db.Model):
    """Model for characters."""

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('user.id'), nullable=False)
    wallets = db.relationship('Wallet', backref='character', lazy=True)


class Wallet(db.Model):
    """Model for wallets."""

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    character_id: Mapped[int] = mapped_column(db.ForeignKey('character.id'), nullable=False)
    transactions = db.relationship('Transaction', backref='wallet', lazy=True)


class Transaction(db.Model):
    """Model for transactions."""

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(db.Float, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.utcnow, nullable=False)
    wallet_id: Mapped[int] = mapped_column(db.ForeignKey('wallet.id'), nullable=False)


