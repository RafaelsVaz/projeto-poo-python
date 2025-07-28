class Empresa:

    def __init__(self, razaoSocial, codigoDaEmpresa):
        self.razaoSocial = razaoSocial
        self.codigoDaEmpresa = codigoDaEmpresa

    def getRazaoSocial(self):
        return self.razaoSocial

    def setRazaoSocial(self, razaoSocial):
        self.razaoSocial = razaoSocial

    def getCodigoDaEmpresa(self):
        return self.codigoDaEmpresa

    def setCodigoDaEmpresa(self, codigoDaEmpresa):
        self.codigoDaEmpresa = codigoDaEmpresa


class Pagamento:

    def calcular_pagamento(self):
        pass


class Horista(Pagamento):

    def __init__(self, salario_por_hora, horas_trabalhadas):
        self.salario_por_hora = salario_por_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_pagamento(self):
        return self.salario_por_hora * self.horas_trabalhadas * 4.5  # polimorfismo


class Assalariado(Pagamento):

    def __init__(self, salario_base):
        self.salario_base = salario_base

    def calcular_pagamento(self):
        return self.salario_base  #polimorfismo


class Funcionario:

    def __init__(self, nome, CPF, pagamento):
        self.nome = nome
        self.CPF = CPF
        self.pagamento = pagamento  # associação com a classe Pagamento

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getCPF(self):
        return self.CPF

    def setCPF(self, CPF):
        self.CPF = CPF

    def getPagamento(self):
        return self.pagamento

    def setPagamento(self, pagamento):
        if isinstance(pagamento, Pagamento):
            self.pagamento = pagamento
        else:
            raise ValueError(
                "pagamento deve ser uma instância de Horista ou Assalariado.")

    def calcularPagamento(self):
        return self.pagamento.calcular_pagamento()


class Vendedor(Funcionario):  # Vendedor é filho de Funcionario (herança)

    def __init__(self, nome, CPF, pagamento, quantVendas, comissao):
        super().__init__(nome, CPF, pagamento)
        self.quantVendas = quantVendas
        self.comissao = comissao

    def getQuantVendas(self):
        return self.quantVendas

    def setQuantVendas(self, quantVendas):
        self.quantVendas = quantVendas

    def getComissao(self):
        return self.comissao

    def setComissao(self, comissao):
        self.comissao = comissao

    def calcularPagamento(self):
        base = super().calcularPagamento()
        comissao_total = self.quantVendas * self.comissao
        return base + comissao_total


class Gerente(Funcionario):  # Gerente é filho de Funcionario (herança)

    def __init__(self, nome, CPF, pagamento, senha, numFuncionarios):
        super().__init__(nome, CPF, pagamento)
        self.senha = senha
        self.numFuncionarios = numFuncionarios

    def getSenha(self):
        return self.senha

    def setSenha(self, senha):
        self.senha = senha

    def getNumFuncionarios(self):
        return self.numFuncionarios

    def setNumFuncionarios(self, numFuncionarios):
        self.numFuncionarios = numFuncionarios

    def calcularPagamento(self):
        base = super().calcularPagamento()
        bonus = self.numFuncionarios * 100
        return base + bonus


class Loja:

    def __init__(self, nome, endereco, empresa):
        self.nome = nome
        self.endereco = endereco
        self.empresa = empresa  # associação
        self.funcionarios = []

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEmpresa(self):
        return self.empresa

    def setEmpresa(self, empresa):
        self.empresa = empresa

    def adicionarFuncionario(self, funcionario):
        if isinstance(funcionario, Funcionario):
            self.funcionarios.append(funcionario)
        else:
            raise ValueError(
                "funcionario deve ser uma instância de Funcionario ou suas subclasses."
            )

    def listarFuncionarios(self):
        for funcionario in self.funcionarios:
            print(f"""Nome: {funcionario.getNome()} 
CPF: {funcionario.getCPF()} 
Pagamento: R${funcionario.calcularPagamento():.2f} """)
            print("--" * 20)


def criarFuncionario():
    print("\nCadastro de funcionários:")
    print("=-" * 20)
    nome = input("Digite o nome do funcionário: ")
    CPF = input("Digite o CPF do funcionário: ")
    print("=-" * 20)
    # escolhendo o cargo
    print("O funcionário é:\n1. Gerente\n2. Vendedor")
    cargo = input("Digite o número correspondente: ")
    print("=-" * 20)
    # escolhendo o tipo de pagamento
    print("O funcionário é:\n1. Horista\n2. Assalariado")
    tipoPagamento = input("Digite o número correspondente: ")
    print("=-" * 20)

    if tipoPagamento == "1":  # Horista
        salarioPorHora = float(input("Digite o salário por hora: "))
        horasTrabalhadas = float(
            input("Digite as horas trabalhadas na semana: "))
        pagamento = Horista(salario_por_hora=salarioPorHora,
                            horas_trabalhadas=horasTrabalhadas)
    elif tipoPagamento == "2":  # Assalariado
        salarioBase = float(input("Digite o salário base: "))
        pagamento = Assalariado(salario_base=salarioBase)
    else:
        print("Opção de pagamento inválida!")
        return None

    if cargo == "1":  # Gerente
        senha = input("Digite a senha do gerente: ")
        numFuncionarios = int(
            input("Digite o número de funcionários gerenciados: "))
        funcionario = Gerente(nome, CPF, pagamento, senha, numFuncionarios)
    elif cargo == "2":  # Vendedor
        quantVendas = int(input("Digite a quantidade de vendas: "))
        comissao = float(input("Digite o valor da comissão por venda: "))
        funcionario = Vendedor(nome, CPF, pagamento, quantVendas, comissao)
    else:
        print("Opção de cargo inválida!")
        return None

    print(
        f"\nPagamento de {funcionario.getNome()}: R${funcionario.calcularPagamento():.2f}\n"
    )
    return funcionario


def main():
    print("--" * 20)
    # criar empresa
    razaoSocial = input("Digite a razão social da empresa: ").strip()
    codigoEmpresa = input("Digite o código da empresa: ").strip().upper()
    empresa = Empresa(razaoSocial, codigoEmpresa)

    print("--" * 20)
    # criar loja
    nomeLoja = input("Digite o nome da loja: ").strip()
    endereco = input("Digite o endereço da loja: ").strip()
    print("--" * 20)

    loja = Loja(nomeLoja, endereco, empresa)

    while True:
        funcionario = criarFuncionario()
        if funcionario:
            loja.adicionarFuncionario(funcionario)

        while True:
            continuar = input(
                "Deseja cadastrar outro funcionário? (s/n): ").lower()[0]
            if continuar in 'sn':
                break
        if continuar == 'n':
            break

    print("\nLista de Funcionários da Loja:")
    print("--" * 20)
    loja.listarFuncionarios()


if __name__ == "__main__":
    main()
