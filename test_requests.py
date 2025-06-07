import requests

#get avaliacoes

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

#status
print(avaliacoes.status_code)

#dados
print(avaliacoes.json())


print(type(avaliacoes.json()))

print(avaliacoes.json()['count'])

#print(avaliacoes.json()['results'][0][{'id', 'avaliacao', 'nome'}])

#print(avaliacoes.json() ['results'][0]['id'],avaliacoes.json() ['results'][0]['avaliacao'],avaliacoes.json() ['results'][0]['nome'])

avaliacao = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/19/')

print(avaliacao.json())

headers = {
    'Authorization': 'Token 2ead31fe8db5eca6cb5683e7e21735aa6340af98'
}
cursos = requests.get(url='http://127.0.0.1:8000/api/v2/cursos/', headers=headers)       

print(cursos.json())