import mysql.connector
from mysql.connector import Error
class Supplier:
    def __init__(self, db_connection):
        self.db_connection = db_connection


    def supplier_exists(self, supplier_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            return False

        try:
            cursor = connection.cursor()
            query = "SELECT EXISTS(SELECT 1 FROM Suppliers WHERE supplier_id = %s)"
            cursor.execute(query, (supplier_id,))
            return cursor.fetchone()[0]
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def create_supplier(self, phone, email, address, cnpj, name):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "INSERT INTO Suppliers (phone, email, address, cnpj, name) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (phone, email, address, cnpj, name))
            connection.commit()
            print("supplier adicionado com sucesso.")
        except Error as e:
            print(f"Erro ao adicionar supplier: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
            
    def read_suppliers(self):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM Suppliers"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Error as e:
            print(f"Erro ao ler os suppliers: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def read_supplier_by_id(self, supplier_id):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = "SELECT * FROM Suppliers WHERE supplier_id = %s"
            cursor.execute(query, (supplier_id,))
            record = cursor.fetchone()
            if record:
                print("Detalhes do suppliere:", record)
            else:
                print(f"Nenhum supplier encontrado com o ID: {supplier_id}")
        except Error as e:
            print(f"Erro ao ler o supplier: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                
    def update_supplier(self, supplier_id, phone, email, address, cnpj, name):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "UPDATE Suppliers SET phone = %s, email = %s, address = %s, cnpj = %s, name = %s WHERE supplier_id = %s"
            cursor.execute(query, (phone, email, address, cnpj, name, supplier_id))
            connection.commit()
            print("supplier atualizado com sucesso.")
        except Error as e:
            print(f"Erro ao atualizar supplier: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def update_specific_supplier_data(self, supplier_id, field, new_value):
        connection = self.db_connection.create_connection()
        if connection is None:
            print("Não foi possível estabelecer uma conexão com o banco de dados.")
            return

        try:
            cursor = connection.cursor()
            query = f"UPDATE Suppliers SET {field} = %s WHERE supplier_id = %s"
            cursor.execute(query, (new_value, supplier_id))
            connection.commit()
            print(f"Dado do supplier atualizado com sucesso: {field} = {new_value}")
        except Error as e:
            print(f"Erro ao atualizar o supplier: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def delete_supplier(self, supplier_id):
        try:
            connection = self.db_connection.create_connection()
            cursor = connection.cursor()
            query = "DELETE FROM Suppliers WHERE supplier_id = %s"
            cursor.execute(query, (supplier_id,))
            connection.commit()
            print("supplier removido com sucesso.")
        except Error as e:
            print(f"Erro ao remover supplier: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
