API de Notícias
Descrição
Esta é uma API RESTful para gerenciar notícias, construída com Flask e SQLite. A API permite criar, visualizar, atualizar e deletar notícias. Cada notícia contém um título, corpo, autor e data de criação.

A API está documentada utilizando Swagger e possui uma coleção Postman para facilitar o teste dos endpoints.

Funcionalidades
A API permite:

Listar todas as notícias
Obter uma notícia específica pelo ID
Criar uma nova notícia
Atualizar uma notícia existente
Deletar uma notícia
Endpoints
GET /news
Lista todas as notícias cadastradas.

Exemplo de Resposta:

json
Copiar código
[
  {
    "id": 1,
    "title": "Título da Notícia",
    "body": "Corpo da notícia",
    "author": "Nome do autor",
    "created_at": "2023-10-05T18:42:00"
  },
  {
    "id": 2,
    "title": "Outra Notícia",
    "body": "Outro corpo de notícia",
    "author": "Outro autor",
    "created_at": "2023-10-06T09:00:00"
  }
]
GET /news/{id}
Obtém uma notícia específica pelo ID.

Exemplo de Resposta:

json
Copiar código
{
  "id": 1,
  "title": "Título da Notícia",
  "body": "Corpo da notícia",
  "author": "Nome do autor",
  "created_at": "2023-10-05T18:42:00"
}
POST /news
Cria uma nova notícia.

Corpo da Requisição (JSON):

json
Copiar código
{
  "title": "Título da Notícia",
  "body": "Corpo da notícia",
  "author": "Nome do autor"
}
Exemplo de Resposta:

json
Copiar código
{
  "message": "Notícia criada com sucesso!"
}
PUT /news/{id}
Atualiza uma notícia existente pelo ID.

Corpo da Requisição (JSON):

json
Copiar código
{
  "title": "Novo Título",
  "body": "Novo Corpo da notícia",
  "author": "Nome do autor"
}
Exemplo de Resposta:

json
Copiar código
{
  "message": "Notícia atualizada com sucesso!"
}
DELETE /news/{id}
Deleta uma notícia específica pelo ID.

Exemplo de Resposta:

json
Copiar código
{
  "message": "Notícia deletada com sucesso!"
}
Como Rodar o Projeto Localmente
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Instale as dependências:
bash
Copiar código
cd news-api
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
Configure o banco de dados e inicie o servidor:
bash
Copiar código
python app.py
O servidor será iniciado em http://localhost:5000.

Documentação da API
A API está documentada utilizando Swagger. Acesse a documentação via o endpoint /swagger.

Testando com Postman
Uma coleção do Postman foi criada para facilitar os testes da API. Para utilizá-la:

Baixe a coleção do Postman.
Importe-a no seu Postman.
Use os exemplos de requisição para testar os endpoints da API.
Deploy no Render.com
Esta API está hospedada publicamente no Render.com. Para acessar a versão ao vivo, visite o link:

URL do Deploy: https://seu-api-no-render.com
