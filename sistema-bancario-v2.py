# Exibe o MENU de escolha
def menu():
    menu = """Escolha uma das operações que deseja realizar:
    [1] Depositar
    [2] Sacar
    [3] Exibir extrato
    [4] Cadastrar usuário
    [5] Criar conta corrente
    [6] Listar contas
    [0] Sair\n"""
    return int(input(menu))

# Função de saque com toda a lógica da operação
def sacar(*, saldo, limite_valor_saque, extrato, saque_diario, sacar_valor):  
    if saque_diario > 0:
        if sacar_valor <= saldo:
            if sacar_valor <= limite_valor_saque:
                extrato += f"Sacou R${sacar_valor}\n"
                saldo -= sacar_valor
                saque_diario -= 1                
            else:
                print("O Sr(a) não pode exceder o limite de saque de R$500!")
        else:
            print("O Sr(a) não tem saldo suficiente para o saque!")
    else:
        print("O Sr(a) atingiu o limite de saques diários!")
    return saldo, extrato, saque_diario

# Função de depositar com toda a lógica da operação
def depositar(saldo, extrato, depositar_valor, /):
    if depositar_valor > 0:
        extrato += f"Depositou R${depositar_valor}\n"
        saldo += depositar_valor
    else:
        print("Digite um valor válido!")
    return saldo, extrato

# Função de extrato, para exibir todas transações feitas
def exibir_extrato(saldo, /, *, extrato=""):
    print(f"EXTRATO\n{extrato}\nSaldo final de R${saldo}")

# Lista que armazena todos usuários cadastrados
usuario_lista = []

# Lista que armazena todas contas-corrente cadastradas
contas = []

# Dicionário padrão para cadastro de usuário
usuario_dados = {
    "nome": "", 
    "data_nasc": "", 
    "cpf": "", 
    "endereco": {
        "logradouro": "", 
        "numero": 0, 
        "bairro": "", 
        "cidade_estado": "", 
        "conta_corrente": ""
    }
}

# Função que verifica se o CPF digitado está cadastrado ou não
def filtrar_usuario(cpf, usuarios_dados):
    usuarios_filtrados = [usuario for usuario in usuarios_dados if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para cadastrar/criar um novo usuário
def criar_usuario():
    novo_usuario = {
        "nome": "", 
        "data_nasc": "", 
        "cpf": "", 
        "endereco": {
            "logradouro": "", 
            "numero": 0, 
            "bairro": "", 
            "cidade_estado": "", 
            "conta_corrente": ""
        }
    }

    novo_usuario["nome"] = input("Digite seu nome: ")
    novo_usuario["data_nasc"] = input("Data de nascimento (dd-mm-aaaa): ")
    while True:
        novo_usuario["cpf"] = input("Digite seu CPF: ")
        if len(novo_usuario["cpf"]) != 11:
            print("Digite um CPF válido!")
        elif filtrar_usuario(novo_usuario["cpf"], usuario_lista) is not None:
            print("Este CPF já está cadastrado! Digite outro.")
        else:
            break
    novo_usuario["endereco"]["logradouro"] = input("Logradouro: ")
    novo_usuario["endereco"]["numero"] = input("Número: ")
    novo_usuario["endereco"]["bairro"] = input("Bairro: ")
    novo_usuario["endereco"]["cidade_estado"] = input("Cidade-Estado: ")

    usuario_lista.append(novo_usuario)

    print("Usuário adicionado com sucesso!\n")

# Função para cadastrar/criar um nova conta-corrente
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não está cadastrado no sistema!")

# Função que lista todas contas-corrente criadas
def lista_contas():
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, CPF do Usuário: {conta['usuario']['cpf']}")
        print(f"Nome: {conta['usuario']['nome']}, Data de Nascimento: {conta['usuario']['data_nasc']}")
        print("Endereço:")
        endereco = conta['usuario']['endereco']
        print(f"  Logradouro: {endereco['logradouro']}, Número: {endereco['numero']}")
        print(f"  Bairro: {endereco['bairro']}, Cidade-Estado: {endereco['cidade_estado']}\n")

        
# Função principal, que executa toda a operação
def main():
    SAQUE_DIARIO = 3
    LIMITE_VALOR_SAQUE = 500
    AGENCIA = "0001"
    saldo = 0
    extrato = ""

    print("Bem-vindo(a) ao banco DioBank!")

    while True:
        opcao = menu()
        
        if opcao == 1:
            depositar_valor = int(input("Digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, extrato, depositar_valor)

        elif opcao == 2:  
            sacar_valor = int(input("Digite o valor que deseja sacar: "))
            saldo, extrato, SAQUE_DIARIO = sacar(
                saldo=saldo, 
                limite_valor_saque=LIMITE_VALOR_SAQUE, 
                extrato=extrato, 
                saque_diario=SAQUE_DIARIO, 
                sacar_valor=sacar_valor
            )
                
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario()

        elif opcao == 5:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuario_lista)
            if conta:
                contas.append(conta)

        elif opcao == 6:
            lista_contas()

        elif opcao == 0:
            break

        else:
            print("Digite um valor válido!")
            
# Executa a função principal
main()
