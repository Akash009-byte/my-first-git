import requests
from bs4 import BeautifulSoup
import pandas as pd


def run_market_scraper():
    # 1. Target URL (A practice site for scraping)
    url = "http://books.toscrape.com/"

    # 2. Fetch the website content
    response = requests.get(url)

    # 3. Parse the HTML structure
    soup = BeautifulSoup(response.text, 'html.parser')

    market_data = []
    # 4. Find all book containers on the page
    for book in soup.find_all('article', class_='product_pod'):
        # Extract the full title and price
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text

        market_data.append({
            "Product Name": title,
            "Price": price
        })

    # 5. Save to a CSV file (This creates your Data Pipeline)
    df = pd.DataFrame(market_data)
    df.to_csv('scraped_market_data.csv', index=False)

    print(f"Success! Scraped {len(df)} items and saved to 'scraped_market_data.csv'.")


if __name__ == "__main__":
    run_market_scraper()