# Documentação da API

## Visão Geral

Esta API fornece dois serviços principais:

- Autocompletar texto usando um modelo de linguagem GPT-2
- Tradução de texto do inglês para o francês usando um modelo de tradução

## Configuração do Servidor

A API é construída usando FastAPI e pode ser executada em dispositivos com ou sem suporte a GPU.

### Endpoints Disponíveis

1. **Status do Servidor**

   - **URL:** `/status`
   - **Método:** GET
   - **Descrição:** Verifica se o servidor está em execução
   - **Resposta de Sucesso:**
     ```json
     {
       "message": "O server está rodando!"
     }
     ```

2. **Autocompletar**

   - **URL:** `/chat/autocomplete`
   - **Método:** POST
   - **Descrição:** Gera continuação automática para uma frase de entrada

   #### Parâmetros de Entrada

   - `phrase` (string, obrigatório): Texto inicial para autocompletar

   #### Exemplo de Requisição

   ```json
   {
     "phrase": "I like milk!"
   }
   ```

   #### Exemplo de Resposta

   ```json
   {
     "assistant": "I like milk! I like the taste of it. This was my first time buying dairy."
   }
   ```

3. **Tradução**

   - **URL:** `/translate/translator`
   - **Método:** POST
   - **Descrição:** Traduz texto do inglês para o francês

   #### Parâmetros de Entrada

   - `phrase` (string, obrigatório): Texto em inglês para tradução

   #### Exemplo de Requisição

   ```json
   {
     "phrase": "Good morning"
   }
   ```

   #### Exemplo de Resposta

   ```json
   {
     "assistant": "Bonjour"
   }
   ```

## Modelos Utilizados

- **Autocompletar:** `openai-community/gpt2`
- **Tradução:** `Helsinki-NLP/opus-mt-en-fr`

## Considerações Técnicas

- A API detecta automaticamente a disponibilidade de GPU
- Caso não haja GPU disponível, o processamento será realizado na CPU
- Os modelos são carregados usando a biblioteca Transformers do Hugging Face

## Tratamento de Erros

- Se o modelo retornar uma lista, será extraído o texto do primeiro item
- Caso contrário, o resultado será convertido para string

## Requisitos

- Python 3.8+
- FastAPI
- Torch
- Transformers
- Modelos pré-treinados do Hugging Face

## Exemplo de Uso com Curl

### Status do Servidor

```bash
curl http://localhost:8000/status
```

### Autocompletar

```bash
curl -X POST http://localhost:8000/chat/autocomplete \
     -H "Content-Type: application/json" \
     -d '{"phrase": "I like milk!"}'
```

### Tradução

```bash
curl -X POST http://localhost:8000/translate/translator \
     -H "Content-Type: application/json" \
     -d '{"phrase": "Good morning"}'
```
