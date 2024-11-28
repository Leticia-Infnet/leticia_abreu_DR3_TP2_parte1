# Interagindo com LLMs através de API
Parte 1 do Teste de Performance 2 da disciplina Desenvolvimento de Data-Driven Apps com Python
## Clonando o respositório
```
git clone https://github.com/Leticia-Infnet/leticia_abreu_DR3_TP2_parte1.git
```
## Instalando dependências
```
pip install -r requirements.txt
```
⚠️ATENÇÃO⚠️

A biblioteca torch não está listada no requirements.txt. Isso porque as bibliotecas do Pytorch tem suportes específicos para o tipo de OS e arquitetura (CUDA ou CPU) do seu computador. Acesse este [link](https://pytorch.org/) para instalar a versão certa para sua máquina
## Ativando o server uvicorn
1. Da raíz do projeto, vá para o diretório src:
```
cd src
```
2. Estando no diretório src, digite na linha de comando:
```
uvicorn --host 0.0.0.0 --port 8000 --reload main:app
```
## Requisições para o server
Se você seguiu todos os passos, o servirdor estará rodando em http://localhost:8000. Faça requisições através da sua ferramenta preferida (Postman, HTTPie, curl, lib request). Para saber detalhes sobre a API, confira a [documentação](docs).
