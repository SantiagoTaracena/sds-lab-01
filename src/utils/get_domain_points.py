from urllib.parse import urlparse

def get_domain_points(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain.count(".")
