
import mysql.connector
from mysql.connector import Error

class Format:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def format_exists(self, format_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM Formats WHERE format_id = %s)"
            cursor.execute(query, (format_id,))
            return cursor.fetchone()[0]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def create_format(self, name):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO Formats (name) VALUES (%s)"
            cursor.execute(query, (name,))
            connection.commit()
            print("Formato adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar Formato: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
            connection.close()

            
    def read_formats(self):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Formats"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erro ao ler os Formatos: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_format_by_id(self, format_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Formats WHERE format_id = %s"
            cursor.execute(query, (format_id,))
            record = cursor.fetchone()
            if record:
                print("Detalhes do Formato:", record)
            else:
                print(f"Nenhum Formato encontrado com o ID: {format_id}")
        except Error as e:
            print(f"Erro ao ler o Formato: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def update_format(self, format_id, name):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "UPDATE Formats SET name = %s WHERE format_id = %s"
            cursor.execute(query, (name, format_id))
            connection.commit()
            print("Formato atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar Formato: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def update_specific_format_data(self, format_id, field, new_value):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = f"UPDATE Formats SET {field} = %s WHERE format_id = %s"
            cursor.execute(query, (new_value, format_id))
            connection.commit()
            print(f"Dado do Formato atualizado com sucesso: {field} = {new_value}")
        except Error as e:
            print(f"Erro ao atualizar o Formato: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_format(self, format_id):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM Formats WHERE format_id = %s"
            cursor.execute(query, (format_id,))
            connection.commit()
            print("Formato removido com sucesso.")
        except Error as e:
            print(f"Erro ao remover Formato: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()