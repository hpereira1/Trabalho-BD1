from CRUD.Client import Client
class ClientsCLI:
    def __init__(self, client_crud : Client):
        self.client_crud = client_crud    

    def run(self):
        while True:
            print("\nGerenciamento de Clientes:")
            print("1. Adicionar Cliente")
            print("2. Listar Clientes")
            print("3. Atualizar Cliente")
            print("4. Deletar Cliente")
            print("5. Ver Detalhes de um Cliente Específico")
            print("6. Atualizar Dado Específico de um Cliente")
            print("7. Retornar ao Menu Principal")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.add_client()
                continue
            elif choice == '2':
                self.list_clients()
                continue
                
            elif choice == '3':
                self.update_client()
                continue
                
            elif choice == '4':
                self.delete_client()
                continue
                
            if choice == '5':
                self.read_specific_client() 
                continue
                
            if choice == '6':
                self.update_specific_client()  
                continue
                     
            elif choice == '7':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")


    def add_client(self):
        while True:
            name = input("\nNome do cliente: ")
            if not name.strip():
                print("\nO nome do cliente não pode ser vazio. Por favor, insira um nome válido.")
                continue

            phone = input("\nTelefone do cliente: ")
            if not phone.strip():
                print("\nO número de telefone não pode ser vazio. Por favor, insira um número válido.")
                continue

            address = input("\nEndereço do cliente: ")
            if not address.strip():
                print("\nO endereço do cliente não pode ser vazio. Por favor, insira um endereço válido.")
                continue

            email = input("\nEmail do cliente: ")
            if not email.strip():
                print("\nO email não pode ser vazio. Por favor, insira um email válido.")
                continue

            break

        self.client_crud.create_client(name, phone, address, email)


    def list_clients(self):
        clients = self.client_crud.read_clients()
        for client in clients:
            print(client)
            
    def read_specific_client(self):
        client_id = input("Digite o ID do cliente que deseja visualizar: ")
        self.client_crud.read_client_by_id(client_id)
    
    def update_client(self):
        client_id = input("ID do cliente a ser atualizado: ")
        if not client_id.strip():
            print("O ID do cliente não pode ser vazio.")
            return

        # Verifica se o cliente existe
        if not self.client_crud.client_exists(client_id):
            print("Cliente não encontrado.")
            return

        name = input("Novo nome do cliente: ")
        while not name.strip():
            print("O nome do cliente não pode ser vazio.")
            name = input("Novo nome do cliente: ")

        phone = input("Novo telefone do cliente: ")
        while not phone.strip():
            print("O telefone do cliente não pode ser vazio.")
            phone = input("Novo telefone do cliente: ")

        address = input("Novo endereço do cliente: ")
        while not address.strip():
            print("O endereço do cliente não pode ser vazio.")
            address = input("Novo endereço do cliente: ")

        email = input("Novo email do cliente: ")
        while not email.strip():
            print("O email do cliente não pode ser vazio.")
            email = input("Novo email do cliente: ")

        self.client_crud.update_client(client_id, name, phone, address, email)

        
    def update_specific_client(self):
        client_id = input("Digite o ID do cliente que deseja atualizar: ")

        # Verifica se o cliente existe
        if not self.client_crud.client_exists(client_id):
            print("Cliente não encontrado.")
            return

        field = input("Digite o campo que deseja atualizar (name, phone, address, email): ")
        valid_fields = ['name', 'phone', 'address', 'email']

        # Verifica se o campo é válido
        if field not in valid_fields:
            print("Campo inválido. Escolha entre 'name', 'phone', 'address', 'email'.")
            return

        new_value = input(f"Digite o novo valor para o campo {field}: ")
        while not new_value.strip():
            print(f"O valor para {field} não pode ser vazio.")
            new_value = input(f"Digite o novo valor para o campo {field}: ")
        self.client_crud.update_specific_client_data(client_id, field, new_value)
        
    def delete_client(self):
        client_id = input("ID do cliente a ser removido: ")
        # Verifica se o cliente existe
        if not self.client_crud.client_exists(client_id):
            print("Cliente não encontrado.")
            return
        
        self.client_crud.delete_client(client_id)
    
    