import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Step 1: Send a request to the website
url = 'http://books.toscrape.com/'
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
books = soup.find_all('article', class_='product_pod')

titles = []
prices = []

for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    titles.append(title)
    prices.append(price)

# Step 4: Store data in a DataFrame
data = pd.DataFrame({
    'Title': titles,
    'Price': prices
})

# Step 5: Save data to a CSV file
data.to_csv('books.csv', index=False)

# Print the current working directory
print(f"Data saved to books.csv in directory: {os.getcwd()}")
