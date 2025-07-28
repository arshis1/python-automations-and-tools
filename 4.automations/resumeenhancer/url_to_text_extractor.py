import requests
from bs4 import BeautifulSoup

def extract_all_meta_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        metadata = {}

        # Get <title> tag separately
        if soup.title and soup.title.string:
            metadata['title'] = soup.title.string.strip()

        # Extract all meta tags dynamically
        for meta in soup.find_all('meta'):
            name = meta.get('name') or meta.get('property')
            content = meta.get('content')
            if name and content:
                metadata[name] = content.strip()

        return metadata

    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
