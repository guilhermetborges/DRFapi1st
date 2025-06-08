import requests

headers = {'Authorization': 'Token 2ead31fe8db5eca6cb5683e7e21735aa6340af98'}

cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resltado  = requests.delete(url=f'{cursos}12/', headers=headers)

print(resltado.status_code)

assert resltado.status_code == 204
