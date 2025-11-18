# 🌦️ Projeto API OpenWeather Meteomatics

O projeto realiza diariamente a coleta de dados climáticos da cidade de Joinville/SC 
usando a API da OpenWeather. Uma task automática executada à meia-noite consulta a API, 
extrai temperatura, umidade e condições climáticas, e persiste as informações no banco MySQL.

## 📌 Explicação das tasks

> A task `consultar_clima_task` é executada automaticamente via Celery 
> Ela chama a função `buscar_dados_climaticos_da_api`, que faz a chamada HTTP usando parâmetros 
> dinâmicos na API OpenWeather.

## 📌 Arquitetura resumida

```
Task → API OpenWeather → Django Service → MySQL → API REST (consultas)
```

---

## 🧪 Exemplos de requisição
Exemplo usando curl:
```bash
curl "http://localhost:8000/api/clima?data=2025-11-17"
```

Exemplo de resposta (simplificado):
```
[
    {
        "data": "2025-11-17",
        "valores": [
            {
                "data_medicao": "2025-11-17T03:00:00",
                "temperatura": 22.7,
                "precipitacao": 0.86,
                "vento": 0.0
            },
            {
                "data_medicao": "2025-11-17T06:00:00",
                "temperatura": 23.3,
                "precipitacao": 3.79,
                "vento": 1.0
            }
        ]
    }
]
```

---

## 🚀 Tecnologias
- Python  
- Django  
- Django REST Framework  
- Docker + Docker Compose  
- Celery, Redis para tarefas assíncronas
- Biblioteca para integração com APIs meteorológicas (Meteomatics / OpenWeather)

---

## 📦 Funcionalidades

- Endpoint para consulta de previsão meteorológica por cidade ou coordenadas  
- Suporte para parâmetros como temperatura, vento, chuva, pressão, etc  
- Respostas em JSON padronizadas  
- Possibilidade de configurar chaves de API (OpenWeather / Meteomatics) via variáveis de ambiente

---

## ⚙️ Requisitos

Para rodar localmente, você vai precisar de:

- Python >= 3.10 (ou versão compatível com seu `requirements.txt`)  
- Docker
- Docker Compose

---

## 🔧 Como rodar

### Usando Docker

1. Clone o repositório  
```bash
   git clone https://github.com/helen-knk/open-weather-meteomatics.git  
   cd open-weather-meteomatics  
```
2. Ajuste o arquivo `.env.example` para `.env` e ajuste as variáveis.

Suba os containers:
```
docker compose up --build 
```
Estudos indicam que o comando abaixo podem salvar vidas em produção.
```
docker compose -f docker-compose.prod.yml up --build
```
Parar a execução dos containers:
```
docker compose down
```

Parar a execução dos containers, e limpar os dados do MySQL:
```
docker compose down -v
```

3. Acesse a API (por exemplo):

- http://localhost:8000/api/clima
- ou http://localhost:8000/swagger


### Sem Docker (venv)
Crie e ative um ambiente virtual:
```bash
python -m venv .venv  
source .venv/bin/activate   # Linux / Mac  
.\.venv\Scripts\activate    # Windows  
```

1. Instale as dependências:
```
 pip install -r requirements.txt  
```

2. Ajuste o arquivo `.env.example` para `.env`, configurando as variáveis.
3. Rode o servidor:
```
python manage.py runserver  
```
