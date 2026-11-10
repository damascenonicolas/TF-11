
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

class Cliente:
    """Responsavel por armazenar os dados cadastrais e de endereco de um cliente."""
    def __init__(self, nome, cpf, email, rua, cidade, cep, tipo):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.rua = rua
        self.cidade = cidade
        self.cep = cep
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

class Pedido:
    """Responsavel por agrupar o numero, o cliente, os itens e o status de um pedido."""
    def __init__(self, numero, cliente, itens, status):
        self.numero = numero
        self.cliente = cliente
        self.itens = itens
        self.status = status

def calcular_desconto(tipo_do_cliente, total):
    if tipo_do_cliente == "vip":
        return total.percentual(0.10)
    if tipo_do_cliente == "funcionario":
        return total.percentual(0.20)
    return Dinheiro(0)

def processar_pedidos():
    try:
        cliente_ana = Cliente("Ana Souza", Cpf("12345678901"), Email("ana@email.com"), "Rua A", "Sorocaba", Cep("18000000"), "normal")
    except ValueError:
        pass

    try:
        cliente_bruno = Cliente("Bruno Lima", Cpf("123"), Email("bruno@email.com"), "Rua B", "Itu", Cep("13300000"), "vip")
    except ValueError:
        cliente_bruno = None # Marcador para falha na criacao

    try:
        cliente_carla = Cliente("Carla Dias", Cpf("98765432100"), Email("carla-email.com"), "Rua C", "Campinas", Cep("13000000"), "funcionario")
    except ValueError:
        cliente_carla = None

    try:
        cliente_diego = Cliente("Diego Rocha", Cpf("45678912300"), Email("diego@email.com"), "Rua D", "Itu", Cep("13300000"), "vip")
    except ValueError:
        cliente_diego = None

    try:
        cliente_eva = Cliente("Eva Nunes", Cpf("78912345600"), Email("eva@email.com"), "Rua E", "Itu", Cep("13300000"), "funcionario")
    except ValueError:
        cliente_eva = None

    try:
        cliente_fabio = Cliente("Fbio Melo", Cpf("32165498700"), Email("fabio@email.com"), "Rua F", "Sorocaba", Cep("18000"), "normal")
    except ValueError:
        cliente_fabio = None

    try:
        cliente_gil = Cliente("Gil Alves", Cpf("65498732100"), Email("gil@email.com"), "Rua G", "Sorocaba", Cep("18000000"), "normal")
    except ValueError:
        cliente_gil = None

    produto_caderno = Produto("Caderno", Dinheiro.de_reais(15.50))
    produto_caneta = Produto("Caneta", Dinheiro.de_reais(2.50))
    produto_mochila = Produto("Mochila", Dinheiro.de_reais(120.00))
    produto_livro = Produto("Livro", Dinheiro.de_reais(89.50))
    produto_estojo = Produto("Estojo", Dinheiro.de_reais(10.00))
    produto_fone = Produto("Fone", Dinheiro.de_reais(60.00))

    brutos = [
        (1, lambda: Cliente("Ana Souza", Cpf("12345678901"), Email("ana@email.com"), "Rua A", "Sorocaba", Cep("18000000"), "normal"), [ItemDoPedido(produto_caderno, 2), ItemDoPedido(produto_caneta, 5)], Status("A")),
        (2, lambda: Cliente("Bruno Lima", Cpf("123"), Email("bruno@email.com"), "Rua B", "Itu", Cep("13300000"), "vip"), [ItemDoPedido(produto_mochila, 1)], Status("A")),
        (3, lambda: Cliente("Ana Souza", Cpf("12345678901"), Email("ana@email.com"), "Rua A", "Sorocaba", Cep("18000000"), "normal"), [ItemDoPedido(produto_livro, 1)], Status("A")),
        (4, lambda: Cliente("Carla Dias", Cpf("98765432100"), Email("carla-email.com"), "Rua C", "Campinas", Cep("13000000"), "funcionario"), [ItemDoPedido(produto_estojo, 2)], Status("A")),
        (5, lambda: Cliente("Diego Rocha", Cpf("45678912300"), Email("diego@email.com"), "Rua D", "Itu", Cep("13300000"), "vip"), [ItemDoPedido(produto_caderno, 1)], Status("A")),
        (6, lambda: Cliente("Eva Nunes", Cpf("78912345600"), Email("eva