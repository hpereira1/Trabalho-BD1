import mysql.connector
from mysql.connector import Error

class Client:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def client_exists(self, client_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM Clients WHERE client_id = %s)"
            cursor.execute(query, (client_id,))
            return cursor.fetchone()[0]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def create_client(self, name, phone, address, email):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO Clients (name, phone, address, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, phone, address, email))
            connection.commit()
            print("Cliente adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar cliente: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            
    def read_clients(self):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Clients"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erro ao ler os clientes: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_client_by_id(self, client_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Clients WHERE client_id = %s"
            cursor.execute(query, (client_id,))
            record = cursor.fetchone()
            if record:
                print("Detalhes do Cliente:", record)
            else:
                print(f"Nenhum cliente encontrado com o ID: {client_id}")
        except Error as e:
            print(f"Erro ao ler o cliente: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def update_client(self, client_id, name, phone, address, email):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "UPDATE Clients SET name = %s, phone = %s, address = %s, email = %s WHERE client_id = %s"
            cursor.execute(query, (name, phone, address, email, client_id))
            connection.commit()
            print("Cliente atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar cliente: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def update_specific_client_data(self, client_id, field, new_value):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = f"UPDATE Clients SET {field} = %s WHERE client_id = %s"
            cursor.execute(query, (new_value, client_id))
            connection.commit()
            print(f"Dado do cliente atualizado com sucesso: {field} = {new_value}")
        except Error as e:
            print(f"Erro ao atualizar o cliente: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_client(self, client_id):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM Clients WHERE client_id = %s"
            cursor.execute(query, (client_id,))
            connection.commit()
            print("Cliente removido com sucesso.")
        except Error as e:
            print(f"Erro ao remover cliente: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
