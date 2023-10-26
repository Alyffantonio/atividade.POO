class Conta_bancaria:
    def __init__(self, Num, Saldo, Nome, Tipo, Limite, Status=False):
        self.numero = Num
        self.saldo = Saldo
        self.nome = Nome
        self.tipo = Tipo
        self.limite =Limite
        self.status = Status


    def depositar(self, deposito):
        if deposito > 0:
            self.saldo+=deposito
            print(f"Valor do deposito:{deposito}")
        else:
            deposito < 0
            print(f"{deposito}R$ esté valor de deposito é invalido!!!")

    def Sacar(self, valor_saque):
            if valor_saque <= 0:
                print(f"{valor_saque}R$ este valor de saque é invalido invalido!")
            elif valor_saque > self.saldo:
                print("Saldo insuficiente!")
            elif valor_saque > self.limite:
                print(f"O valor do saque de:{valor_saque} é maior que seu limite de:{self.limite}")
            else:
                self.saldo -= valor_saque
                print(f"Valor de saque:{valor_saque}R$")


    def ativar(self):
        if self.status == False:
            self.status = True
            print("Conta ativa!")
        else:
            print("Conta ativa!")

    def verificarsaldo(self):
        print(f"saldo atual:{self.saldo}")