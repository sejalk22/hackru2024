import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Import urljoin function

def scrape_link_content(url):
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

def scrape_links_in_urls(urls):
    for url in urls:
        # Send request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all hyperlinks present on webpage
            links = soup.find_all('a')

            # Counter for link number
            link_num = 0

            # Iterate through all links
            for link in links:
                href = link.get('href')
                if href:
                    # Increment link number
                    link_num += 1

                    # Construct absolute URL
                    absolute_url = urljoin(url, href)

                    # Scrape content of the link
                    content = scrape_link_content(absolute_url)
                    if content:
                        # Save the content to a file
                        with open(f"Graduate School of Applied and Professional Psychology_{link_num}_content.txt", "w", encoding="utf-8") as file:
                            file.write(content)
                        print(f"Content of link {link_num} in URL {url} saved to link_{link_num}_content.txt")
                    else:
                        print(f"Skipping link {link_num} in URL {url}: Failed to retrieve content.")
        else:
            print(f"Failed to retrieve content from the URL: {url}")

# URLs to scrape
urls = [
 #"https://newbrunswick.rutgers.edu/academics/schools-colleges/school-of-arts-and-sciences",
#" https://bloustein.rutgers.edu/",
"https://gsapp.rutgers.edu/",
#"https://gse.rutgers.edu/",
#"https://www.masongross.rutgers.edu/",
#"https://www.business.rutgers.edu/","https://sas.rutgers.edu/",
#"https://comminfo.rutgers.edu/",
#"https://soe.rutgers.edu/apply",
#"https://sebs.rutgers.edu/",
#"https://grad.rutgers.edu/",
#"https://smlr.rutgers.edu/",
#"https://socialwork.rutgers.edu/",
#"https://pharmacy.rutgers.edu/",
#"https://njms.rutgers.edu/",
#"https://rwjms.rutgers.edu/",
#"https://sdm.rutgers.edu/",
#"https://shp.rutgers.edu/",
#"https://nursing.rutgers.edu/",
#"https://sph.rutgers.edu/"
]

# Scrape links in all the URLs
scrape_links_in_urls(urls)

