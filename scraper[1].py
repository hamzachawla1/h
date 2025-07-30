import requests
from bs4 import BeautifulSoup

def get_reviews(product_name):
    query = product_name.replace(" ", "+")
    url = f"https://www.flipkart.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select("a._1fQZEK")

    if not links:
        return []

    product_link = "https://www.flipkart.com" + links[0].get("href")
    response = requests.get(product_link, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    reviews = []
    review_blocks = soup.select("div._27M-vq")

    for block in review_blocks[:10]:
        rating = block.select_one("div._3LWZlK")
        text = block.select_one("div.t-ZTKy")
        if rating and text:
            reviews.append({
                "rating": rating.text,
                "text": text.text.strip()
            })

    return reviews
