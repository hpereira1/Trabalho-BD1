from CRUD.Artist import Artist
class ArtistsCLI:
    def __init__(self, artist_crud : Artist):
        self.artist_crud = artist_crud

    def run(self):
        while True:
            print("\nGerenciamento de Artistas:")
            print("1. Adicionar Artista")
            print("2. Listar Artistas")
            print("3. Atualizar Artista")
            print("4. Deletar Artista")
            print("5. Ver Detalhes de um Artista Específico")
            print("6. Atualizar Dado Específico de um Artista")
            print("5. Retornar ao Menu Principal")

            choice = input("Escolha uma opção: ")
            
            if choice == '1':
                self.add_artist()
                continue
            elif choice == '2':
                self.list_artists()
                continue
                
            elif choice == '3':
                self.update_artist()
                continue
                
            elif choice == '4':
                self.delete_artist()
                continue
                
            if choice == '5':
                self.read_specific_artist() 
                continue
                
            if choice == '6':
                self.update_specific_artist()  
                continue
                     
            elif choice == '7':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

    def add_artist(self):
        while True:
            name = input("\nNome do artista: ")
            if not name.strip():
                print("O nome do artista não pode ser vazio.")
                continue

            country = input("País do artista: ")
            if not country.strip():
                print("O pais do artista não pode ser vazio.")
                continue
            break
        self.artist_crud.create_artist(name, country)
    

    def list_artists(self):
        artists = self.artist_crud.read_artists()
        for artist in artists:
            print(artist)

    def update_artist(self):
        artist_id = input("ID do artista a ser atualizado: ")
        if not artist_id.strip():
            print("O ID do artista não pode ser vazio.")
            return
        
        if not self.artist_crud.artist_exists(artist_id):
            print("Artista não encontrado.")
            return

        name = input("Novo nome do artista: ")
        while not name.strip():
            print("O nome do artiste não pode ser vazio.")
            name = input("Novo nome do artiste: ")
            
        country = input("Novo país do artista: ")
        while not country.strip():
            print("O pais do artista não pode ser vazio.")
            country = input("Novo país do artista: ")

            
        self.artist_crud.update_artist(artist_id, name, country)
        print("Artista atualizado com sucesso.")
        
    def read_specific_artist(self):
        artist_id = input("Digite o ID do artist que deseja visualizar: ")
        self.artist_crud.read_artist_by_id(artist_id)
        
    def update_specific_artist(self):
        artist_id = input("Digite o ID do artist que deseja atualizar: ")

        # Verifica se o artiste existe
        if not self.artist_crud.artist_exists(artist_id):
            print("artist não encontrado.")
            return

        field = input("Digite o campo que deseja atualizar (name, country): ")
        valid_fields = ['name', 'country']

        # Verifica se o campo é válido
        if field not in valid_fields:
            print("Campo inválido. Escolha entre 'name', 'country'.")
            return

        new_value = input(f"Digite o novo valor para o campo {field}: ")
        while not new_value.strip():
            print(f"O valor para {field} não pode ser vazio.")
            new_value = input(f"Digite o novo valor para o campo {field}: ")
        self.artist_crud.update_specific_artist_data(artist_id, field, new_value)

    def delete_artist(self):
        artist_id = input("ID do artist a ser removido: ")
        # Verifica se o artiste existe
        if not self.artist_crud.artist_exists(artist_id):
            print("artist não encontrado.")
            return
        
        self.artist_crud.delete_artist(artist_id)
    