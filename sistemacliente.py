# Define a classe Sistema Cliente que irá armazenar os registros dos clientes

from cliente import Cliente

class SistemaCliente:

    def __init__(self):
        self.historico_clientes = Cliente.obter_historico_clientes()

    def exibir_historico_clientes(self):
        historico = Cliente.obter_historico_clientes()
        for cliente in historico:
            cliente.exibir_informacoes()
            print("-" * 30)
