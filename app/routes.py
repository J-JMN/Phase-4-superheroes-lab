from flask import Blueprint, request, make_response, jsonify
from .models import Hero, Power, HeroPower
import json
from app import db

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return "<h1>Welcome to the Superhero API!</h1>"


@api.route('/heroes')
def get_heroes():
    heroes = Hero.query.all()

    hero_list = [{
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
    }for hero in heroes] 

    pretty_json = json.dumps(hero_list, indent=4)

    response = make_response(pretty_json, 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@api.route('/heroes/<int:hero_id>')
def hero_by_id(hero_id):
    hero = Hero.query.filter_by(id = hero_id).first()

    if not hero:
        return jsonify({'error': 'Hero not found'}), 404

    hero_list = [{
        'id': hero.id,
        'name': hero.name,
        'super_name': hero.super_name,
        'hero_powers': [{
            'hero_id': hp.hero_id,
            'id': hp.power.id,
            'powers': [{
                'description': hp.power.description,
                'id': hp.power.id,
                'name': hp.power.name,
            }]
        } for hp in hero.hero_powers]
    }]

    pretty_json = json.dumps(hero_list, indent=4)
    response = make_response(pretty_json, 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@api.route('/powers')
def get_powers():
    powers = Power.query.all()

    power_list = [{
        'description': power.description,
        'id': power.id,
        'name': power.name,
    } for power in powers]

    pretty_json = json.dumps(power_list, indent=4)

    response = make_response(pretty_json, 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@api.route('/powers/<int:power_id>')
def power_by_id(power_id):
    power = Power.query.filter_by(id=power_id).first()

    if not power:
        return jsonify({'error': 'Power not found'}), 404

    power_list = [{
        'description': power.description,
        'id': power.id,
        'name': power.name,
        } for hp in power.hero_powers]
    

    pretty_json = json.dumps(power_list, indent=4)
    response = make_response(pretty_json, 200)
    response.headers['Content-Type'] = 'application/json'
    return response

@api.route('/powers/<int:power_id>', methods = ['PATCH'])
def update_power(power_id):
    power = Power.query.filter_by(id = power_id).first()

    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()

    description = data.get('description')
    if not description or not isinstance(description, str) or description.strip() == "":
        return jsonify({'error': 'Validation errors'}), 404
    
    power.description = description
    db.session.commit()

    return jsonify({
        'message': 'Power updated successfully',        
        'power': {
            'description': power.description,
            'id': power.id,
            'name': power.name,
        }
    })


@api.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    if not hero_id or not power_id or not strength:
        return jsonify ({'error': 'Validation errors'}), 400
    
    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({'error': 'Hero or Power not found'}), 404
    
    existing = HeroPower.query.filter_by(hero_id=hero_id, power_id=power_id).first()
    if existing:
        return jsonify({'error': 'Hero already has this power'}), 400

    
    hero_power = HeroPower(
        hero_id=hero_id,
        power_id=power_id,
        strength=strength
    )   
    db.session.add(hero_power)
    db.session.commit()

    return jsonify({
        'hero_id': hero.id,
        'power_id': power.id,
        'strength': hero_power.strength,
        'hero': {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name
        },
        'power': {
            'id': power.id,
            'name': power.name,
            'description': power.description
      }
    }), 201