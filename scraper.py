import requests
from bs4 import BeautifulSoup

def scrape_baltic_stocks():
    url = "https://nasdaqbaltic.com/statistics/en/shares"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    stocks = []
    rows = soup.select("table.data-table tbody tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 8:
            continue  # skip incomplete rows

        try:
            stock = {
                "symbol": cols[0].get_text(strip=True),
                "name": cols[1].get_text(strip=True),
                "peRatio": float(cols[5].get_text(strip=True) or 0),
                "roe": float(cols[6].get_text(strip=True).replace('%', '').strip() or 0),
                "eps": float(cols[7].get_text(strip=True) or 0),
            }
            stocks.append(stock)
        except Exception:
            continue

    return stocks
