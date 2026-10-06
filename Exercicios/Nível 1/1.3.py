"""1.3 Crie um set() vazio chamado ids_vistos. 
Escreva um pequeno trecho de código que recebe uma lista de IDs (alguns repetidos) 
e imprime só os que ainda não estavam no set, adicionando cada um depois de imprimir."""



id_vistos = set()
lista_de_ids = ["evt_1" , "evt_2" , "evt_1" , "evt_3" ,"evt_1" , "evt_2"]

for id_atual in lista_de_ids: # percorre cada item da lista, um de cada vez.
    if id_atual not in id_vistos: # verifica se esse id ainda não está no conjunto.
        print("Novo:" , id_atual)
        id_vistos.add(id_atual)  # adiciona o id ao conjunto, para que da próxima vez ele seja reconhecido como "já visto".
    else:
        print("Repetindo , ignorando:", id_atual)