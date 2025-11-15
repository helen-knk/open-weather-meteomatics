# 🌦️ Projeto API OpenWeather (Em construção 🚧)

Este projeto está em desenvolvimento e novas funcionalidades serão adicionadas em breve.

## 🐍 Requisitos
- Python 3.14.0
- Docker 28.5.2
- Docker Compose v2.40.3
- Virtualenv (opcional, mas recomendado)

## 📦 Instalação e Ambiente
1. Criar e ativar o ambiente virtual
```
python -m venv .venv
```

Windows:
```
.\.venv\Scripts\activate
```

Linux/Mac:
```
source .venv/bin/activate
```


## 📥 Instalar Dependências

Após ativar a venv:

```
pip install -r requirements.txt
```

### 🔄 Atualizar o requirements.txt

Sempre que você instalar novos pacotes:
```
pip install nome-do-pacote
```

Atualize o arquivo:
```
pip freeze > requirements.txt
```

Isso garante que o projeto esteja sempre com as dependências corretas para reprodução.

### Executar o projeto via Docker
Subir o serviço:
```
docker compose up --build
```
Parar o serviço:
```
docker compose down -v
```

## 📁 Estrutura do Projeto (por enquanto)

````
projeto/
│
├── core/        # Configurações principais do Django
├── api/         # Lógica da API (em desenvolvimento)
├── requirements.txt
└── README.md
````