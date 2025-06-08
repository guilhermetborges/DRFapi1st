import requests
import jsonpath

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

#resultados = jsonpath.jsonpath(avaliacoes.json(), '$..avaliacao')

#print(resultados)

primeiro = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

nome = jsonpath.jsonpath(avaliacoes.json(), 'results.1.nome')

nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome') # nomes = jsonpath.jsonpath(avaliacoes.json(), '$..nome')

notas = jsonpath.jsonpath(avaliacoes.json(), '$..avaliacao')

print(notas)
print(nomes)

for i in range(len(nomes)):
    print(f'{nomes[i]}: {notas[i]}')