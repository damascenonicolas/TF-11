# Trabalho Prático - Object Calisthenics (TF-11)

### 1. Normalização
A normalização consiste em armazenar cada dado em um único lugar, fazendo com que as demais entidades apenas apontem para ele por referência. Na loja, resolveu o problema de duplicação dos dados da cliente Ana, garantindo que alterações cadastrais ocorram em um único objeto compartilhado por seus múltiplos pedidos.

### 2. Obsessão por tipos primitivos
O CPF virou uma classe para encapsular regras de validação diretamente no construtor, impedindo que dados inválidos circulem pelo sistema. O uso de centavos inteiros no Dinheiro evitou imprecisões matemáticas comuns em números de ponto flutuante.

### 3. Diga, não pergunte
A lógica de pagamento e cancelamento foi transferida de condicionais externas para métodos internos da classe Pedido. Em vez de consultar o status externamente para tomar decisões, o código agora delega o comportamento diretamente ao objeto responsável.

### 4. Fail first
O "hadouken" (ifs aninhados) foi eliminado utilizando retornos antecipados para tratar casos de erro e exceções no início dos métodos. O uso de `else` foi substituído por validações precoces e por polimorfismo nas estratégias de desconto.

### 5. Modularização
- Cpf: Valida e encapsula o número do CPF.
- Email: Valida e encapsula o formato do e-mail.
- Cep: Valida e encapsula o formato do CEP.
- Dinheiro: Gerencia valores monetários em centavos inteiros.
- Status: Controla o estado e as transições do pedido.
- TipoNormal / TipoVip / TipoFuncionario: Aplicam regras de desconto por polimorfismo.
- Pessoa: Armazena dados de identificação pessoal.
- Endereco: Armazena dados de localização.
- Cliente: Agrupa pessoa, endereço e tipo de cliente.
- Produto: Representa um produto com nome e preço.
- ItemDoPedido: Associa um produto a uma quantidade.
- ItensDoPedido: Gerencia a coleção interna de itens.
- Pedido: Gerencia o estado, o cliente e os itens de uma compra.
- Pedidos: Gerencia o dicionário global e execuções em lote.

### 6. Dívida técnica
A maior dificuldade foi estruturar o roteiro de testes e simulações do dicionário mantendo rigorosamente a mesma ordem cronológica de saída da base feia. Nenhuma outra restrição estrutural ficou pendente.