from datetime import datetime

from app import db

class User(db.Model):
    """Model for user accounts."""

    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(80), unique=True, nullable=False)
    email: str = db.Column(db.String(120), unique=True, nullable=False)
    characters = db.relationship('Character', backref='user', lazy=True)


class Character(db.Model):
    """Model for characters."""

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), nullable=False)
    user_id: int = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    wallets = db.relationship('Wallet', backref='character', lazy=True)


class Wallet(db.Model):
    """Model for wallets."""

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(80), nullable=False)
    character_id: int = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    transactions = db.relationship('Transaction', backref='wallet', lazy=True)


class Transaction(db.Model):
    """Model for transactions."""

    id: int = db.Column(db.Integer, primary_key=True)
    amount: float = db.Column(db.Float, nullable=False)
    timestamp: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    wallet_id: int = db.Column(db.Integer, db.ForeignKey('wallet.id'), nullable=False)


