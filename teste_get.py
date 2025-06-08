import requests

headers = {'Authorization': 'Token 2ead31fe8db5eca6cb5683e7e21735aa6340af98'}

cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

avaliacoes = 'http://127.0.0.1:8000/api/v2/avaliacoes/'

resultasoCurso = requests.get(url=cursos, headers=headers)

resultadoAvaliacoes = requests.get(url=avaliacoes, headers=headers)

print(resultasoCurso.json())

#print(resultadoAvaliacoes.json())
###################################


print(resultasoCurso.status_code)

#assert resultasoCurso.status_code == 200

#assert resultasoCurso.json()['count'] == 6

print(resultasoCurso.json()["count"])


