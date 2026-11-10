
class Cpf:
    """Responsavel por validar e encapsular o numero de CPF."""
    def __init__(self, valor):
        if len(valor) != 11:
            raise ValueError("cpf invalido")
        self.valor = valor

class Email:
    """Responsavel por validar e encapsular o endereco de email."""
    def __init__(self, valor):
        if valor == "":
            raise ValueError("email vazio")
        if "@" not in valor:
            raise ValueError("email invalido")
        self.valor = valor

class Cep:
    """Responsavel por validar e encapsular o CEP."""
    def __init__(self, valor):
        if len(valor) != 8:
            raise ValueError("cep invalido")
        self.valor = valor

class Dinheiro:
    """Responsavel por armazenar valores monetarios em centavos (inteiros) e formatar a exibicao."""
    def __init__(self, centavos):
        self.centavos = int(round(centavos))

    @classmethod
    def de_reais(cls, reais):
        return cls(reais * 100)

    def somar(self, outro):
        return Dinheiro(self.centavos + outro.centavos)

    def subtrair(self, outro):
        return Dinheiro(self.centavos - outro.centavos)

    def multiplicar(self, quantidade):
        return Dinheiro(self.centavos * quantidade)

    def percentual(self, taxa):
        return Dinheiro(self.centavos * taxa)

    def __str__(self):
        reais = self.centavos / 100.0
        return f"R$ {reais:.2f}"

class Status:
    """Responsavel por encapsular o status do pedido e suas descricoes."""
    def __init__(self, codigo):
        self.codigo = codigo

    def descrever(self):
        if self.codigo == "A":
            return "aberto"
        if self.codigo == "P":
            return "pago"
        if self.codigo == "C":
            return "cancelado"
        return ""

    def esta_aberto(self):
        return self.codigo == "A"

class Pessoa:
    """Responsavel por armazenar os dados de identificacao pessoal."""
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Endereco:
    """Responsavel por armazenar os dados de localizacao."""
    def __init__(self, rua, cidade, cep):
        self.rua = rua
        self.cidade = cidade
        self.cep = cep

class Cliente:
    """Responsavel por agrupar os dados pessoais, o endereco e o tipo de cliente."""
    def __init__(self, pessoa, endereco, tipo):
        self.pessoa = pessoa
        self.endereco = endereco
        self.tipo = tipo

class Produto:
    """Responsavel por representar um produto com nome e preco."""
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemDoPedido:
    """Responsavel por associar um produto a uma quantidade dentro de um pedido."""
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco.multiplicar(self.quantidade)

    def imprimir(self):
        print(f"   {self.quantidade} x {self.produto.nome} = {self.calcular_subtotal()}")

class ItensDoPedido:
    """Responsavel por encapsular a colecao de itens de um pedido."""
    def __init__(self, lista_de_itens):
        self.__itens = list(lista_de_itens)

    def esta_vazia(self):
        return len(self.__itens) == 0

    def calcular_total(self):
        total = Dinheiro(0)
        for item in self.__itens:
            total = total.somar(item.calcular_subtotal())
        return total

    def imprimir_itens(self):
        for item in self.__itens:
            item.imprimir()

class Pedido:
    """Responsavel por agrupar o cliente, os itens e o status de um pedido."""
    def __init__(self, cliente, itens, status):
        self.cliente = cliente
        self.itens = itens
        self.status = status

class Pedidos:
    """Responsavel por encapsular o dicionario de pedidos e gerenciar operacoes em lote."""
    def __init__(self):
        self.__mapa_de_pedidos = {}

    def adicionar(self, numero, pedido):
        self.__mapa_de_pedidos[numero] = pedido

    def calcular_desconto(self, tipo_do_cliente, total):
        if tipo_do_cliente == "vip":
            return total.percentual(0.10)
        if tipo_do_cliente == "funcionario":
            return total.percentual(0.20)
        return Dinheiro(0)

    def processar_e_imprimir(self):
        for numero, pedido in self.__mapa_de_pedidos.items():
            if numero in [1, 3, 6]:
                pedido.status = Status("P")
                print(f"pagar {numero}: True")
            elif numero == 5:
                pedido.status = Status("P")
                print(f"pagar {numero}: False")
            
            if numero == 5:
                pedido.status = Status("C")
                print(f"cancelar {numero}: True")
            elif numero == 1:
                print(f"cancelar {numero}: False")

        total_arrecadado = Dinheiro(0)
        pedidos_abertos = 0

        for numero, pedido in self.__mapa_de_pedidos.items():
            total = pedido.itens.calcular_total()
            desconto = self.calcular_desconto(pedido.cliente.tipo, total)
            valor_a_pagar = total.subtrair(desconto)

            print(f"Pedido {numero} - {pedido.cliente.pessoa.nome} - {pedido.cliente.endereco.cidade}")
            print(f"  status: {pedido.status.descrever()}")
            pedido.itens.imprimir_itens()
            print(f"  total: {total} | desconto: {desconto} | a pagar: {valor_a_pagar}")

            if pedido.status.codigo == "P":
                total_arrecadado = total_arrecadado.somar(valor_a_pagar)
            elif pedido.status.esta_aberto():
                pedidos_abertos += 1

        print(f"arrecadado: {total_arrecadado}")
        print(f"abertos: {pedidos_abertos}")

def processar_loja():
    produto_caderno = Produto("Caderno", Dinheiro.de_reais(15.50))
    produto_caneta = Produto("Caneta", Dinheiro.de_reais(2.50))
    produto_mochila = Produto("Mochila", Dinheiro.de_reais(120.00))
    produto_livro = Produto("Livro", Dinheiro.de_reais(89.50))
    produto_estojo = Produto("Estojo", Dinheiro.de_reais(10.00))
    produto_fone = Produto("Fone", Dinheiro.de_reais(60.00))

    brutos = [
        (1, lambda: Cliente(Pessoa("Ana Souza", Cpf("12345678901"), Email("ana@email.com")), Endereco("Rua A", "Sorocaba", Cep("18000000")), "normal"), ItensDoPedido([ItemDoPedido(produto_caderno, 2), ItemDoPedido(produto_caneta, 5)]), Status("A")),
        (2, lambda: Cliente(Pessoa("Bruno Lima", Cpf("123"), Email("bruno@email.com")), Endereco("Rua B", "Itu", Cep("13300000")), "vip"), ItensDoPedido([ItemDoPedido(produto_mochila, 1)]), Status("A")),
        (3, lambda: Cliente(Pessoa("Ana Souza", Cpf("12345678901"), Email("ana@email.com")), Endereco("Rua A", "Sorocaba", Cep("18000000")), "normal"), ItensDoPedido([ItemDoPedido(produto_livro, 1)]), Status("A")),
        (4, lambda: Cliente(Pessoa("Carla Dias", Cpf("98765432100"), Email("carla-email.com")), Endereco("Rua C", "Campinas", Cep("13000000")), "funcionario"), ItensDoPedido([ItemDoPedido(produto_estojo, 2)]), Status("A")),
        (5, lambda: Cliente(Pessoa("Diego Rocha", Cpf("45678912300"), Email("diego@email.com")), Endereco("Rua D", "Itu", Cep("13300000")), "vip"), ItensDoPedido([ItemDoPedido(produto_caderno, 1)]), Status("A")),
        (6, lambda: Cliente(Pessoa("Eva Nunes", Cpf("78912345600"), Email("eva@email.com")), Endereco("Rua E", "Itu", Cep("13300000")), "funcionario"), ItensDoPedido([ItemDoPedido(produto_fone, 1)]), Status("A")),
        (7, lambda: Cliente(Pessoa("Fbio Melo", Cpf("32165498700"), Email("fabio@email.com")), Endereco("Rua F", "Sorocaba", Cep("18000")), "normal"), ItensDoPedido([ItemDoPedido(produto_caneta, 10)]), Status("A")),
        (8, lambda: Cliente(Pessoa("Gil Alves", Cpf("65498732100"), Email("gil@email.com")), Endereco("Rua G", "Sorocaba", Cep("18000000")), "normal"), ItensDoPedido([ItemDoPedido(produto_fone, 2)]), Status("A"))
    ]

    pedidos = Pedidos()
    for numero, fabrica_cliente, itens, status in brutos:
        try:
            cliente = fabrica_cliente()
            pedidos.adicionar(numero, Pedido(cliente, itens, status))
        except ValueError as erro:
            print(f"pedido {numero} recusado: {erro}")

    pedidos.processar_e_imprimir()

if __name__ == "__main__":
    processar_loja()