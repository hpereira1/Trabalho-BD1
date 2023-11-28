import mysql.connector
from mysql.connector import Error

class Disc:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def disc_exists(self, disc_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM Discs WHERE disc_id = %s)"
            cursor.execute(query, (disc_id,))
            return cursor.fetchone()[0]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

 
    def create_disc(self, title, artist_id, genre_id, format_id, price):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO Discs (title, artist_id, genre_id, format_id, price) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (title, artist_id, genre_id, format_id, price))
            connection.commit()
            print("disc adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar disc: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            
    def read_discs(self):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Discs"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erro ao ler os discs: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_disc_by_id(self, disc_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Discs WHERE disc_id = %s"
            cursor.execute(query, (disc_id,))
            record = cursor.fetchone()
            if record:
                print("Detalhes do disc:", record)
            else:
                print(f"Nenhum disc encontrado com o ID: {disc_id}")
        except Error as e:
            print(f"Erro ao ler o disc: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def update_disc(self, disc_id, title, artist_id, genre_id, format_id, price):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "UPDATE Discs SET title = %s, artist_id = %s, genre_id = %s, format_id = %s, price = %s WHERE disc_id = %s"
            cursor.execute(query, (title, artist_id, genre_id, format_id, price, disc_id))
            connection.commit()
            print("disc atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar disce: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

def delete_disc(self):
    disc_id = input("ID do disco a ser removido: ")

    # Verifica se o disco existe
    if not self.disc_crud.disc_exists(disc_id):
        print("Disco não encontrado.")
        return

    # Verifica se o disco está sendo referenciado em 'Orders'
    if self.disc_crud.is_disc_referenced_in_orders(disc_id):
        choice = input("Disco está em pedidos. Deseja remover todos os pedidos relacionados? (s/n): ")
        if choice.lower() == 's':
            self.disc_crud.delete_related_orders(disc_id)
        else:
            print("Operação cancelada.")
            return

    self.disc_crud.delete_disc(disc_id)
    print("Disco removido com sucesso.")

    def delete_related_orders(self, disc_id):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM Orders WHERE disc_id = %s"
            cursor.execute(query, (disc_id,))
            connection.commit()
            print(f"Todos os pedidos relacionados ao disco com ID {disc_id} foram removidos.")
        except Error as e:
            print(f"Erro ao remover pedidos relacionados: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()