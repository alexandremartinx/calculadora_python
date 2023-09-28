import tkinter as tk

class Calculadora:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Calculadora")
        
        # Variáveis para armazenar os números e a operação
        self.num1 = ""
        self.num2 = ""
        self.operacao = ""
        
        # Rótulo para exibir os números e a operação atual
        self.display = tk.Label(janela, text="", padx=10, pady=10, font=("Helvetica", 18))
        self.display.grid(row=0, column=0, columnspan=4)
        
        # Botões numéricos
        numeros = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0', '.'
        ]
        
        row, col = 1, 0
        for numero in numeros:
            tk.Button(janela, text=numero, padx=20, pady=20, font=("Helvetica", 14), command=lambda n=numero: self.adicionar_numero(n)).grid(row=row, column=col)
            col += 1
            if col > 2:
                col = 0
                row += 1
        
        # Botões de operações
        operacoes = ['+', '-', '*', '/']
        row = 1
        col = 3
        for operacao in operacoes:
            tk.Button(janela, text=operacao, padx=20, pady=20, font=("Helvetica", 14), bg="orange", command=lambda o=operacao: self.definir_operacao(o)).grid(row=row, column=col)
            row += 1

        # Botão de igual
        tk.Button(janela, text="=", padx=20, pady=20, font=("Helvetica", 14), bg="green", fg="white", command=self.calcular).grid(row=5, column=2)
        
        # Botão Limpar
        tk.Button(janela, text="C", padx=20, pady=20, font=("Helvetica", 14), bg="red", fg="white", command=self.limpar).grid(row=5, column=3)
    
    def adicionar_numero(self, numero):
        if self.operacao == "":
            self.num1 += numero
            self.atualizar_display(self.num1)
        else:
            self.num2 += numero
            self.atualizar_display(f"{self.num1} {self.operacao} {self.num2}")
    
    def definir_operacao(self, operacao):
        if self.num1 != "":
            if self.num2 != "":
                self.calcular()
            self.operacao = operacao
            self.atualizar_display(f"{self.num1} {self.operacao}")
    
    def calcular(self):
        if self.num1 != "" and self.num2 != "" and self.operacao != "":
            try:
                resultado = eval(f"{self.num1} {self.operacao} {self.num2}")
                self.limpar()
                self.num1 = str(resultado)
                self.atualizar_display(resultado)
            except ZeroDivisionError:
                self.limpar()
                self.atualizar_display("Erro: Divisão por zero")
    
    def limpar(self):
        self.num1 = ""
        self.num2 = ""
        self.operacao = ""
        self.atualizar_display("")
    
    def atualizar_display(self, valor):
        self.display.config(text=valor)

if __name__ == "__main__":
    janela = tk.Tk()
    calculadora = Calculadora(janela)
    janela.mainloop()
