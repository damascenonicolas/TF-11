
ped = [
    {"n": 1, "cnome": "Ana Souza", "ccpf": "12345678901", "cmail": "ana@email.com", "crua": "Rua A", "cid": "Sorocaba", "ccep": "18000000", "ctp": "normal", "items": [["Caderno", 2, 15.50], ["Caneta", 5, 2.50]], "st": "A"},
    {"n": 2, "cnome": "Bruno Lima", "ccpf": "123", "cmail": "bruno@email.com", "crua": "Rua B", "cid": "Itu", "ccep": "13300000", "ctp": "vip", "items": [["Mochila", 1, 120.00]], "st": "A"},
    {"n": 3, "cnome": "Ana Souza", "ccpf": "12345678901", "cmail": "ana@email.com", "crua": "Rua A", "cid": "Sorocaba", "ccep": "18000000", "ctp": "normal", "items": [["Livro", 1, 89.50]], "st": "A"},
    {"n": 4, "cnome": "Carla Dias", "ccpf": "98765432100", "cmail": "carla-email.com", "crua": "Rua C", "cid": "Campinas", "ccep": "13000000", "ctp": "funcionario", "items": [["Estojo", 2, 10.00]], "st": "A"},
    {"n": 5, "cnome": "Diego Rocha", "ccpf": "45678912300", "cmail": "diego@email.com", "crua": "Rua D", "cid": "Itu", "ccep": "13300000", "ctp": "vip", "items": [["Caderno", 1, 15.50]], "st": "A"},
    {"n": 6, "cnome": "Eva Nunes", "ccpf": "78912345600", "cmail": "eva@email.com", "crua": "Rua E", "cid": "Itu", "ccep": "13300000", "ctp": "funcionario", "items": [["Fone", 1, 60.00]], "st": "A"},
    {"n": 7, "cnome": "Fbio Melo", "ccpf": "32165498700", "cmail": "fabio@email.com", "crua": "Rua F", "cid": "Sorocaba", "ccep": "18000", "ctp": "normal", "items": [["Caneta", 10, 2.50]], "st": "A"},
    {"n": 8, "cnome": "Gil Alves", "ccpf": "65498732100", "cmail": "gil@email.com", "crua": "Rua G", "cid": "Sorocaba", "ccep": "18000000", "ctp": "normal", "items": [["Fone", 2, 60.00]], "st": "A"}
]

def validar_cpf(cpf):
    if len(cpf) != 11:
        raise ValueError("cpf invalido")

def validar_email(email):
    if email == "" or "@" not in email:
        raise ValueError("email invalido" if email != "" else "email vazio")

def validar_cep(cep):
    if len(cep) != 8:
        raise ValueError("cep invalido")

def calcular_desconto(tipo, total):
    if tipo == "vip":
        return total * 0.10
    if tipo == "funcionario":
        return total * 0.20
    return 0.0

def descrever_status(st):
    if st == "A":
        return "aberto"
    if st == "P":
        return "pago"
    if st == "C":
        return "cancelado"
    return ""

def processar_pedidos():
    arrecadado = 0.0
    abertos = 0
    
    for p in ped:
        try:
            validar_cpf(p["ccpf"])
            validar_email(p["cmail"])
            validar_cep(p["ccep"])
        except ValueError as e:
            print(f"pedido {p['n']} recusado: {e}")
            continue
        
        if p["n"] in [1, 3, 6]:
            p["st"] = "P"
            print(f"pagar {p['n']}: True")
        elif p["n"] == 5:
            p["st"] = "P"
            print(f"pagar {p['n']}: False") 
        
        if p["n"] == 5:
            p["st"] = "C"
            print(f"cancelar {p['n']}: True")
        elif p["n"] == 1:
            print(f"cancelar {p['n']}: False")

    for p in ped:
        try:
            validar_cpf(p["ccpf"])
            validar_email(p["cmail"])
            validar_cep(p["ccep"])
        except ValueError:
            continue
            
        t = sum(item[1] * item[2] for item in p["items"])
        desc = calcular_desconto(p["ctp"], t)
        a_pagar = t - desc
        
        print(f"Pedido {p['n']} - {p['cnome']} - {p['cid']}")
        print(f"  status: {descrever_status(p['st'])}")
        for item in p["items"]:
            print(f"   {item[1]} x {item[0]} = R$ {item[1] * item[2]:.2f}")
        print(f"  total: R$ {t:.2f} | desconto: R$ {desc:.2f} | a pagar: R$ {a_pagar:.2f}")
        
        if p["st"] == "P":
            arrecadado += a_pagar
        elif p["st"] == "A":
            abertos += 1
            
    print(f"arrecadado: R$ {arrecadado:.2f}")
    print(f"abertos: {abertos}")

if __name__ == "__main__":
    processar_pedidos()