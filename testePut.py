import requests

headers = {'Authorization': 'Token 2ead31fe8db5eca6cb5683e7e21735aa6340af98'}

cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

put_curso = {'titulo': 'j ', 'url': 'http://www.djak-g'}

resultado = requests.put(url=f'{cursos}12/', headers=headers, data=put_curso)

teste_resultado = requests.get(url=f'{cursos}12/', headers=headers)

print(teste_resultado.json())


assert resultado.status_code == 200

assert resultado.json()['titulo'] == put_curso['titulo']

