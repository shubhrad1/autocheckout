
import json
import os
from url_extract import extract_website_name




def read_cache(url):
    website_name=extract_website_name(url)
    cache_file = "cache.json"
    if not os.path.exists(cache_file):
        return False , [],"Cache file does not exist."
    with open(cache_file, "r") as f:
        cache = json.load(f)

    if website_name in cache:
        return True, cache[website_name],None
    else:
        return False,[],None

def write_cache(url, elements):
    website_name=extract_website_name(url)
    cache_file = "cache.json"
    if os.path.exists(cache_file):
        with open(cache_file, "r") as f:
            cache = json.load(f)
    else:
        cache = {}

    cache[website_name] = elements

    with open(cache_file, "w") as f:
        json.dump(cache, f, indent=4)  # Use indent for better readability

