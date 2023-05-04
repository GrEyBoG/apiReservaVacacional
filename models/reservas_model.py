class ReservasModel:
    def __init__(self, mysql):
        self.mysql = mysql
        
    def get_reservas(self):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('SELECT * FROM reservas')
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception as e:
            print('ERROR: ', e)
    
    def get_reserva(self, id):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute(
                'SELECT * FROM reservas WHERE reservaId = %s', (id,))
            result = cursor.fetchone()
            cursor.close()
            return result
        except Exception as e:
            print('ERROR: ', e)

        
    def insert_reserva(self, reserva):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('INSERT INTO reservas (email, firstName, lastName, phoneNumber, daysAmount, peopleAmount) VALUES (%s, %s, %s, %s, %s, %s)', (reserva['email'], reserva['firstName'], reserva['lastName'], reserva['phoneNumber'], reserva['daysAmount'], reserva['peopleAmount']))
            self.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print('ERROR: ', e)

            
    def delete_reserva(self, id):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute('DELETE FROM reservas WHERE reservaId = %s', (id,))
            self.mysql.connection.commit()
        except Exception as e:
            print('ERROR: ', e)
    