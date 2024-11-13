# define a classe reserva e suas funcionalidades

import mysql.connector
from datetime import datetime

class Reserva:
    def __init__(self, cliente_id, quarto_id, data_entrada, data_saida, total_dias, valor_total):
        self.cliente_id = cliente_id
        self.quarto_id = quarto_id
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.total_dias = total_dias
        self.valor_total = valor_total

    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="676869",
            database="sistema_hotel"
        )

    @staticmethod
    def fazer_reserva(cliente_id, quarto, data_entrada, data_saida):
        total_dias = (data_saida - data_entrada).days
        valor_total = total_dias * quarto.preco_por_dia
        conexao = Reserva.conectar()
        cursor = conexao.cursor()
        comando = """
        INSERT INTO reservas (cliente_id, quarto_id, data_entrada, data_saida, total_dias, valor_total)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(comando, (cliente_id, quarto.id, data_entrada, data_saida, total_dias, valor_total))
        conexao.commit()
        cursor.close()
        conexao.close()
        quarto.marcar_como_ocupado()
