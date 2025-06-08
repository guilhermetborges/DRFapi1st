import requests

headers = {'Authorization': 'Token 2ead31fe8db5eca6cb5683e7e21735aa6340af98'}

cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

novo_curso = {'titulo': 'jaavaaaaa', 'url': 'http://www.djak.rg'}

resultado = requests.post(url=cursos, headers=headers, data=novo_curso)

print(resultado.json())

assert resultado.status_code == 201


assert resultado.json()['titulo'] == novo_curso['titulo']


