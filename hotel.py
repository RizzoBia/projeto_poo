# Gerencia o hotel e sua lista de quartos e reservas
class Hotel:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.quarto = []  # Lista de quartos
        self.reservas = []  # Lista de reservas

    def armazenar_quarto(self, quarto):
        self.quarto.append(quarto)
        print(f"Quarto {quarto.get_numero()} ({quarto.get_tipo()}) adicionado ao hotel {self.nome}.")

    def listar_quartos_disponiveis(self):
        print(f"Quartos disponíveis ({self.nome}):")
        for quarto in self.quarto:
            if quarto.verificar_disponibilidade():
                print(f"Quarto {quarto.get_numero()}: Disponível")
            else:
                print(f"Quarto {quarto.get_numero()}: Ocupado")

    def obter_quarto_por_numero(self, numero):
        for quarto in self.quarto:
            if quarto.get_numero() == numero:
                return quarto
        return None  # Retorna None se o quarto não for encontrado

    def armazenar_reserva(self, reserva):
        self.reservas.append(reserva)

    def obter_reservas(self):
        return self.reservas
