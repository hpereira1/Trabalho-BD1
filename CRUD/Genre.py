import mysql.connector
from mysql.connector import Error

class Genre:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def genre_exists(self, genre_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM Genres WHERE genre_id = %s)"
            cursor.execute(query, (genre_id,))
            return cursor.fetchone()[0]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def create_genre(self, name):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO Genres (name) VALUES (%s)"
            cursor.execute(query, (name,))
            connection.commit()
            print("Genero adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar genero: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            
    def read_genre(self):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Genres"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erro ao ler os generos: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_genre_by_id(self, genre_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Genres WHERE genre_id = %s"
            cursor.execute(query, (genre_id,))
            record = cursor.fetchone()
            if record:
                print("Detalhes do Genero:", record)
            else:
                print(f"Nenhum genero encontrado com o ID: {genre_id}")
        except Error as e:
            print(f"Erro ao ler o genero: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def update_genre(self, genre_id, name):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "UPDATE Genres SET name = %s WHERE genre_id = %s"
            cursor.execute(query, (name, genre_id))
            connection.commit()
            print("Genero atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar genre: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def update_specific_genre_data(self, genre_id, field, new_value):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = f"UPDATE Genres SET {field} = %s WHERE genre_id = %s"
            cursor.execute(query, (new_value, genre_id))
            connection.commit()
            print(f"Dado do genero atualizado com sucesso: {field} = {new_value}")
        except Error as e:
            print(f"Erro ao atualizar o genero: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_genre(self, genre_id):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM Genres WHERE genre_id = %s"
            cursor.execute(query, (genre_id,))
            connection.commit()
            print("Genero removido com sucesso.")
        except Error as e:
            print(f"Erro ao remover genero: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()