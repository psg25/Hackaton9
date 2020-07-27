from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/hackatons9'
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['usuario']
    password = request.json['contrasena']
    email = request.json['email']
    if username and email and password:

        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'usuario':username, 'email':email, 'contrasena':password}
            )
        response = {
            'id': str(id),
            'usuario': username,
            'contrasena': hashed_password,
            'email': email
        }
        return response
    else:
        return not_found()

@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')

@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id':ObjectId(id)})
    response = jsonify({'message': 'El usuario'+id+'fue eliminado'})
    return response

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    username = request.json['usuario']
    password = request.json['contrasena']
    email = request.json['email']

    if username and password and email:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one({'_id':ObjectId(id)}, {'$set':{
            'usuario':username,
            'contrasena': hashed_password,
            'email': email
        }})
        response = jsonify({'message': 'El usuario '+id+'fue actualizado'})
    return response

@app.errorhandler(404)
def not_found(erros=None):
    response = jsonify({
            'message': 'No se encontro el dato: '+ request.url,
            'status': 404
        })
    response.status_code = 404
    return response

if __name__== '__main__':
    app.run(debug=True)

