from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from waitress import serve
from app import app

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo da notícia
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Criar o banco de dados
with app.app_context():
    db.create_all()

# Rota para listar todas as notícias
@app.route('/news', methods=['GET'])
def get_news():
    news = News.query.all()
    return jsonify([{
        'id': item.id,
        'title': item.title,
        'body': item.body,
        'author': item.author,
        'created_at': item.created_at
    } for item in news])

# Rota para obter uma notícia específica sobre determinada região 
@app.route('/news/<int:id>', methods=['GET'])
def get_news_by_id(id):
    news_item = News.query.get_or_404(id)
    return jsonify({
        'id': news_item.id,
        'title': news_item.title,
        'body': news_item.body,
        'author': news_item.author,
        'created_at': news_item.created_at
    })

# Rota para criar uma nova notícia sobre o clima
@app.route('/news', methods=['POST'])
def create_news():
    data = request.get_json()
    new_news = News(
        title=data['title'],
        body=data['body'],
        author=data['author']
    )
    db.session.add(new_news)
    db.session.commit()
    return jsonify({'message': 'Notícia criada com sucesso!'}), 201

# Rota para atualizar uma notícia existente sobre o clima
@app.route('/news/<int:id>', methods=['PUT'])
def update_news(id):
    data = request.get_json()
    news_item = News.query.get_or_404(id)

    news_item.title = data['title']
    news_item.body = data['body']
    news_item.author = data['author']

    db.session.commit()
    return jsonify({'message': 'Notícia atualizada com sucesso!'})

# Rota para deletar uma noticia sobre o clima
@app.route('/news/<int:id>', methods=['DELETE'])
def delete_news(id):
    news_item = News.query.get_or_404(id)
    db.session.delete(news_item)
    db.session.commit()
    return jsonify({'message': 'Notícia deletada com sucesso!'})

# Documentação do Swagger
@app.route('/swagger')
def swagger_ui():
    return '''
    <html>
        <head>
            <title>API de Notícias - Swagger UI</title>
        </head>
        <body>
            <h1>API de Notícias - Documentação</h1>
            <iframe src="/swagger.json" width="100%" height="1000px"></iframe>
        </body>
    </html>
    '''

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)