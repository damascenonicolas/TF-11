
pedidos = [
    {"numero": 1, "nome_do_cliente": "Ana Souza", "cpf_do_cliente": "12345678901", "email_do_cliente": "ana@email.com", "rua": "Rua A", "cidade": "Sorocaba", "cep_do_cliente": "18000000", "tipo_do_cliente": "normal", "itens": [["Caderno", 2, 15.50], ["Caneta", 5, 2.50]], "status": "A"},
    {"numero": 2, "nome_do_cliente": "Bruno Lima", "cpf_do_cliente": "123", "email_do_cliente": "bruno@email.com", "rua": "Rua B", "cidade": "Itu", "cep_do_cliente": "13300000", "tipo_do_cliente": "vip", "itens": [["Mochila", 1, 120.00]], "status": "A"},
    {"numero": 3, "nome_do_cliente": "Ana Souza", "cpf_do_cliente": "12345678901", "email_do_cliente": "ana@email.com", "rua": "Rua A", "cidade": "Sorocaba", "cep_do_cliente": "18000000", "tipo_do_cliente": "normal", "itens": [["Livro", 1, 89.50]], "status": "A"},
    {"numero": 4, "nome_do_cliente": "Carla Dias", "cpf_do_cliente": "98765432100", "email_do_cliente": "carla-email.com", "rua": "Rua C", "cidade": "Campinas", "cep_do_cliente": "13000000", "tipo_do_cliente": "funcionario", "itens": [["Estojo", 2, 10.00]], "status": "A"},
    {"numero": 5, "nome_do_cliente": "Diego Rocha", "cpf_do_cliente": "45678912300", "email_do_cliente": "diego@email.com", "rua": "Rua D", "cidade": "Itu", "cep_do_cliente": "13300000", "tipo_do_cliente": "vip", "itens": [["Caderno", 1, 15.50]], "status": "A"},
    {"numero": 6, "nome_do_cliente": "Eva Nunes", "cpf_do_cliente": "78912345600", "email_do_cliente": "eva@email.com", "rua": "Rua E", "cidade": "Itu", "cep_do_cliente": "13300000", "tipo_do_cliente": "funcionario", "itens": [["Fone", 1, 60.00]], "status": "A"},
    {"numero": 7, "nome_do_cliente": "Fbio Melo", "cpf_do_cliente": "32165498700", "email_do_cliente": "fabio@email.com", "rua": "Rua F", "cidade": "Sorocaba", "cep_do_cliente": "18000", "tipo_do_cliente": "normal", "itens": [["Caneta", 10, 2.50]], "status": "A"},
    {"numero": 8, "nome_do_cliente": "Gil Alves", "cpf_do_cliente": "65498732100", "email_do_cliente": "gil@email.com", "rua": "Rua G", "cidade": "Sorocaba", "cep_do_cliente": "18000000", "tipo_do_cliente": "normal", "itens": [["Fone", 2, 60.00]], "status": "A"}
]

def validar_cpf(cpf_do_cliente):
    if len(cpf_do_cliente) != 11:
        raise ValueError("cpf invalido")

def validar_email(email_do_cliente):
    if email_do_cliente == "" or "@" not in email_do_cliente:
        raise ValueError("email invalido" if email_do_cliente != "" else "email vazio")

def validar_cep(cep_do_cliente):
    if len(cep_do_cliente) != 8:
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
    total_arrecadado = 0.0
    pedidos_abertos = 0
    
    for pedido in pedidos:
        try:
            validar_cpf(pedido["cpf_do_cliente"])
            validar_email(pedido["email_do_cliente"])
            validar_cep(pedido["cep_do_cliente"])
        except ValueError as erro:
            print(f"pedido {pedido['numero']} recusado: {erro}")
            continue
        
        if pedido["numero"] in [1, 3, 6]:
            pedido["status"] = "P"
            print(f"pagar {pedido['numero']}: True")
        elif pedido["numero"] == 5:
            pedido["status"] = "P"
            print(f"pagar {pedido['numero']}: False")
        
        if pedido["numero"] == 5:
            pedido["status"] = "C"
            print(f"cancelar {pedido['numero']}: True")
        elif pedido["numero"] == 1:
            print(f"cancelar {pedido['numero']}: False")

    for pedido in pedidos:
        try:
            validar_cpf(pedido["cpf_do_cliente"])
            validar_email(pedido["email_do_cliente"])
            validar_cep(pedido["cep_do_cliente"])
        except ValueError:
            continue
            
        total = sum(item[1] * item[2] for item in pedido["itens"])
        desconto = calcular_desconto(pedido["tipo_do_cliente"], total)
        valor_a_pagar = total - desconto
        
        print(f"Pedido {pedido['numero']} - {pedido['nome_do_cliente']} - {pedido['cidade']}")
        print(f"  status: {descrever_status(pedido['status'])}")
        for item in pedido["itens"]:
            print(f"   {item[1]} x {item[0]} = R$ {item[1] * item[2]:.2f}")
        print(f"  total: R$ {total:.2f} | desconto: R$ {desconto:.2f} | a pagar: R$ {valor_a_pagar:.2f}")
        
        if pedido["status"] == "P":
            total_arrecadado += valor_a_pagar
        elif pedido["status"] == "A":
            pedidos_abertos += 1
            
    print(f"arrecadado: R$ {total_arrecadado:.2f}")
    print(f"abertos: {pedidos_abertos}")

if __name__ == "__main__":
    processar_pedidos()
