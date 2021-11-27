# bibliotecas
import pytest
import requests

# Endereço de API
url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # No .asmr seria 'text/xml


# O teste
def testar_criar_usuario():
    # Configura
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = "unknown"
    mensagem_esperada = '4689'

    # Executa
    resposta = requests.post(  # Faz a requisição, passando:
        url=url,  # O endpoint da API
        data=open('C:/Users/User/PycharmProjects/FTS132/test/db/user1.json', 'rb'),  # O body JSON
        headers=headers  # O header com o Content-Type
    )

    # formatação
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # status code
    print(corpo_da_resposta)  # respostas formatada

    # valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada
