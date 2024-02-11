from urllib.parse import urlparse

def get_domain_lenght(url):
    parsed_url = urlparse(url)
    return len(parsed_url.netloc)
