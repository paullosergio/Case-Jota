# Projeto Django com DRF e Celery

Este é um projeto Django que utiliza Django Rest Framework (DRF) para APIs RESTful, Celery para tarefas assíncronas, e Redis como broker de mensagens.

## Requisitos

- Python 3.8+
- Docker e Docker Compose
- Redis (será configurado via Docker)

## Configuração do Ambiente

1. Clone o repositório:
```bash
git clone [https://github.com/paullosergio/Case-Jota.git]
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

