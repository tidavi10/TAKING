import requests

def main():
    print('####################')
    print('DATA DE HOJE 29/01')
    print('##EXERCÍCIO BRANCH##')
    print('## TAKING CEP TESTE DAVI ##')
    print('ESTUDANDO PARA EFETUAR MERGE')
    print('ESTUDANDO PARA EFETUAR MERGE')
    print('ESTUDANDO PARA EFETUAR MERGE')
    print('ESTUDANDO PARA EFETUAR MERGE')
    print('####################')
    print()

    cep_input = input('Digite o CEP que você deseja consultar: ')

    if len(cep_input) != 8:
        print('Quantidade de dígitos inválida!')
        exit()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('==> CEP ENCONTRADO <==')

        print('CEP: {}'.format(address_data['cep']))
        print('Logradouro: {}'.format(address_data['logradouro']))
        print('Complemento: {}'.format(address_data['complemento']))
        print('Bairro: {}'.format(address_data['bairro']))
        print('Cidade: {}'.format(address_data['localidade']))
        print('Estado: {}'.format(address_data['uf']))

    else:
        print('{}: CEP inválido.'.format(cep_input))

    print('---------------------------------')
    option = int(input('Deseja realizar uma nova consulta ?\n1. Sim\n2. Sair\n'))
    if option == 1:
        main()
    else:
        print('FINALIZADO_TAKING...')


if __name__ == '__main__':
    main()