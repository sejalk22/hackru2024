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

# URLs to scrape
#urls = [
###"https://newbrunswick.rutgers.edu/academics/schools-colleges/school-of-arts-and-sciences",
#"https://bloustein.rutgers.edu/",
###"https://gsapp.rutgers.edu/",
#"https://gse.rutgers.edu/",
#"https://www.masongross.rutgers.edu/",
#"https://www.business.rutgers.edu/","https://sas.rutgers.edu/",
#"https://comminfo.rutgers.edu/",
#"https://soe.rutgers.edu/apply",
#"https://sebs.rutgers.edu/",
#"https://grad.rutgers.edu/",
###"https://smlr.rutgers.edu/",
#"https://socialwork.rutgers.edu/",
#"https://pharmacy.rutgers.edu/",
#"https://njms.rutgers.edu/",
#"https://rwjms.rutgers.edu/",
#"https://sdm.rutgers.edu/",
#"https://shp.rutgers.edu/",
#"https://nursing.rutgers.edu/",
#"https://sph.rutgers.edu/" ]
