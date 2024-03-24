import requests
from bs4 import BeautifulSoup
import urls
from urls import urls  # Import the list of URLs from urls.py

# Define the get_sublinks function
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

all_sublinks = []

# Iterate over the list of URLs
for url in urls:
    # Get the sublinks for the current URL
    sublinks = get_sublinks(url)
    # Extend the master list with the sublinks from the current URL
    all_sublinks.extend(sublinks)

# Print the complete list of sublinks
print("All Sublinks:", all_sublinks)
