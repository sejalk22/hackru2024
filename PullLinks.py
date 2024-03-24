import requests
from bs4 import BeautifulSoup

def get_sublinks(url):
    try:
        # Send a request to the URL
        response = requests.get(url)
        # Initialize BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all anchor tags in the HTML and extract the href attributes
        links = [link.get('href') for link in soup.find_all('a') if link.get('href') != None]
        # Filter and format the links properly (you might need to adjust this based on the site structure)
        links = [link if link.startswith('http') else url + link for link in links]
        return links
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
url = "https://bloustein.rutgers.edu/"  # Replace with the website you are interested in
sublinks = get_sublinks(url)
print(sublinks)
