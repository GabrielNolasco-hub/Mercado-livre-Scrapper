# Mercado Livre Scraper  Projeto Python  

## What (O que é?)  
Este é um projeto em Python que coleta automaticamente dados públicos do site **Mercado Livre**, utilizando web scraping com a biblioteca **BeautifulSoup**.  
Os resultados coletados são organizados com **pandas** e exportados em um arquivo **.csv**.  

O programa acessa os resultados de busca para qualquer termo e extrai:  
- Título do produto  
- Preço  
- Link para o anúncio  

---

## Why (Por que?)  
O objetivo do projeto é praticar:  
- Automação de coleta de dados com Python  
- Análise de páginas HTML com BeautifulSoup  
- Manipulação de dados com pandas  
- Exportação em formato de fácil consulta (CSV)  

Aplicações possíveis:  
- Comparação de preços  
- Estudos de mercado  
- Relatórios de tendências de consumo  

---

## Who (Quem participa?)  
- Desenvolvedores iniciantes ou intermediários que desejam aprender scraping, tratamento de dados e exportação.  
- Usuários ou pesquisadores que desejam consultar listas de produtos atualizadas de forma automatizada.  

---

## Where (Onde será usado?)  
- O script pode ser executado em **Windows** e **Linux**.  
- Os resultados são salvos em um arquivo chamado `produtos_mercado_livre.csv`, que pode ser aberto em qualquer planilha ou software de análise de dados.  

---

## When (Quando usar?)  
- Sempre que for necessário coletar informações públicas do Mercado Livre.  
- Ideal para consultas rápidas de preços, análises de tendências de produtos ou geração de relatórios.  

---

## How (Como funciona?)  

### 1. Clone o repositório do GitHub:  
```bash
git clone https://github.com/seu-usuario/mercado-livre-scraper.git
cd mercado-livre-scraper
```
### 2. Instale as dependências:
```bash
pip install -r requirements.txt
```
### 3. Execute o script principal:
```bash
python mercado_livre_scraper.py
