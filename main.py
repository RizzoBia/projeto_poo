from cliente import Cliente
from quarto import Quarto
from reserva import Reserva
from datetime import datetime

def cadastrar_cliente():
    print("\n----- Cadastrar Cliente -----")
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    Cliente.cadastrar_cliente(nome, telefone, email, cpf)
    print("Cliente cadastrado com sucesso!")

def listar_clientes():
    print("\n----- Lista de Clientes -----")
    clientes = Cliente.listar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente.id}, Nome: {cliente.nome}, Telefone: {cliente.telefone}, Email: {cliente.email}, CPF: {cliente.cpf}")

def listar_quartos_disponiveis():
    quartos = Quarto.listar_quartos_disponiveis()
    for quarto in quartos:
        print(f"ID: {quarto.id}, Número: {quarto.numero}, Tipo: {quarto.tipo}, Preço por dia: R${quarto.preco_por_dia}")

def fazer_reserva():
    cpf = input("Digite o CPF do cliente: ")
    cliente = Cliente.obter_cliente_por_cpf(cpf)
    if not cliente:
        print("Cliente não encontrado. Cadastre o cliente antes de fazer uma reserva.")
        return

    listar_quartos_disponiveis()
    numero_quarto = int(input("Digite o número do quarto: "))
    data_entrada = datetime.strptime(input("Data de entrada (dd/mm/yyyy): "), "%d/%m/%Y")
    data_saida = datetime.strptime(input("Data de saída (dd/mm/yyyy): "), "%d/%m/%Y")
    
    # Buscar o quarto específico pelo número
    quarto = next((q for q in Quarto.listar_quartos_disponiveis() if q.numero == numero_quarto), None)
    if not quarto:
        print("Quarto não disponível.")
        return

    Reserva.fazer_reserva(cliente_id=cliente.id, quarto=quarto, data_entrada=data_entrada, data_saida=data_saida)
    print("Reserva feita com sucesso!")

# Menu principal
while True:
    print("\n1. Cadastrar Cliente\n2. Listar Clientes\n3. Listar Quartos Disponíveis\n4. Fazer Reserva\n0. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        listar_clientes()
    elif opcao == "3":
        listar_quartos_disponiveis()
    elif opcao == "4":
        fazer_reserva()
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")
