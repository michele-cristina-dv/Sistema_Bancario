class BancoInterativo:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.saques_hoje = 0
        self.bem_vindo()

    def bem_vindo(self):
        print("  ╔═════════════════════════════════╗")
        print("    BEM VINDO A SUA CONTA DIGITAL ")
        print("  ╚═════════════════════════════════╝")
        self.menu()

    def menu(self):
        while True:
            print("\n MENU PRINCIPAL ".center(15))
            print("\n[1] Depositar")
            print("[2] Sacar")
            print("[3] Ver Extrato")
            print("[4] Sair")
            
            opcao = input("\n Escolha uma opção (1-4): ")
            
            if opcao == "1":
                self.depositar()
            elif opcao == "2":
                self.sacar()
            elif opcao == "3":
                self.extrato()
            elif opcao == "4":
                print("\n Obrigado por usar nosso banco digital! Volte sempre :) ")
                break
            else:
                print("\n Opção inválida! Por favor, escolha de 1 a 4")

    def depositar(self):
        try:
            print("\n DEPÓSITO ".ljust(36, "▂"))
            valor = float(input("Quanto você deseja depositar? R$ "))
            
            if valor > 0:
                self.saldo += valor
                self.depositos.append(valor)
                print(f"\n Sucesso! R$ {valor:.2f} depositados!")
                print(f"   Saldo atual: R$ {self.saldo:.2f}")
            else:
                print("\n Valor inválido! O depósito deve ser positivo.")
        except:
            print("\n Por favor, digite um valor numérico válido!")

    def sacar(self):
        try:
            print("\n SAQUE ".ljust(36, "▂"))
            
            if self.saques_hoje >= 3:
                print("\n Você já realizou 3 saques hoje! Volte amanhã.")
                return
            
            if self.saldo <= 0:
                print("\n Saldo insuficiente. Faça um depósito primeiro!")
                return
                
            valor = float(input(f"Quanto deseja sacar? (LIMITE: R$ 500.00)\n R$ "))
            
            if valor > 500:
                print("\n Limite por saque deve ser Até: R$ 500,00!")
            elif valor <= 0:
                print("\n Valor para efetuar o saque deve ser positivo!")
            elif valor > self.saldo:
                print(f"\n Saldo insuficiente! Seu saldo é de R$ {self.saldo:.2f}")
            else:
                self.saldo -= valor
                self.saques.append(valor)
                self.saques_hoje += 1
                print(f"\n Saque de R$ {valor:.2f} realizado!")
                print(f"   Saques hoje: {self.saques_hoje}/3")
                print(f"   Saldo atual: R$ {self.saldo:.2f}")
        except:
            print("\n Por favor, digite um valor numérico válido!")

    def extrato(self):
        print("\n EXTRATO BANCÁRIO ".ljust(36, "▂"))
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        
        if not self.depositos and not self.saques:
            print(" Nenhuma movimentação registrada")
        else:
            print(" DEPÓSITOS:")
            if not self.depositos:
                print("   Nenhum depósito realizado")
            else:
                for d in self.depositos:
                    print(f"    +R$ {d:.2f}")
            
            print("\n SAQUES:")
            if not self.saques:
                print("   Nenhum saque realizado")
            else:
                for s in self.saques:
                    print(f"    -R$ {s:.2f}")
        
        print("\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print(f" SALDO ATUAL: R$ {self.saldo:.2f}")
        
        if self.saldo > 1000:
            print(" Seu dinheiro está crescendo! Continue assim!")
        elif self.saldo > 0:
            print(" Ótimo progresso! Vamos aumentar esses valores?")

# Inicia o sistema bancário
if __name__ == "__main__":
    BancoInterativo()
