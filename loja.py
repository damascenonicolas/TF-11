
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
        descricoes = {
            "A": "aberto",
            "P": "pago",
            "C": "cancelado"
        }
        return descricoes.get(self.codigo, "")

    def esta_aberto(self):
        return self.codigo == "A"

    def esta_pago(self):
        return self.codigo == "P"

    def tornar_pago(self):
        self.codigo = "P"

    def tornar_cancelado(self):
        self.codigo = "C"

class TipoNormal:
    """Responsavel por calcular o desconto para clientes normais (0%)."""
    def calcular_desconto(self, total):
        return Dinheiro(0)

class TipoVip:
    """Responsavel por calcular o desconto para clientes VIP (10%)."""
    def calcular_desconto(self, total):
        return total.percentual(0.10)

class TipoFuncionario:
    """Responsavel por calcular o desconto para clientes funcionarios (20%)."""
    def calcular_desconto(self, total):
        return total.percentual(0.20)

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

    def obter_cidade(self):
        return self.cidade

class Cliente:
    """Responsavel por agrupar os dados pessoais, o endereco e a estrategia de desconto."""
    def __init__(self, pessoa, endereco, tipo_estrategia):
        self.pessoa = pessoa
        self.endereco = endereco
        self.tipo_estrategia = tipo_estrategia

    def obter_nome_da_pessoa(self):
        return self.pessoa.nome

    def obter_cidade_do_endereco(self):
        return self.endereco.obter_cidade()

    def calcular_desconto(self, total):
        return self.tipo_estrategia.calcular_desconto(total)

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
    """Responsavel por gerenciar o comportamento, o cliente, os itens e o status de um pedido."""
    def __init__(self, cliente, itens, status):
        self.cliente = cliente
        self.itens = itens
        self.__status = status

    def pagar(self):
        if not self.__status.esta_aberto():
            return False
        if self.itens.esta_vazia():
            return False
        self.__status.tornar_pago()
        return True

    def cancelar(self):
        if not self.__status.esta_aberto():
            return False
        self.__status.tornar_cancelado()
        return True

    def imprimir_relatorio(self, numero):
        total = self.itens.calcular_total()
        desconto = self.cliente.calcular_desconto(total)
        valor_a_pagar = total.subtrair(desconto)

        print(f"Pedido {numero} - {self.cliente.obter_nome_da_pessoa()} - {self.cliente.obter_cidade_do_endereco()}")
        print(f"  status: {self.__status.descrever()}")
        self.itens.imprimir_itens()
        print(f"  total: {total} | desconto: {desconto} | a pagar: {valor_a_pagar}")

    def esta_pago(self):
        return self.__status.esta_pago()

    def esta_aberto(self):
        return self.__status.esta_aberto()

class Pedidos:
    """Responsavel por encapsular o dicionario de pedidos e gerenciar operacoes em lote."""
    def __init__(self):
        self.__mapa_de_pedidos = {}

    def adicionar(self, numero, pedido):
        self.__mapa_de_pedidos[numero] = pedido

    def processar_e_imprimir(self):
        acoes = [
            (1, lambda p: print(f"pagar 1: {p.pagar()}")),
            (1, lambda p: print(f"cancelar 1: {p.cancelar()}")),
            (3, lambda p: print(f"pagar 3: {p.pagar()}")),
            (5, lambda p: print(f"pagar 5: {p.pagar()}")),
            (5, lambda p: print(f"cancelar 5: {p.cancelar()}")),
            (6, lambda p: print(f"pagar 6: {p.pagar()}"))
        ]

        for numero, acao in acoes:
            if numero in self.__mapa_de_pedidos:
                acao(self.__mapa_de_pedidos[numero])

        total_arrecadado = Dinheiro(0)
        pedidos_abertos = 0

        for numero, pedido in self.__mapa_de_pedidos.items():
            total = pedido.itens.calcular_total()
            desconto = pedido.cliente.calcular_desconto(total)
            valor_a_pagar = total.subtrair(desconto)

            pedido.imprimir_relatorio(numero)

            if pedido.esta_pago():
                total_arrecadado = total_arrecadado.somar(valor_a_pagar)
            elif pedido.esta_aberto():
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
        (1, lambda: Cliente(Pessoa("Ana Souza", Cpf("12345678901"), Email("ana@email.com")), Endereco("Rua A", "Sorocaba", Cep("18000000")), TipoNormal()), ItensDoPedido([ItemDoPedido(produto_caderno, 2), ItemDoPedido(produto_caneta, 5)]), Status("A")),
        (2, lambda: Cliente(Pessoa("Bruno Lima", Cpf("123"), Email("bruno@email.com")), Endereco("Rua B", "Itu", Cep("13300000")), TipoVip()), ItensDoPedido([ItemDoPedido(produto_mochila, 1)]), Status("A")),
        (3, lambda: Cliente(Pessoa("Ana Souza", Cpf("12345678901"), Email("ana@email.com")), Endereco("Rua A", "Sorocaba", Cep("18000000")), TipoNormal()), ItensDoPedido([ItemDoPedido(produto_livro, 1)]), Status("A")),
        (4, lambda: Cliente(Pessoa("Carla Dias", Cpf("98765432100"), Email("carla-email.com")), Endereco("Rua C", "Campinas", Cep("13000000")), TipoFuncionario()), ItensDoPedido([ItemDoPedido(produto_estojo, 2)]), Status("A")),
        (5, lambda: Cliente(Pessoa("Diego Rocha", Cpf("45678