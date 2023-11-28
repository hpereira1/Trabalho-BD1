import mysql.connector
from mysql.connector import Error

class Artist:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def artist_exists(self, artist_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM Artists WHERE artist_id = %s)"
            cursor.execute(query, (artist_id,))
            return cursor.fetchone()[0]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def create_artist(self, name, country):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO Artists (name, Country) VALUES (%s, %s)"
            cursor.execute(query, (name, country))
            connection.commit()
            print("Artista adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar artista: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()


    def read_artists(self):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Artists"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erro ao ler os artistas: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_artist_by_id(self, artist_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Artists WHERE artist_id = %s"
            cursor.execute(query, (artist_id,))
            record = cursor.fetchone()
            if record:
                print("Detalhes do artist:", record)
            else:
                print(f"Nenhum artist encontrado com o ID: {artist_id}")
        except Error as e:
            print(f"Erro ao ler o artist: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_artist(self, artist_id, name, country):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "UPDATE Artists SET name = %s, country = %s WHERE artist_id = %s"
            cursor.execute(query, (name, country, artist_id))
            connection.commit()
            print("artist atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar artiste: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def update_specific_artist_data(self, artist_id, field, new_value):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = f"UPDATE Artists SET {field} = %s WHERE artist_id = %s"
            cursor.execute(query, (new_value, artist_id))
            connection.commit()
            print(f"Dado do artista atualizado com sucesso: {field} = {new_value}")
        except Error as e:
            print(f"Erro ao atualizar o artista: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_artist(self, artist_id):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM Artists WHERE artist_id = %s"
            cursor.execute(query, (artist_id,))
            connection.commit()
            print("Artista removido com sucesso.")
        except Error as e:
            print(f"Erro ao remover artista: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()