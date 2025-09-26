import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

def scrape_mercado_livre(search_term="placa de video"):
    """
    Acessa o site do Mercado Livre, busca por um termo, coleta dados dos produtos
    e os salva em um arquivo .csv.
    """
    # Formata o termo de busca para ser usado na URL
    search_term_formatted = search_term.replace(" ", "-")
    url = f"https://lista.mercadolivre.com.br/{search_term_formatted}"

    # Cabeçalhos para simular um navegador e evitar bloqueios
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    }

    print(f"Acessando a página de busca para: '{search_term}'...")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Lança um erro para status HTTP ruins (4xx ou 5xx)
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return

    # Utiliza o BeautifulSoup para analisar o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra todos os itens da lista de resultados
    # A classe pode mudar, é importante inspecionar o site se parar de funcionar
    products = soup.find_all('div', class_='poly-card__content')

    if not products:
        print("Nenhum produto encontrado. A estrutura do site pode ter mudado.")
        return

    print(f"Encontrados {len(products)} produtos. Extraindo dados...")
    
    products_data = []
    # Itera sobre cada produto encontrado
    for product in products:
        try:
            # Extrai o título do produto
            title_element = product.find('h3', class_='poly-component__title-wrapper')
            title = "N/A"
            if title_element:
                a_tag = title_element.find('a')
                if a_tag:
                    title = a_tag.text.strip()


            # Extrai o preço do produto
            price_container = product.find('span', class_='andes-money-amount')

            price_str = "0"
            if price_container:
                fraction = price_container.find('span', class_='andes-money-amount__fraction')
                cents = price_container.find('span', class_='andes-money-amount__cents')

                if fraction:
                    # Remove separador de milhar (.)
                    price_str = fraction.text.replace('.', '')
                    if cents:
                        price_str += f".{cents.text}"

            # Converte o preço em float
            try:
                price = float(price_str)
            except ValueError:
                price = 0.0

            # Extrai o link do produto
            link_element = product.find('h3', class_='poly-component__title-wrapper')

            link = "N/A"
            if link_element:
                a_tag = link_element.find('a')
                if a_tag and 'href' in a_tag.attrs:
                    link = a_tag['href']
            
            products_data.append({
                "Título": title,
                "Preço (R$)": price,
                "Link": link
            })
        except (AttributeError, ValueError) as e:
            # Pula o produto se algum campo essencial não for encontrado
            print(f"Erro ao processar um produto: {e}")
            continue

    if not products_data:
        print("Nenhum dado de produto foi extraído com sucesso.")
        return

    # Cria um DataFrame do Pandas com os dados coletados
    df = pd.DataFrame(products_data)
    
    # Ordena os produtos do mais barato para o mais caro
    df = df.sort_values(by="Preço (R$)", ascending=True)

    # Define o nome do arquivo de saída
    output_filename = "produtos_mercado_livre.csv"
    
    # Salva o DataFrame em um arquivo CSV
    df.to_csv(output_filename, index=False, encoding='utf-8-sig')

    print("-" * 30)
    print(f"Arquivo '{output_filename}' gerado com sucesso!")
    print(f"Total de {len(df)} produtos salvos.")
    print("Top 5 produtos mais baratos encontrados:")
    # Exibe os 5 primeiros produtos do DataFrame formatado
    print(tabulate(df.head(5), headers="keys", tablefmt="grid", showindex=False))


if __name__ == "__main__":
    # Você pode alterar o termo de busca aqui se desejar
    scrape_mercado_livre(search_term="placa de video rtx 4060")
