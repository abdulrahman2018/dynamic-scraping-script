
# Web Scraper for Extracting Blog Links

This project is a Python-based web scraping tool that extracts and lists blog-related links from a given website. The scraper uses `requests` and `BeautifulSoup` to fetch and parse the HTML content, filtering for blog links while avoiding duplicates.

## Features

- Scrapes a specified website for all anchor (`<a>`) tags (links).
- Filters out links that are not related to the blog (based on the presence of the word "blog" in the URL).
- Stores the unique blog links in a `.txt` file for further use.
- Handles relative URLs and converts them to absolute URLs.
- Ensures no duplicate links are saved.

## Technologies Used

- **Python**  
- **Requests** library (for sending HTTP requests)  
- **BeautifulSoup** library (for parsing HTML content)  
- **urllib.parse** (for handling URL resolution)

## Requirements

Before running the script, make sure to install the required libraries:

```bash
pip install requests beautifulsoup4
```

## How It Works

1. The script sends a GET request to the specified website.
2. It parses the HTML content to extract all links (`<a>` tags).
3. It checks each link to ensure it’s not a duplicate.
4. It filters links containing the word "blog" and ensures they belong to the base domain.
5. It outputs the valid blog links to the console and saves them to a `.txt` file.

## Output

- A `.txt` file named `scraped_links.txt` is generated, containing all the unique blog-related links found on the website.

## Usage

To run the scraper, simply execute the script in your Python environment. You can modify the base URL in the script to target a different website.

```bash
python scraper.py
```

![Uploading image.png…]()
