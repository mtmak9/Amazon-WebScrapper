# This script is a basic web scraper that retrieves product information from an Amazon product page and saves it in an Excel file.
# The script starts by importing the required libraries (requests, BeautifulSoup, and pandas). It then makes a request to an Amazon product page using the requests library and a specified User-Agent header. The response is then parsed using the BeautifulSoup library and stored in a soup object.
# Next, the script extracts the following information from the soup object:
# Title of the product
# Price of the product
# ASIN (Amazon Standard Identification Number) of the product
# URL of the product image
# The script then loops through the product details section and extracts the key-value pairs of information into a dictionary, where the keys are the product details and the values are their respective descriptions.
# Finally, the extracted information is stored in a pandas DataFrame and saved to an Excel file named "product_info.xlsx".
# Note: The script uses HTML tags and CSS selectors to locate the specific elements on the page. These selectors may not work if Amazon changes the structure of its product pages.
#
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make a request to the website
url = "https://www.amazon.com/dp/B07K8F5YDW"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
res = requests.get(url, headers=headers)

# Parse the HTML content of the page
soup = BeautifulSoup(res.content, 'html.parser')

# Extract the product details
title = soup.select_one('#productTitle').get_text().strip()
price = soup.select_one('#priceblock_ourprice').get_text().strip()
asin = soup.select_one('input[name=ASIN]')['value']
img_url = soup.select_one('#imgTagWrapperId img')['src']

# Extract the product information
product_info = {}
for li in soup.select('#prodDetails .content li'):
    key = li.select_one('.label').get_text().strip()
    value = li.select_one('.value').get_text().strip()
    product_info[key] = value

# Save the information to an Excel file
df = pd.DataFrame({
    'Title': [title],
    'Price': [price],
    'ASIN': [asin],
    'Image URL': [img_url],
    'Product Information': [product_info],
})
df.to_excel('product_info.xlsx', index=False)