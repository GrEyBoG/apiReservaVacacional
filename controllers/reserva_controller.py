from flask import request, jsonify, Blueprint
from models.reservas_model import ReservasModel

reservasController = Blueprint('reservasController', __name__)

def initReservasController(app, mySQL):
    global ReservasModel
    ReservasModel = ReservasModel(mySQL)
    
    app.register_blueprint(reservasController)
    
def get_reservas():
    try:
        return jsonify(ReservasModel.get_reservas())
    except Exception as e:
        return jsonify({'message': 'ERROR: ' + str(e)})
        print('ERROR: ', e)
        
def get_reserva(id):
    try:
        return jsonify(ReservasModel.get_reserva(id))
    except Exception as e:
        return jsonify({'message': 'ERROR: ' + str(e)})
        print('ERROR: ', e)
        
def insert_reserva():
    try: 
        newReserva = {
            "email": request.json['email'],
            "firstName": request.json['firstName'],
            "lastName": request.json['lastName'],
            "phoneNumber": request.json['phoneNumber'],
            "daysAmount": request.json['daysAmount'],
            "peopleAmount": request.json['peopleAmount']
        }
        ReservasModel.insert_reserva(newReserva)
        return jsonify({'message': 'reserva Added Succesfully'})
    except Exception as e:
        return jsonify({'message': 'ERROR: ' + str(e)})
        print('ERROR: ', e)
        
def delete_reserva(id):
    try:
        ReservasModel.delete_reserva(id)
        return jsonify({'message': 'reserva Deleted Succesfully'})
    except Exception as e:
        return jsonify({'message': 'ERROR: ' + str(e)})
        print('ERROR: ', e)


    
