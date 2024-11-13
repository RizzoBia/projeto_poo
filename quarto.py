# Define a classe quarto e seus tipos


import mysql.connector

class Quarto:
    def __init__(self, id, numero, tipo, capacidade, preco_por_dia, status="disponivel"):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.capacidade = capacidade
        self.preco_por_dia = preco_por_dia
        self.status = status

    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="676869",
            database="sistema_hotel"
        )

    @staticmethod
    def listar_quartos_disponiveis():
        conexao = Quarto.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM quartos WHERE status = 'disponivel'")
        quartos = cursor.fetchall()
        cursor.close()
        conexao.close()
        # Debug: Exibe o status dos quartos retornados
        print("Quartos disponíveis encontrados no banco de dados:")
        for quarto in quartos:
            print(f"ID: {quarto[0]}, Número: {quarto[1]}, Status: {quarto[5]}")
        # Retorna uma lista de objetos Quarto apenas para os quartos disponíveis
        return [Quarto(*quarto) for quarto in quartos]

    def marcar_como_ocupado(self):
        conexao = Quarto.conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE quartos SET status = 'ocupado' WHERE id = %s", (self.id,))
        conexao.commit()
        cursor.close()
        conexao.close()

