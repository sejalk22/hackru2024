import requests
from bs4 import BeautifulSoup

def scrape_page_content(url):
    # Send request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all content within the HTML
        all_content = soup.get_text()

        # Return the extracted content
        return all_content
    else:
        print(f"Failed to retrieve content from the URL: {url}")
        return None

# URLs to scrape
urls = [
    "https://newbrunswick.rutgers.edu/academics/schools-colleges/school-of-arts-and-sciences",
    " https://bloustein.rutgers.edu/","https://gsapp.rutgers.edu/",
"https://gse.rutgers.edu/",
"https://www.masongross.rutgers.edu/",
"https://www.business.rutgers.edu/","https://sas.rutgers.edu/"
"https://comminfo.rutgers.edu/"
"https://soe.rutgers.edu/apply"
"https://sebs.rutgers.edu/"
"https://grad.rutgers.edu/"
"https://smlr.rutgers.edu/"
"https://socialwork.rutgers.edu/"
"https://pharmacy.rutgers.edu/"
"https://njms.rutgers.edu/"
"https://rwjms.rutgers.edu/"
"https://sdm.rutgers.edu/"
"https://shp.rutgers.edu/"
"https://nursing.rutgers.edu/"
"https://sph.rutgers.edu/"
]

# Scrape content from all the URLs
for i, url in enumerate(urls, 1):
    # Scrape the content of the page
    content = scrape_page_content(url)
    
    # Save the content to a text file
    if content:
        with open(f"scraped_content_{i}.txt", "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Content of URL {i} saved to scraped_content_{i}.txt")
    else:
        print(f"Skipping URL {i}: Failed to retrieve content.")
