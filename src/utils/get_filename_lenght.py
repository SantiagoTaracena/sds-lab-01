import os
from urllib.parse import urlparse

def get_filename_lenght(url):
    parsed_url = urlparse(url)
    return len(os.path.basename(parsed_url.path))
