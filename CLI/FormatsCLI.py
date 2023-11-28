from CRUD.Format import Format
class FormatsCLI:
    def __init__(self, format_crud: Format):
        self.format_crud = format_crud

    def run(self):
        while True:
            print("\nGerenciamento de Formatos:")
            print("1. Adicionar Formato")
            print("2. Listar Formato")
            print("3. Atualizar Formato")
            print("4. Deletar Formato")
            print("5. Ver Detalhes de um Formato Específico")
            print("6. Atualizar Dado Específico de um Formato")
            print("7. Retornar ao Menu Principal")

            choice = input("Escolha uma opção: ")
            
            if choice == '1':
                self.add_format()
                continue
            elif choice == '2':
                self.list_formats()
                continue
                
            elif choice == '3':
                self.update_format()
                continue
                
            elif choice == '4':
                self.delete_format()
                continue
                
            if choice == '5':
                self.read_specific_format() 
                continue
                
            if choice == '6':
                self.update_specific_format()  
                continue
                     
            elif choice == '7':
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")

    def add_format(self):
        while True:
            name = input("\nNome do formato: ")
            if not name.strip():
                print("O nome do formato não pode ser vazio.")
            break

        self.format_crud.create_format(name)
    
    def list_formats(self):
        formats = self.format_crud.read_formats()
        for format in formats:
            print(format)
    def read_specific_format(self):
        format_id = input("Digite o ID do Formato que deseja visualizar: ")
        self.format_crud.read_format_by_id(format_id)
    
    def update_format(self):
        format_id = input("ID do Formato a ser atualizado: ")
        if not format_id.strip():
            print("O ID do Formato não pode ser vazio.")
            return

        # Verifica se o Formato existe
        if not self.format_crud.format_exists(format_id):
            print("Formato não encontrado.")
            return

        name = input("Novo nome do Formato: ")
        while not name.strip():
            print("O nome do Formato não pode ser vazio.")
            name = input("Novo nome do Formato: ")

        self.format_crud.update_format(format_id, name)

        
    def update_specific_format(self):
        format_id = input("Digite o ID do Formato que deseja atualizar: ")

        # Verifica se o Formato existe
        if not self.format_crud.format_exists(format_id):
            print("Formato não encontrado.")
            return

        field = input("Digite o campo que deseja atualizar (name): ")
        valid_fields = ['name']

        # Verifica se o campo é válido
        if field not in valid_fields:
            print("Campo inválido.")
            return

        new_value = input(f"Digite o novo valor para o campo {field}: ")
        while not new_value.strip():
            print(f"O valor para {field} não pode ser vazio.")
            new_value = input(f"Digite o novo valor para o campo {field}: ")
        self.format_crud.update_specific_format_data(format_id, field, new_value)
        
    def delete_format(self):
        format_id = input("ID do Formato a ser removido: ")
        
        # Verifica se o Formato existe
        if not self.format_crud.format_exists(format_id):
            print("Formato não encontrado.")
            return
        
        self.format_crud.delete_format(format_id)


    
    
    