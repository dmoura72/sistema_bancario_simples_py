#Desafio 01

'''def calcular_saldo(transacoes): 
    saldo = 0  # Inicializa o saldo
    for transacao in transacoes:
        saldo += transacao  # Soma cada transação ao saldo
    return f"Saldo: R$ {saldo:.2f}"  # Retorna o saldo formatado

# Entrada do usuário
entrada_usuario = input("Digite os valores separados por vírgula: ")

# Remover espaços e converter para lista de floats
entrada_usuario = entrada_usuario.replace(" ", "")
transacoes = [float(valor) for valor in entrada_usuario.split(",")]

# Chamar a função e exibir o saldo
resultado = calcular_saldo(transacoes)
print(resultado) '''

#Desafio 02

def filtrar_transacoes(transacoes, limite): 
    transacoes_filtradas = []

    # Itera sobre cada transação na lista:
    for transacao in transacoes:
        # Verifica se o valor absoluto da transação é maior que o limite:
        if abs(transacao) > limite:
            # Adiciona a transação à lista filtrada:
            transacoes_filtradas.append(transacao)

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


# Recebe a entrada e separa os valores
entrada = input()

# Separa a lista de transações e o limite
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")  
limite = float(limite.strip())  # Converte o limite para float

# Converte os valores das transações para inteiros
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

# Filtra as transações que ultrapassam o limite
resultado = filtrar_transacoes(transacoes, limite)

# Exibe o resultado no formato esperado
print(f"Transações: {resultado}")