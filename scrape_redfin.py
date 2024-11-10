import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL for the website
base_url = "https://www.exness.com"

# Send a GET request to the page and handle potential redirection
url = "https://www.exness.com"
response = requests.get(url, allow_redirects=True)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all anchor tags (links)
links = soup.find_all('a')

# Set to store unique links
unique_links = set()

# Iterate over each link and process
for link in links:
    href = link.get('href')
    
    # Skip if the link is empty or already processed
    if href is None or href in unique_links:
        continue
    
    # Convert relative URLs to absolute URLs
    full_url = urljoin(base_url, href)
    
    # Filter links: Only keep links containing "blog" and belonging to the base domain
    if "blog" in full_url and base_url in full_url:
        print(f"Blog Link: {full_url}")
    
    # Add the link to the set to avoid duplicates
    unique_links.add(full_url)

# Optional: Save unique links to a file
with open("scraped_links.txt", "w") as f:
    for link in unique_links:
        f.write(link + "\n")
