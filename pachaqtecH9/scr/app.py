from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO URI']='mongodb://localhost:27017/hackatons9'
mongo = PyMongo(app)

@app.route('/users', methods=['POST'])
def create_user():
    return {'message':'recibido'}

if __name__== '__main__':
    app.run(debug=True)

