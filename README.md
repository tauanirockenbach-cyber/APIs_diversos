# 📡 APIs Diversas - Integrações em Python

Este diretório contém uma coleção de scripts em Python desenvolvidos para realizar o consumo de diferentes APIs públicas. Os projetos realizam requisições HTTP, tratam os dados recebidos em formato JSON e demonstram conceitos fundamentais de integração, manipulação de dados e exibição de informações.

## 🚀 Arquivos no Repositório

### Consumo de APIs de Entretenimento e Jogos
* **`pokemon.py`**: Script responsável por consumir a [PokeAPI](https://pokeapi.co), buscando informações detalhadas sobre os Pokémon (como nome, tipos, habilidades ou estatísticas).
* **`disney.py`**: Script focado no consumo da [Disney API](https://disneyapi.dev), focado em buscar personagens e dados relacionados ao universo Disney.

### Utilidades e Outras Integrações
* **`app.py`**: Script principal ou interface de entrada do projeto que coordena as execuções.
* **`conselhos.py`**: Script que realiza a integração com uma API de conselhos aleatórios (como a Advice Slip API).
* **`country.py`**: Script para buscar informações geopolíticas e dados detalhados sobre países.
* **`openstreetmap.py`**: Script focado em geolocalização e mapas através das ferramentas gratuitas do OpenStreetMap.

## 🛠️ Pré-requisitos

Antes de executar os scripts, certifique-se de ter o Python instalado em sua máquina e as dependências necessárias configuradas.

Em vez de instalar pacotes individualmente, instale todas as dependências do projeto de uma única vez utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## ⚙️ Como Executar

Abra o terminal na pasta raiz deste projeto e execute o script desejado utilizando o interpretador do Python:

**Para rodar o script principal:**
```bash
python app.py
```

**Para rodar o script do Pokémon:**
```bash
python pokemon.py
```

**Para rodar o script da Disney:**
```bash
python disney.py
```

**Para rodar o script de conselhos:**
```bash
python conselhos.py
```

**Para rodar o script de países:**
```bash
python country.py
```

**Para rodar o script do OpenStreetMap:**
```bash
python openstreetmap.py
```

## 🧠 Tecnologias Utilizadas

* **Python 3**
* **Biblioteca `requests`** (para comunicação HTTP e consumo das APIs)
* **JSON** (para estruturação, leitura e parseamento de dados de resposta)
