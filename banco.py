# Definição da classe ContaBancaria.
class ContaBancaria:
    """
    Representa uma conta bancária com titular, saldo e número,
    e permite operações de depósito, saque e consulta.
    """

    # Método construtor para inicializar os atributos da conta.
    def __init__(self, titular, numero_conta):
        """
        Inicializa uma nova ContaBancaria.
        """
        # Atributos de instância.
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0.0  # O saldo inicial é sempre 0.

    # Método para adicionar um valor ao saldo.
    def depositar(self, valor):
        """
        Adiciona um 'valor' ao saldo da conta. O valor deve ser positivo.
        """
        # Validação para garantir que o valor do depósito seja positivo.
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
            self.consultar_saldo()
        else:
            print("Valor de depósito inválido. Por favor, insira um valor positivo.")

    # Método para remover um valor do saldo.
    def sacar(self, valor):
        """
        Remove um 'valor' do saldo, se houver fundos suficientes.
        """
        # Validação para garantir que o valor do saque seja positivo.
        if valor <= 0:
            print("Valor de saque inválido. Por favor, insira um valor positivo.")
            return

        # Validação para verificar se há saldo suficiente.
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            self.consultar_saldo()
        else:
            print("Saldo insuficiente para realizar o saque.")
            print(f"Valor do saque: R$ {valor:.2f} | Saldo atual: R$ {self.saldo:.2f}")

    # Método para exibir o saldo atual.
    def consultar_saldo(self):
        """
        Exibe o saldo atual formatado.
        """
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    # Método para mostrar um extrato simples da conta.
    def exibir_extrato(self):
        """
        Mostra as informações completas da conta.
        """
        print("\n--- Extrato da Conta ---")
        print(f"Titular: {self.titular}")
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Saldo Disponível: R$ {self.saldo:.2f}")
        print("------------------------\n")

# --- Exemplo de Uso da Classe ContaBancaria ---
# 1. Criando um objeto da classe ContaBancaria.
conta_joao = ContaBancaria("João da Silva", "12345-6")

# 2. Testando os métodos.
conta_joao.exibir_extrato() # Mostra as informações iniciais da conta.

conta_joao.depositar(1500.50) # Realiza um depósito.
conta_joao.sacar(300.00)      # Realiza um saque válido.
conta_joao.sacar(2000.00)     # Tenta realizar um saque com saldo insuficiente.
conta_joao.depositar(-100)    # Tenta realizar um depósito com valor negativo.

conta_joao.exibir_extrato() # Mostra o estado final da conta.
