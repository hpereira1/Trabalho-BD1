from CRUD.Genre import Genre
class GenreCLI:
    def __init__(self, genre_crud : Genre):
        self.genre_crud = genre_crud    

    def run(self):
        print(type(self.genre_crud))
        
        while True:
            print("\nGerenciamento de generos:")
            print("1. Adicionar genero")
            print("2. Listar generos")
            print("3. Atualizar genero")
            print("4. Deletar genero")
            print("5. Ver Detalhes de um genero Específico")
            print("6. Atualizar Dado Específico de um genero")
            print("7. Retornar ao Menu Principal")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.add_genre()
                continue
            elif choice == '2':
                self.list_genre()
                continue
                
            elif choice == '3':
                self.update_genre()
                continue
                
            elif choice == '4':
                self.delete_genre()
                continue
                
            if choice == '5':
                self.read_specific_genre() 
                continue
                
            if choice == '6':
                self.update_specific_genre()  
                continue
                     
            elif choice == '7':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")


    def add_genre(self):
        while True:
            name = input("\nNome do genero: ")
            if not name.strip():
                print("\nO nome do genero não pode ser vazio. Por favor, insira um nome válido.")
            break

        self.genre_crud.create_genre(name)


    def list_genre(self):
        genres = self.genre_crud.read_genre()
        for genre in genres:
            print(genre)
            
    def read_specific_genre(self):
        genre_id = input("Digite o ID do genero que deseja visualizar: ")
        self.genre_crud.read_genre_by_id(genre_id)
    
    def update_genre(self):
        genre_id = input("ID do genero a ser atualizado: ")
        if not genre_id.strip():
            print("O ID do genero não pode ser vazio.")
            return

        # Verifica se o genero existe
        if not self.genre_crud.genre_exists(genre_id):
            print("genero não encontrado.")
            return

        name = input("Novo nome do genero: ")
        while not name.strip():
            print("O nome do genero não pode ser vazio.")
            name = input("Novo nome do genero: ")

        self.genre_crud.update_genre(genre_id, name)

        
    def update_specific_genre(self):
        genre_id = input("Digite o ID do genero que deseja atualizar: ")

        # Verifica se o genero existe
        if not self.genre_crud.genre_exists(genre_id):
            print("genero não encontrado.")
            return

        field = input("Digite o campo que deseja atualizar (name, phone, address, email): ")
        valid_fields = ['name']

        # Verifica se o campo é válido
        if field not in valid_fields:
            print("Campo inválido.")
            return

        new_value = input(f"Digite o novo valor para o campo {field}: ")
        while not new_value.strip():
            print(f"O valor para {field} não pode ser vazio.")
            new_value = input(f"Digite o novo valor para o campo {field}: ")
        self.genre_crud.update_specific_genre_data(genre_id, field, new_value)
        
    def delete_genre(self):
        genre_id = input("ID do genero a ser removido: ")
        # Verifica se o genero existe
        if not self.genre_crud.genre_exists(genre_id):
            print("genero não encontrado.")
            return
        
        self.genre_crud.delete_genre(genre_id)
    