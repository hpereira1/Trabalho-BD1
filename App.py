from CRUD.Client import Client
from CRUD.Artist import Artist
from CRUD.Format import Format
from CRUD.Supplier import Supplier
from CRUD.Disc import Disc
from CRUD.Genre import Genre
# from CRUD.Client import Client
# from CRUD.Client import Client
# from CRUD.Client import Client
from DatabaseConnection import DatabaseConnection
from CLI.ClientsCLI import ClientsCLI
from CLI.ArtistsCLI import ArtistsCLI
from CLI.FormatsCLI import FormatsCLI
from CLI.SuppliersCLI import SuppliersCLI
from CLI.DiscsCLI import DiscsCLI
from CLI.GenresCLI import GenreCLI

class App:
    def __init__(self, clients_cli, artists_cli, suppliers_cli,formats_cli, discs_cli,genres_cli):
        self.clients_cli = clients_cli
        self.artists_cli = artists_cli
        self.suppliers_cli = suppliers_cli
        self.formats_cli = formats_cli
        self.discs_cli = discs_cli
        self.genres_cli = genres_cli

    def run(self):
        while True:
            print("\nMenu Principal:")
            print("1. Gerenciamento de Clientes")
            print("2. Gerenciamento de Artistas")
            print("3. Gerenciamento de Formatos")
            print("4. Gerenciamento de Suppliers")
            print("5. Gerenciamento de Genres")
            print("6. Gerenciamento de Discs")
            print("7. Sair")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.clients_cli.run()
            elif choice == '2':
                self.artists_cli.run()
            elif choice == '3':
                self.formats_cli.run()
            elif choice == '4':
                self.suppliers_cli.run()
            elif choice == '5':
                self.genres_cli.run()
                pass
            elif choice == '6':
                self.discs_cli.run()
            elif choice == '7':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")



# Configurações do banco de dados
db_host = 'localhost'
db_database = 'disco'
db_user = ''
db_password = ''

# Instanciando as classes
db_connection = DatabaseConnection(db_host, db_database, db_user, db_password)
client_crud = Client(db_connection)
clients_cli = ClientsCLI(client_crud)  # Instância de ClientsCLI
artist_crud = Artist(db_connection)
artists_cli = ArtistsCLI(artist_crud)
format_crud = Format(db_connection)
formats_cli = FormatsCLI(format_crud)
supplier_crud = Supplier(db_connection)
suppliers_cli = SuppliersCLI(supplier_crud)
disc_crud = Disc(db_connection)
discs_cli = DiscsCLI(disc_crud)
genre_crud = Genre(db_connection)
genres_cli = GenreCLI(genre_crud)
app = App(clients_cli, artists_cli, suppliers_cli, formats_cli, discs_cli, genres_cli) 

app.run()