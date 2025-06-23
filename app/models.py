from app import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-powers.heroes',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    super_name = db.Column(db.String(30), nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')
    def _repr_(self):
        return f'<Hero {self.name} ({self.super_name})>'

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_rules = ('-heroes.powers',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String, nullable=True)

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    @validates('description')
    def validate_description(self, key, description):
        print(f"Validating field '{key}' with value '{description}'")
        if description and len(description) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return description

    def _repr_(self):
        return f'<Power {self.name}>'

class HeroPower(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    serialize_rules = ('-hero.powers', '-power.heroes')

    strength = db.Column(db.Integer, nullable=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), primary_key=True)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    @validates('strength')
    def validate_strength(self, key, strength):
        print(f"Validating field '{key}' with value '{strength}'")
        if strength not in ["Weak", "Average", "Strong"]:
            raise ValueError("Strength must be either 'Weak', 'Average', or 'Strong'.")
        return strength

    def _repr_(self):
        return f'<HeroPower {self.hero.name} - {self.power.name}>'