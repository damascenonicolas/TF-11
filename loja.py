class Cpf:
    def __init__(self, valor):
        if len(valor) != 11:
            raise ValueError("cpf invalido")
        self.valor = valor

class Email:
    def __init__(self, valor):
        if valor == "":
            raise ValueError("email vazio")
        if "@" not in valor:
            raise ValueError("email invalido")
        self.valor = valor

class Cep:
    def __init__(self, valor):
        if len(valor) != 8:
            raise ValueError("cep invalido")
        self.valor = valor

class Dinheiro:
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
    def __init__(self, codigo):
        self.codigo = codigo

    def descrever(self):
        descricoes = {"A": "aberto", "P": "pago", "C": "cancelado"}
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
    def calcular_desconto(self, total):
        return Dinheiro(0)

class TipoVip:
    def calcular_desconto(self, total):
        return total.percentual(0.10)

class TipoFuncionario:
    def calcular_desconto(self, total):
        return total.percentual(0.20)

class Pessoa:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email

class Endereco:
    def __init__(self, rua, cidade, cep):
        self.rua = rua
        self.cidade = cidade
        self.cep = cep

    def obter_cidade(self):
        return self.cidade

class Cliente:
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
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ItemDoPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco.multiplicar(self.quantidade)

    def imprimir(self):
        print(f"   {self.quantidade} x {self.produto.nome} = {self.calcular_subtotal()}")

class ItensDoPedido:
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
    pcad = Produto("Caderno", Dinheiro.de_reais(15.50))
    pcan = Produto("Caneta", Dinheiro.de_reais(2.50))
    pmoc = Produto("Mochila", Dinheiro.de_reais(120.00))
    pliv = Produto("Livro", Dinheiro.de_reais(89.50))
    pest = Produto("Estojo", Dinheiro.de_reais(10.00))
    pfon = Produto("Fone", Dinheiro.de_reais(60.00))

    brutos = [
        (1, lambda: Cliente(Pessoa("Ana Souza", Cpf("12345678901"), Email("ana@email.com")), Endereco("Rua A", "Sorocaba", Cep("18000000")), TipoNormal()), ItensDoPedido([ItemDoPedido(pcad, 2), ItemDoPedido(pcan, 5)]), Status("A")),
        (2, lambda: Cliente(Pessoa("Bruno Lima", Cpf("123"), Email("bruno@email.com")), Endereco("Rua B", "Itu", Cep("13300000")), TipoVip()), ItensDoPedido([ItemDoPedido(pmoc, 1)]), Status("A")),
        (3, lambda: Cliente(Pessoa("Ana Souza", Cpf("12345678901"), Email("ana@email.com")), Endereco("Rua A", "Sorocaba", Cep("18000000")), TipoNormal()), ItensDoPedido([ItemDoPedido(pliv, 1)]), Status("A")),
        (4, lambda: Cliente(Pessoa("Carla Dias", Cpf("98765432100"), Email("carla-email.com")), Endereco("Rua C", "Campinas", Cep("13000000")), TipoFuncionario()), ItensDoPedido([ItemDoPedido(pest, 2)]), Status("A")),
        (5, lambda: Cliente(Pessoa("Diego Rocha", Cpf("45678912300"), Email("diego@email.com")), Endereco("Rua D", "Itu", Cep("13300000")), TipoVip()), ItensDoPedido([ItemDoPedido(pcad, 1)]), Status("A")),
        (6, lambda: Cliente(Pessoa("Eva Nunes", Cpf("78912345600"), Email("eva@email.com")), Endereco("Rua E", "Itu", Cep("13300000")), TipoFuncionario()), ItensDoPedido([ItemDoPedido(pfon, 1)]), Status("A")),
        (7, lambda: Cliente(Pessoa("Fbio Melo", Cpf("32165498700"), Email("fabio@email.com")), Endereco("Rua F", "Sorocaba", Cep("18000")), TipoNormal()), ItensDoPedido([ItemDoPedido(pcan, 10)]), Status("A")),
        (8, lambda: Cliente(Pessoa("Gil Alves", Cpf("65498732100"), Email("gil@email.com")), Endereco("Rua G", "Sorocaba", Cep("18000000")), TipoNormal()), ItensDoPedido([ItemDoPedido(pfon, 2)]), Status("A"))
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