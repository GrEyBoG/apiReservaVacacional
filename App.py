from flask import Flask
from flask_cors import CORS
from database.db import init_database
from routes.routs import routes
from controllers.reserva_controller import initReservasController

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes)

mySQL = init_database(app)
initReservasController(app, mySQL)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
