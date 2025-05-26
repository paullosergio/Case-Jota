# Projeto Django com DRF e Celery

Este é um projeto Django que utiliza Django Rest Framework (DRF) para APIs RESTful, Celery para tarefas assíncronas, e Redis como broker de mensagens.

## Requisitos

- Python 3.8+
- Docker e Docker Compose
- Redis (será configurado via Docker)

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone https://github.com/paullosergio/Case-Jota.git
cd [NOME_DO_DIRETÓRIO]
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração do Docker

1. Certifique-se de que o Docker e Docker Compose estão instalados em sua máquina.

2. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```bash
POSTGRES_DB=exemplo
POSTGRES_USER=exemplo
POSTGRES_PASSWORD=exemplo
```

3. Inicie os containers:
```bash
docker-compose up -d
```

## Configuração do Banco de Dados

1. Execute as migrações:
```bash
python manage.py migrate
```

2. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

## Executando o Projeto

1. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

2. Em outro terminal, inicie o worker do Celery:
```bash
celery -A core worker -l info
```

3. Para monitorar tarefas Celery (opcional):
```bash
celery -A core flower
```

## Acessando a API

- API principal: http://localhost:8000/
- Documentação Swagger: http://localhost:8000/swagger/
- Interface de administração: http://localhost:8000/admin/

## Estrutura do Projeto

- `core/`: Configurações principais do Django
- `users/`: Aplicação de gerenciamento de usuários
- `news/`: Aplicação de notícias
- `media/`: Arquivos de mídia enviados
- `staticfiles/`: Arquivos estáticos

## Configurações Importantes

- O projeto usa JWT para autenticação
- Redis está configurado como broker para o Celery
- Arquivos de mídia são servidos em `/media/`
- Arquivos estáticos são servidos em `/static/`

## Testes

O projeto utiliza pytest para testes. Os testes estão organizados em dois arquivos principais:

1. `tests/test_news.py`: Testes para a API de notícias
2. `tests/test_users.py`: Testes para a API de usuários

### Executando os Testes

1. Instale as dependências de teste:
```bash
pip install pytest pytest-django pytest-cov
```

2. Execute todos os testes:
```bash
pytest
```

3. Execute testes com cobertura:
```bash
pytest --cov=.
```

4. Execute testes específicos:
```bash
pytest tests/test_news.py  # Testes da API de notícias
pytest tests/test_users.py  # Testes da API de usuários
```

### Estrutura dos Testes

Os testes incluem:

- Testes de registro e autenticação de usuários
- Testes de CRUD para notícias
- Testes de autorização e permissões
- Testes de endpoints da API

Cada teste verifica:
- Status codes corretos
- Respostas esperadas
- Validação de dados
- Comportamento de autenticação

