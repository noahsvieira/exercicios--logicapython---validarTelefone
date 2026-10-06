#Parte 1.1
#Criando função e atendendo os critérios do desafio.

def validar_telefone(telefone):
    tem_tamanho_certo = len(telefone) in (10,11)
    so_tem_numeros = telefone.isdigit()
    return tem_tamanho_certo and so_tem_numeros

#Testando se realmente o código funciona
print(validar_telefone("11999999999"))
print(validar_telefone("1199"))
print(validar_telefone("1199ab"))

# Parte 1.2 
# Criação Classe do pedido.
class Pedido:
    def __init__(self, produto, valor):
        self.produto = produto
        self.valor = valor 

    def resumo(self):
        return f"Pedido de {self.produto} - R${self.valor:.2f}"

pedido1 = Pedido("Recarga", 20)
print(pedido1.resumo())

#Parte 1.3
#Set controlando duplicados
id_vistos = set()
lista_de_ids = ["evt_1" , "evt_2" , "evt_1" , "evt_3" ,"evt_1" , "evt_2"]

for id_atual in lista_de_ids:
    if id_atual not in id_vistos:
        print("Novo:" , id_atual)
        id_vistos.add(id_atual)
    else:
        print("Repetindo , ignorando:", id_atual)

