import requests

class TestCursos:
    headers = {'Authorization': 'Token 2ead31fe8db5eca6cb5683e7e21735aa6340af98'}
    cursos = 'http://127.0.0.1:8000/api/v2/cursos/'

    def test_get_cursos(self):
        resposta = requests.get(url=self.cursos, headers=self.headers)

        assert resposta.status_code == 200


    def test_get_curso(self):
        resposta = requests.get(url=f'{self.cursos}13/', headers=self.headers)

        assert resposta.status_code == 200


    def test_post_cursos(self):
        novo_curso = {'titulo': 'cursodeteste', 'url': 'http://www.jjahhghhgdjorg'}
        resposta = requests.post(url=self.cursos, headers=self.headers, data=novo_curso)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']



    def test_put_curso(self):
        put_curso = {'titulo': 'java pa', 'url': 'http://www.hh.bg'}
        resposta = requests.put(url=f'{self.cursos}4/', headers=self.headers, data=put_curso)

        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == put_curso['titulo']


    def post_delete_curso(self):
        resposta = requests.delete(url=f'{self.cursos}9/', headers=self.headers)

        assert len(resposta.text) == 0 and resposta.status_code == 204