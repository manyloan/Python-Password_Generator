import random
import string

qtd_caracteres = int(input('Insira a quantidade de caracteres na senha: '))
qtd_numeros = int(input('Insira a quantidade de numeros na senha: '))

numero_list =  ''.join(random.choice(string.digits) for i in range(qtd_numeros))
caracteres_list = ''.join(random.choice(string.ascii_letters) for i in range(qtd_caracteres))
	
syntax_list = numero_list + caracteres_list + '!@#'
if len(syntax_list) < 6:
    print('Senhas tem que ter no mínimo 6 caracteres.')
    exit()
result = random.sample(syntax_list, len(syntax_list)) 
password = ''.join((result))
print('Sua senha é:  {}'.format(password))
