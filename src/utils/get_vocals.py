from urllib.parse import urlparse

def get_vocals(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return sum([1 for char in domain if (char.lower() in "aeiou")])
