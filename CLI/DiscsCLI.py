class DiscsCLI:
    def __init__(self, disc_crud):
        self.disc_crud = disc_crud

    def run(self):
        while True:
            print("\nGerenciamento de Discos:")
            print("1. Adicionar Disco")
            print("2. Listar Discos")
            print("3. Atualizar Disco")
            print("4. Deletar Disco")
            print("5. Ver Detalhes de um Disco Específico")
            print("6. Retornar ao Menu Principal")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.add_disc()
            elif choice == '2':
                self.list_discs()
            elif choice == '3':
                self.update_disc()
            elif choice == '4':
                self.delete_disc()
            elif choice == '5':
                self.read_specific_disc()
            elif choice == '6':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

    def add_disc(self):
        while True:
            title = input("\ntitulo do disc: ")
            if not title.strip():
                print("\nO titulo do disc não pode ser vazio. Por favor, insira um  válido.")
                continue

            artist_id = input("\nartist_id do disc: ")
            if not artist_id.strip():
                print("\nO artist_id não pode ser vazio. Por favor, insira um número válido.")
                continue

            genre_id = input("\ngenre_id do disc: ")
            if not genre_id.strip():
                print("\nO genre_id do disc não pode ser vazio. Por favor, insira um  válido.")
                continue

            format_id = input("\nformat_id do disc: ")
            if not format_id.strip():
                print("\nO format_id não pode ser vazio. Por favor, insira um  válido.")
                continue

            price = input("\nprice do disc: ")
            if not price.strip():
                print("\nO price não pode ser vazio. Por favor, insira um  válido.")
                continue
            if not price.isdigit():
                print("\nO price é float. Por favor, insira um  válido.")
                continue
            break

        self.disc_crud.create_disc(title, artist_id, genre_id, format_id, price)

    def list_discs(self):
        discs = self.disc_crud.read_discs()
        for disc in discs:
            print(disc)

    def read_specific_disc(self):
        disc_id = input("Digite o ID do disc que deseja visualizar: ")
        self.disc_crud.read_disc_by_id(disc_id)

    def update_disc(self):

        while True:
            title = input("\ntitulo do disc: ")
            if not title.strip():
                print("\nO titulo do disc não pode ser vazio. Por favor, insira um  válido.")
                continue

            artist_id = input("\nartist_id do disc: ")
            if not artist_id.strip():
                print("\nO artist_id não pode ser vazio. Por favor, insira um número válido.")
                continue

            genre_id = input("\nEndereço do disc: ")
            if not genre_id.strip():
                print("\nO genre_id do disc não pode ser vazio. Por favor, insira um  válido.")
                continue

            format_id = input("\nformat_id do disc: ")
            if not format_id.strip():
                print("\nO format_id não pode ser vazio. Por favor, insira um  válido.")
                continue

            price = input("\nNovoprice do disc: ")
            if not price.strip():
                print("\nO price não pode ser vazio. Por favor, insira um  válido.")
                continue
            if not price.isdigit():
                print("\nO price é float. Por favor, insira um  válido.")
                continue
            break

        self.disc_crud.update_disc(title, artist_id, genre_id, format_id, price)

    def delete_disc(self):
        disc_id = input("ID do disc a ser removido: ")
        # Verifica se o disce existe
        if not self.disc_crud.disc_exists(disc_id):
            print("disc não encontrado.")
            return
        
        self.disc_crud.delete_disc(disc_id)
        
