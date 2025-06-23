from app.models import Hero, Power, HeroPower
from app import db, create_app
from faker import Faker
from random import choice as rc

app = create_app()
faker = Faker()

with app.app_context():
    print("Dropping existing tables...")
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()

    print("Creating new tables...")
    db.create_all()

    print("Seeding Heroes...")
    heroes = []
    for h in range(20):
        hero = Hero(name= faker.name(), super_name = faker.name())
        heroes.append(hero)

    db.session.add_all(heroes)
    db.session.commit()

    print("Seeding Powers...")
    # generate without using faker
    powers = [
        Power(name='Flight', description='Ability to fly for long distances and heights'),
        Power(name='Super Strength', description='Incredible physical strength beyond normal limits'),
        Power(name='Invisibility', description='Ability to become invisible at will'),
        Power(name='Telepathy', description='Ability to read minds and communicate mentally'),
        Power(name='Time Travel', description='Ability to travel through time and space'),
        Power(name='Telekinesis', description='Ability to move objects with the mind without physical interaction'),
        Power(name='Shape-shifting', description='Ability to change form or appearance at will'),
        Power(name='Healing Factor', description='Rapid healing from injuries and illnesses'),
        Power(name='Energy Blast', description='Ability to project energy blasts at targets'),
        Power(name='Super Speed', description='Incredible speed beyond normal limits and reflexes'),
    ]

    db.session.add_all(powers)
    db.session.commit()

    print("Seeding Hero Powers...")
    hero_powers = []
    existing_pairs = set()
    
    for hp in range(15):
        hero_id = rc(heroes).id
        power_id = rc(powers).id
        strength = rc(["Weak", "Average", "Strong"])
        while (hero_id, power_id) in existing_pairs:
            hero_id = rc(heroes).id
            power_id = rc(powers).id
        existing_pairs.add((hero_id, power_id))
        hero_power = HeroPower(
            hero_id=hero_id,
            power_id=power_id,
            strength=strength
        )
        hero_powers.append(hero_power)

    db.session.add_all(hero_powers)
    db.session.commit()