"""1.1 Crie uma função chamada validar_telefone(telefone) 
que recebe um texto e retorna True se tiver entre 10 e 11 caracteres e todos forem números,
 ou False caso contrário."""


def validar_telefone(telefone):
    tem_tamanho_certo = len(telefone) in (10,11) #conta quantos caracteres tem o texto.
    so_tem_numeros = telefone.isdigit() # método de texto que verifica se todos os caracteres são dígitos
    return tem_tamanho_certo and so_tem_numeros

#Testando se realmente o código funciona
print(validar_telefone("11999999999"))
print(validar_telefone("1199"))
print(validar_telefone("1199ab"))