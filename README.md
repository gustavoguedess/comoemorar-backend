# ComoEmorar Backend

Backend do SaaS para análise de dados de cidades e bairros, integração com IA (OpenAI) e Firebase.

## Estrutura
- FastAPI para API REST
- Firebase para autenticação e dados
- OpenAI para geração de insights

## Como rodar

1. Instale as dependências:
   ```zsh
   pip install -r requirements.txt
   ```
2. Configure o arquivo `.env` com suas chaves:
   ```env
   OPENAI_API_KEY=xxx
   FIREBASE_CREDENTIALS=xxx.json
   SECRET_KEY=algumasecret
   ```
3. Inicie o servidor:
   ```zsh
   uvicorn app.main:app --reload
   ```

## Endpoints
- `/auth`: Autenticação
- `/openai`: Consultas à IA
- `/user`: Dados do usuário
- `/map`: Dados para mapas
