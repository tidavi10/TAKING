print("***************************")
print("*****CONSULTA DO CEP*******")
print("***************************")
print("*********TAKING************")
print()
print("******APRESENTAÇÃO*********")
print("***************************")
print()
cep_input = input('DIGITE O CEP PARA CONSULTA: ')

if len(cep_input) !=8:
    print('QUANTIDADE DIGITOS INVÁLIDA!')
    exit()

request = requests.get('http://viacep.com.br/ws/()/json/'.format(cep_input))

address_data = request_json()

if 'erro' not in address_data:
print('CEP ENCONTRADO SUCESSO')
print('CEP: {}'.format(address_data['cep']))
else
print('{}: CEP INVÁLIDO.'.format(cep_input))
