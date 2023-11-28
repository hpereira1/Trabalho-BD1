from CRUD.Supplier import Supplier
class SuppliersCLI:
    def __init__(self, supplier_crud: Supplier):
        self.supplier_crud = supplier_crud

    def run(self):
        while True:
            print("\nGerenciamento de Fornecedores:")
            print("1. Adicionar Fornecedor")
            print("2. Listar Fornecedores")
            print("3. Atualizar Fornecedor")
            print("4. Deletar Fornecedor")
            print("5. Ver Detalhes de um Fornecedor Específico")
            print("6. Atualizar Dado Específico de um Fornecedor")
            print("7. Retornar ao Menu Principal")

            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.add_supplier()
            elif choice == '2':
                self.list_suppliers()
            elif choice == '3':
                self.update_supplier()
            elif choice == '4':
                self.delete_supplier()
            elif choice == '5':
                self.read_specific_supplier()
            elif choice == '6':
                self.update_specific_supplier()
            elif choice == '7':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")



    def add_supplier(self):
        while True:
            phone = input("\nTelefone do supplier: ")
            if not phone.strip():
                print("\nO número de telefone não pode ser vazio. Por favor, insira um número válido.")
                continue

            email = input("\nEmail do supplier: ")
            if not email.strip():
                print("\nO email não pode ser vazio. Por favor, insira um email válido.")
                continue
            
            address = input("\nEndereço do supplier: ")
            if not address.strip():
                print("\nO endereço do supplier não pode ser vazio. Por favor, insira um endereço válido.")
                continue
            
            cnpj = input("\nCNPJ do supplier: ")
            if not address.strip():
                print("\nO cnpj do supplier não pode ser vazio. Por favor, insira um cnpj válido.")
                continue
                
            name = input("\nNome do supplier: ")
            if not name.strip():
                print("\nO nome do supplier não pode ser vazio. Por favor, insira um nome válido.")
                continue
            break

        self.supplier_crud.create_supplier(phone, email, address, cnpj, name)


    def list_suppliers(self):
        suppliers = self.supplier_crud.read_suppliers()
        for supplier in suppliers:
            print(supplier)
            
    def read_specific_supplier(self):
        supplier_id = input("Digite o ID do supplier que deseja visualizar: ")
        self.supplier_crud.read_supplier_by_id(supplier_id)
    
    def update_supplier(self):
        supplier_id = input("ID do supplier a ser atualizado: ")
        if not supplier_id.strip():
            print("O ID do supplier não pode ser vazio.")
            return

        # Verifica se o suppliere existe
        if not self.supplier_crud.supplier_exists(supplier_id):
            print("supplier não encontrado.")
            return
        
        phone = input("\nNovo Telefone do supplier: ")
        while not phone.strip():
            print("\nO número de telefone não pode ser vazio. Por favor, insira um número válido.")
            phone = input("\nNOvvo Telefone do supplier: ")


        email = input("\nnovo Email do supplier: ")
        while not email.strip():
            print("\nO email não pode ser vazio. Por favor, insira um email válido.")
            email = input("\nnovo Email do supplier: ")

        
        address = input("\nnovo Endereço do supplier: ")
        while not address.strip():
            print("\nO endereço do supplier não pode ser vazio. Por favor, insira um endereço válido.")
            address = input("\nnovo Endereço do supplier: ")

        
        cnpj = input("\nnovo CNPJ do supplier: ")
        while not address.strip():
            print("\nO cnpj do supplier não pode ser vazio. Por favor, insira um cnpj válido.")
            cnpj = input("\nnovo CNPJ do supplier: ")

            
        name = input("\nNome do supplier: ")
        while not name.strip():
            print("\nO nome do supplier não pode ser vazio. Por favor, insira um nome válido.")
            name = input("\nNome do supplier: ")

        self.supplier_crud.update_supplier(supplier_id, phone, email, address, cnpj, name)

        
    def update_specific_supplier(self):
        supplier_id = input("Digite o ID do suppliere que deseja atualizar: ")

        # Verifica se o suppliere existe
        if not self.supplier_crud.supplier_exists(supplier_id):
            print("suppliere não encontrado.")
            return

        field = input("Digite o campo que deseja atualizar (phone, email, address, cnpj, name): ")
        valid_fields = ['phone', 'email', 'address', 'cnpj', 'name']

        # Verifica se o campo é válido
        if field not in valid_fields:
            print("Campo inválido. Escolha entre 'phone', 'email', 'address', 'cnpj', 'name'.")
            return

        new_value = input(f"Digite o novo valor para o campo {field}: ")
        while not new_value.strip():
            print(f"O valor para {field} não pode ser vazio.")
            new_value = input(f"Digite o novo valor para o campo {field}: ")
        self.supplier_crud.update_specific_supplier_data(supplier_id, field, new_value)
        
    def delete_supplier(self):
        supplier_id = input("ID do supplier a ser removido: ")
        if not self.supplier_crud.supplier_exists(supplier_id):
            print("supplier não encontrado.")
            return
        
        self.supplier_crud.delete_supplier(supplier_id)
    
    
