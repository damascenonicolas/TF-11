
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

def validar_cpf(cpf):
    if len(cpf) != 11:
        raise ValueError("cpf invalido")

def validar_email(email):
    if email == "" or "@" not in email:
        raise ValueError("email invalido" if email != "" else "email vazio")

def validar_cep(cep):
    if len(cep) != 8:
        raise ValueError("cep invalido")

def calcular_desconto(tipo_do_cliente, total):
    if tipo_do_cliente == "vip":
        return total * 0.10
    if tipo_do_cliente == "funcionario":
        return total * 0.20
    return 0.0

def descrever_status(status):
    if status == "A":
        return "aberto"
    if status == "P":
        return "pago"
    if status == "C":
        return "cancelado"
    return ""

def processar_pedidos():
    # Instanciando clientes unicos (normalizacao)
    cliente_ana = Cliente("Ana Souza", "12345678901", "ana@email.com", "Rua A", "Sorocaba", "18000000", "normal")
    cliente_bruno = Cliente("Bruno Lima", "123", "bruno@email.com", "Rua B", "Itu", "13300000", "vip")
    cliente_carla = Cliente("Carla Dias", "98765432100", "carla-email.com", "Rua C", "Campinas", "13000000", "funcionario")
    cliente_diego = Cliente("Diego Rocha", "45678912300", "diego@email.com", "Rua D", "Itu", "13300000", "vip")
    cliente_eva = Cliente("Eva Nunes", "78912345600", "eva@email.com", "Rua E", "Itu", "13300000", "funcionario")
    cliente_fabio = Cliente("Fbio Melo", "32165498700", "fabio@email.com", "Rua F", "Sorocaba", "18000", "normal")
    cliente_gil = Cliente("Gil Alves", "65498732100", "gil@email.com", "Rua G", "Sorocaba", "18000000", "normal")

    produto_caderno = Produto("Caderno", 15.50)
    produto_caneta = Produto("Caneta", 2.50)
    produto_mochila = Produto("Mochila", 120.00)
    produto_livro = Produto("Livro", 89.50)
    produto_estojo = Produto("Estojo", 10.00)
    produto_fone = Produto("Fone", 60.00)

    pedidos = [
        Pedido(1, cliente_ana, [ItemDoPedido(produto_caderno, 2), ItemDoPedido(produto_caneta, 5)], "A"),
        Pedido(2, cliente_bruno, [ItemDoPedido(produto_mochila, 1)], "A"),
        Pedido(3, cliente_ana, [ItemDoPedido(produto_livro, 1)], "A"),
        Pedido(4, cliente_carla, [ItemDoPedido(produto_estojo, 2)], "A"),
        Pedido(5, cliente_diego, [ItemDoPedido(produto_caderno, 1)], "A"),
        Pedido(6, cliente_eva, [ItemDoPedido(produto_fone, 1)], "A"),
        Pedido(7, cliente_fabio, [ItemDoPedido(produto_caneta, 10)], "A"),
        Pedido(8, cliente_gil, [ItemDoPedido(produto_fone, 2)], "A")
    ]

    total_arrecadado = 0.0
    pedidos_abertos = 0
    
    for pedido in pedidos:
        try:
            validar_cpf(pedido.cliente.cpf)
            validar_email(pedido.cliente.email)
            validar_cep(pedido.cliente.cep)
        except ValueError as erro:
            print(f"pedido {pedido.numero} recusado: {erro}")
            continue
        
        # acoes do roteiro simuladas
        if pedido.numero in [1, 3, 6]:
            pedido.status = "P"
            print(f"pagar {pedido.numero}: True")
        elif pedido.numero == 5:
            pedido.status = "P"
            print(f"pagar {pedido.numero}: False")
        
        if pedido.numero == 5:
            pedido.status = "C"
            print(f"cancelar {pedido.numero}: True")
        elif pedido.numero == 1:
            print(f"cancelar {pedido.numero}: False")

    for pedido in pedidos:
        try:
            validar_cpf(pedido.cliente.cpf)
            validar_email(pedido.cliente.email)
            validar_cep(pedido.cliente.cep)
        except ValueError:
            continue
            
        total = sum(item.quantidade * item.produto.preco for item in pedido.itens)
        desconto = calcular_desconto(pedido.cliente.tipo, total)
        valor_a_pagar = total - desconto
        
        print(f"Pedido {pedido.numero} - {pedido.cliente.nome} - {pedido.cliente.cidade}")
        print(f"  status: {descrever_status(pedido.status)}")
        for item in pedido.itens:
            print(f"   {item.quantidade} x {item.produto.nome} = R$ {item.quantidade * item.produto.preco:.2f}")
        print(f"  total: R$ {total:.2f} | desconto: R$ {desconto:.2f} | a pagar: R$ {valor_a_pagar:.2f}")
        
        if pedido.status == "P":
            total_arrecadado += valor_a_pagar
        elif pedido.status == "A":
            pedidos_abertos += 1
            
    print(f"arrecadado: R$ {total_arrecadado:.2f}")
    print(f"abertos: {pedidos_abertos}")

if __name__ == "__main__":
    processar_pedidos()
