🛒 Mercado Livre Scraper – Projeto Python
1. What (O que é?)

Um projeto em Python que coleta automaticamente dados públicos do site Mercado Livre, usando web scraping com BeautifulSoup, organiza os resultados com Pandas e exporta-os em um arquivo .csv.

O programa acessa os resultados de busca para qualquer termo e extrai:

📌 Título do produto

💰 Preço

🔗 Link para o anúncio

2. Why (Por que?)

Praticar automação de coleta de dados com Python, uso do BeautifulSoup para análise de páginas HTML, manipulação com Pandas e exportação em formato de fácil consulta (CSV).

Esse tipo de solução pode ser aplicado em:

Comparação de preços

Estudos de mercado

Relatórios de tendências de consumo

3. Who (Quem participa?)

👨‍💻 Desenvolvedores iniciantes ou intermediários que desejam aprender scraping, tratamento de dados e exportação

📊 Usuários ou pesquisadores que queiram consultar listas de produtos atualizadas de forma automatizada

4. Where (Onde será usado?)

💻 O script roda em Windows e Linux

📂 Os resultados são salvos em um arquivo produtos_mercado_livre.csv, que pode ser aberto em qualquer planilha ou software de análise

5. When (Quando usar?)

Sempre que for necessário coletar informações públicas do Mercado Livre

Ideal para consultas rápidas de preços, análises de tendências de produtos ou geração de relatórios

6. How (Como funciona?)

Clone o repositório no GitHub:

git clone https://github.com/seu-usuario/mercado-livre-scraper.git
cd mercado-livre-scraper


Instale as dependências:

pip install -r requirements.txt


Execute o script principal:

python mercado_livre_scraper.py


O programa acessa o Mercado Livre, coleta os dados da busca, organiza com Pandas e salva no arquivo produtos_mercado_livre.csv
