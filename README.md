# Currency Data Pipeline

API REST desenvolvida em Python com FastAPI para consulta e rastreamento de cotações históricas do dólar (USD/BRL) em tempo real.

---

## Sobre o projeto

Este projeto expõe endpoints para consulta de cotações do dólar a partir de uma API financeira pública. O foco está na integração com fontes de dados externas, tratamento do payload JSON retornado e estruturação da resposta para consumo imediato.

O projeto está em desenvolvimento ativo — a arquitetura atual serve como base para a evolução para um pipeline de dados completo com persistência, análise histórica e agendamento de coletas.

---

## Tecnologias utilizadas

- **Python 3** — linguagem principal
- **FastAPI** — framework para construção da API REST
- **Requests** — consumo da API externa de cotações
- **AwesomeAPI** — fonte de dados financeiros (USD-BRL)

---

## Endpoints disponíveis

### `GET /Bem-vindo`
Rota de verificação. Retorna uma mensagem de boas-vindas confirmando que a API está no ar.

**Resposta:**
```json
{
  "Início": "Bem-vindo à API de cotação do dólar!"
}
```

---

### `GET /cotacao-dolar?pesquisa={valor}`
Busca nas últimas 30 cotações diárias do dólar se um determinado valor de compra (`bid`) foi registrado. Retorna a data correspondente caso encontrado.

**Parâmetro:**

| Nome      | Tipo   | Descrição                              |
|-----------|--------|----------------------------------------|
| `pesquisa` | float | Valor de cotação a ser buscado (ex: 5.72) |

**Resposta (sucesso):**
```json
{
  "data_encontrada": "2025-06-10 10:30:00",
  "valor_encontrado": "O valor do dólar nessa data foi: 5.72"
}
```

**Resposta (não encontrado):**
```json
{
  "ERRO": "Valor não encontrado na cotação do dólar."
}
```

---

## Como executar

```bash
# Clone o repositório
git clone https://github.com/EnukNogueira/currency-data-pipeline.git
cd currency-data-pipeline

# Instale as dependências
pip install fastapi requests uvicorn

# Execute a API
uvicorn projeto_dolar:app --reload
```

Acesse a documentação interativa gerada automaticamente pelo FastAPI em:
`http://127.0.0.1:8000/docs`

---

## Próximos passos

- [ ] Persistência das cotações coletadas em banco de dados
- [ ] Endpoint para análise histórica e variação percentual
- [ ] Agendamento de coletas automáticas com APScheduler
- [ ] Suporte a múltiplas moedas (EUR, GBP, BTC)
- [ ] Exportação dos dados em CSV para análise

---

## Autor

**Enuk Nogueira** — Desenvolvedor focado em Engenharia de Dados e Automação de Processos

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/enuknogueira/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/EnukNogueira)
