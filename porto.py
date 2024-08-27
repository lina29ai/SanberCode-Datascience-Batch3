import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_kompas():
    # Request the Kompas homepage
    url = 'https://www.kompas.com'
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return
    
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the popular news section
    popular_news_section = soup.find('div', class_='most__wrap')
    if not popular_news_section:
        print("Could not find the popular news section")
        return
    
    # Extract the titles of the popular news articles
    titles = popular_news_section.find_all('div', class_='most__title')
    if not titles:
        print("Could not find the popular news titles")
        return
    
    # Create a list of the titles
    titles_list = [title.get_text(strip=True) for title in titles[:5]]  # Get only the first 5 titles
    
    # Create a DataFrame
    df = pd.DataFrame(titles_list, columns=["Judul Berita Populer"])
    
    # Print the DataFrame
    print(df)

# Call the function
scrape_kompas()
