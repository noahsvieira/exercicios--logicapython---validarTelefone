"""1.2 Crie uma classe chamada Pedido, com __init__ recebendo produto e valor. 
Adicione um método resumo() que retorna uma frase tipo: 
"Pedido de Recarga - R$ 20.00"."""


class Pedido:
    def __init__(self, produto, valor):
        self.produto = produto # guarda o valor recebido dentro do objeto, para poder usar depois em outros métodos.
        self.valor = valor  

    def resumo(self): # um método — uma função que pertence à classe, e por isso sempre recebe self (o próprio objeto) como primeiro parâmetro.
        return f"Pedido de {self.produto} - R${self.valor:.2f}"

pedido1 = Pedido("Recarga", 20)
print(pedido1.resumo())