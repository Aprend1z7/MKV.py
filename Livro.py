Python 3.13.6 (tags/v3.13.6:4e66535, Aug  6 2025, 14:36:00) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

# Definição da classe Livro, utilizando a convenção PascalCase para o nome da classe.
class Livro:
    """
    Representa um livro com título, autor, número de páginas e progresso de leitura.
    """

    # O método __init__ é o construtor da classe. Ele é chamado automaticamente
    # quando um novo objeto (instância) da classe é criado.
    # 'self' é uma referência ao próprio objeto que está sendo criado.
    def __init__(self, titulo, autor, numero_paginas):
        """
        Inicializa um novo objeto Livro com os atributos fornecidos.
        """
        # Atributos de instância: são específicos para cada objeto 'Livro'.
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.pagina_atual = 0  # O livro começa fechado, na página 0.

    # Método de instância para abrir o livro.
    def abrir_livro(self):
        """
        Define a página atual como 1, indicando que o livro foi aberto.
        """
        # Verifica se o livro já está aberto para não reiniciar o progresso.
        if self.pagina_atual == 0:
            self.pagina_atual = 1
            print(f"O livro '{self.titulo}' foi aberto na página 1.")
        else:
            print(f"O livro '{self.titulo}' já está aberto na página {self.pagina_atual}.")

    # Método de instância para avançar a leitura.
    def ler_paginas(self, quantidade):
        """
        Avança a leitura em uma 'quantidade' de páginas.
        Verifica se o número de páginas lidas não ultrapassa o total do livro.
        """
        # Verifica se o livro está aberto para a leitura.
        if self.pagina_atual == 0:
            print("Você precisa abrir o livro antes de começar a ler!")
            return  # Encerra o método se o livro estiver fechado.

...         # Calcula a nova página atual
...         nova_pagina = self.pagina_atual + quantidade
... 
...         # Verifica se a nova página não ultrapassa o número total de páginas.
...         if nova_pagina <= self.numero_paginas:
...             self.pagina_atual = nova_pagina
...             print(f"Você leu {quantidade} páginas. Agora está na página {self.pagina_atual}.")
...         else:
...             # Se ultrapassar, a leitura termina na última página.
...             paginas_lidas_realmente = self.numero_paginas - self.pagina_atual + 1
...             self.pagina_atual = self.numero_paginas
...             print(f"Você tentou ler {quantidade} páginas, mas o livro terminou!")
...             print(f"Leitura finalizada na última página: {self.numero_paginas}.")
... 
...     # Método de instância para mostrar o progresso da leitura.
...     def exibir_progresso(self):
...         """
...         Mostra a página atual e quantas páginas faltam para terminar o livro.
...         """
...         if self.pagina_atual == 0:
...             print(f"O livro '{self.titulo}' está fechado.")
...         else:
...             paginas_restantes = self.numero_paginas - self.pagina_atual
...             print(f"--- Progresso de Leitura de '{self.titulo}' ---")
...             print(f"Você está na página: {self.pagina_atual}")
...             print(f"Páginas restantes: {paginas_restantes}")
...             print("---------------------------------------------")
... 
... # --- Exemplo de Uso da Classe Livro ---
... # 1. Criando um objeto (instância) da classe Livro.
... meu_livro = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1200)
... 
... # 2. Testando os métodos.
... meu_livro.exibir_progresso()  # Mostra que o livro está fechado.
... meu_livro.ler_paginas(10)      # Avisa que precisa abrir o livro primeiro.
... 
... meu_livro.abrir_livro()        # Abre o livro na página 1.
... meu_livro.ler_paginas(50)      # Lê 50 páginas.
... meu_livro.exibir_progresso()  # Mostra o progresso atual.
... 
... meu_livro.ler_paginas(1150)    # Tenta ler mais páginas do que o livro tem.
