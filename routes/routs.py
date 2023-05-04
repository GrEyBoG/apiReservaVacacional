from flask import Blueprint
from controllers.reserva_controller import get_reservas, get_reserva, insert_reserva, delete_reserva

routes = Blueprint('routes', __name__)

routes.route('/reservas', methods=['GET'])(get_reservas)
routes.route('/reservas/<id>', methods=['GET'])(get_reserva)
routes.route('/reservas', methods=['POST'])(insert_reserva)
routes.route('/reservas/<id>', methods=['DELETE'])(delete_reserva)
