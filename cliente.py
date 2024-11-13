# Define a classe cliente e informações do hóspede
# Dados de cliente como privados

import mysql.connector

import mysql.connector

class Cliente:
    def __init__(self, id, nome, telefone, email, cpf):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.cpf = cpf

    @staticmethod
    def conectar():
        return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="676869",
            database="sistema_hotel"
        )

    @staticmethod
    def cadastrar_cliente(nome, telefone, email, cpf):
        conexao = Cliente.conectar()
        cursor = conexao.cursor()
        comando = "INSERT INTO clientes (nome, telefone, email, cpf) VALUES (%s, %s, %s, %s)"
        valores = (nome, telefone, email, cpf)
        cursor.execute(comando, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def obter_cliente_por_cpf(cpf):
        conexao = Cliente.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email, cpf FROM clientes WHERE cpf = %s", (cpf,))
        cliente = cursor.fetchone()
        cursor.close()
        conexao.close()
        if cliente:
            # Garante que apenas os 5 parâmetros necessários estão sendo passados
            return Cliente(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4])
        return None

    @staticmethod
    def listar_clientes():
        conexao = Cliente.conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, telefone, email, cpf FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return [Cliente(*cliente) for cliente in clientes]